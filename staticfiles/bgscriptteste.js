import * as THREE from 'three';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader.js'

// Create a new scene
const scene2 = new THREE.Scene();

const div = document.getElementsByClassName('div-block-27')[0];

// Create a new camera
const camera = new THREE.PerspectiveCamera(60, div.offsetHeight / div.offsetWidth, 0.1, 1000);
camera.position.z = 1.3;
camera.position.y = 0;

// Create a new renderer
const renderer2 = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer2.setSize(div.offsetWidth, div.offsetHeight);

// TESTE LIGHT
const light = new THREE.SpotLight(0xffffff, .000001);
light.position.set(0, 8, 15).normalize();
light.angle = Math.PI/1;
light.penumbra = 1;

//scene2.add(light);

// Get the div to render on
div.appendChild(renderer2.domElement);
//renderer2.domElement.style.borderRadius = '100%';
//renderer2.domElement.style.position = '50%';
//renderer2.domElement.style.width = '100%';

// Declare the mixer variable outside the loader2.load() callback function
let mixer;

let video = {}
    //Declaring the video
    video['tst'] = document.createElement("video");
    video['tst'].src = '/videos/CLipChamps.mp4';
    video['tst'].muted = true;
    video['tst'].playsInline = true;
    video['tst'].autoplay = true;
    video['tst'].loop = true;
    video['tst'].play();

    function determineModelPath() {
        // Get the width of the screen
        const screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
      
        // Define the model path based on the screen size
        let modelPath;
        if (screenWidth < 768) {
          modelPath = '/models/TesteCelular2Mobile.glb'; // Path for mobile devices
        } else {
          modelPath = '/models/TesteCelular2.glb'; // Path for desktop devices
        }
      
        return modelPath;
      }

    
    const modelPath = determineModelPath();

// load the GLTF model
const loader2 = new GLTFLoader();
loader2.load(
  modelPath, // the path to the GLTF file
  (gltf2) => {
    // set the scale of the model
    gltf2.scene.scale.set(.6, .75, .4);
    // add the model to the scene
    scene2.add(gltf2.scene);

    /*console.log(gltf2.scene);*/


    const videoTexture = new THREE.VideoTexture(video['tst']);
    videoTexture.minFilter = THREE.NearestFilter;
    videoTexture.magFilter = THREE.NearestFilter;
    videoTexture.generateMipmaps = false;
    //videoTexture.encoding = THREE.SRGBColorSpace;
    videoTexture.flipY = false;

    const gradientCanvas = document.createElement('canvas');
    gradientCanvas.width = 256;
    gradientCanvas.height = 1;
    const context = gradientCanvas.getContext('2d');
    const gradient = context.createLinearGradient(256, 0, 0, 0);
    gradient.addColorStop(0, '#ffffff'); // white
    gradient.addColorStop(1, '#000000'); // black
    context.fillStyle = gradient;
    context.fillRect(0, 0, 256, 1);
    const gradientTexture = new THREE.CanvasTexture(gradientCanvas);
    const gradMaterial = new THREE.MeshBasicMaterial({ map: gradientTexture });

    gltf2.scene.traverse((child) => {
      if (child.name === 'Plane001') {
        // Assign the video texture to the mesh material
        child.material = new THREE.MeshBasicMaterial({
          map: videoTexture,
        })
      }
      else if (child.name === 'lala') {
        child.material = new THREE.MeshBasicMaterial({
          /*map: gradientTexture,*/
          roughness: 0.2, 
          metalness: 1.0,
          clearcoat: 0.5, 
          clearcoatRoughness: 0.5,
        })
      }
    });

    // Get the animation
    const animations = gltf2.animations;
    const numAnimations = animations.length;

    // Create a mixer to play the animation
    mixer = new THREE.AnimationMixer(gltf2.scene);

    // Create an animation action from the animation
    const actions = [];
    for (let i=0; i<numAnimations; i++) {
      const animation = animations[i];
      animation.duration = 15;
      const action = mixer.clipAction(animation);
      actions.push(action);
    }

    actions.forEach(action => action.play());
  },
  /*(xhr) => {
    // called while loading is progressing
    console.log(`${(xhr.loaded / xhr.total * 100)}% loaded`);
  },
  (error) => {
    // called when loading has errors
    console.error(error);
  }*/
);

// Animate the cube rotation
let prevTime = 0;
function animate() {
  requestAnimationFrame(animate);
  const time = performance.now();
  const deltaTime = (time - prevTime)*0.001;
  prevTime = time;

  // Check if the mixer is defined before updating it
  if (mixer) {
    mixer.update(deltaTime);
  }

  renderer2.render(scene2, camera);
}

animate();
