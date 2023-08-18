import * as THREE from 'three';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader.js'

const scene3 = new THREE.Scene

const div2 = document.getElementsByClassName('rotating-cube')[0];

const camera = new THREE.PerspectiveCamera(60, div2.offsetHeight / div2.offsetWidth, 0.1, 1000);
camera.position.z = 4.4;
camera.position.y = 0.4;

const renderer3 = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer3.setSize(div2.offsetWidth, div2.offsetHeight);

const light = new THREE.SpotLight(0xffffff, .000001);
light.position.set(0, 8, 15).normalize();
light.angle = Math.PI/1;
light.penumbra = 1;

scene3.add(light);

var geometry = new THREE.BoxGeometry(1, 1, 1);
var material = new THREE.MeshBasicMaterial({ wireframe: true, color: 0x7974F5 });
var cube = new THREE.Mesh(geometry, material);
scene3.add(cube);

div2.appendChild(renderer3.domElement);

function animate() {
    requestAnimationFrame(animate);
    
    cube.rotation.x += 0.001;
    cube.rotation.y += 0.007;
    /*cube.rotation.z += 0.006;*/
    renderer3.render(scene3, camera);
}
animate();
