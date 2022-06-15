import * as THREE from 'three';

let scene, camera, renderer, analyser, uniforms;

const startButton = document.getElementById( 'startButton' );
startButton.addEventListener( 'click', init );

const now_word = document.getElementById( 'now_word' ).innerText;


function init() {
    startButton.style.display = 'none';
    const fftSize = 128;
    const container = document.getElementById( 'canvas' );

    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setSize(window.innerWidth / 4, window.innerHeight / 3);
    renderer.setClearColor( 0x000000 );
    renderer.setPixelRatio( window.devicePixelRatio );
    container.appendChild( renderer.domElement );

    scene = new THREE.Scene();

    camera = new THREE.Camera();
    document.getElementById( 'startButton' );


    const listener = new THREE.AudioListener();
    const audio = new THREE.Audio( listener );
    const file = './static/music/' + now_word + '.mp3';

    const mediaElement = new Audio( file );
    mediaElement.play();

    audio.setMediaElementSource( mediaElement );


    analyser = new THREE.AudioAnalyser( audio, fftSize );

    //

    const format = ( renderer.capabilities.isWebGL2 ) ? THREE.RedFormat : THREE.LuminanceFormat;

    uniforms = {

        tAudioData: { value: new THREE.DataTexture( analyser.data, fftSize / 2, 1, format ) }

    };

    const material = new THREE.ShaderMaterial( {

        uniforms: uniforms,
        vertexShader: document.getElementById( 'vertexShader' ).textContent,
        fragmentShader: document.getElementById( 'fragmentShader' ).textContent

    } );

    const geometry = new THREE.PlaneGeometry( 2, 2 );

    const mesh = new THREE.Mesh( geometry, material );
    scene.add( mesh );

    //

    window.addEventListener( 'resize', onWindowResize );

    animate();

}



function onWindowResize() {

    renderer.setSize( window.innerWidth, window.innerHeight );

}

function animate() {

    requestAnimationFrame( animate );

    render();

}

function render() {

    analyser.getFrequencyData();

    uniforms.tAudioData.value.needsUpdate = true;

    renderer.render( scene, camera );

}

