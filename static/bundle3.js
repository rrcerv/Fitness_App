/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./bgscript3.js":
/*!**********************!*\
  !*** ./bgscript3.js ***!
  \**********************/
/***/ ((__unused_webpack___webpack_module__, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var three__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! three */ \"./node_modules/three/build/three.module.js\");\n\r\n\r\n\r\nconst scene3 = new three__WEBPACK_IMPORTED_MODULE_0__.Scene\r\n\r\nconst div2 = document.getElementsByClassName('rotating-cube')[0];\r\n\r\nconst camera = new three__WEBPACK_IMPORTED_MODULE_0__.PerspectiveCamera(60, div2.offsetHeight / div2.offsetWidth, 0.1, 1000);\r\ncamera.position.z = 4.4;\r\ncamera.position.y = 0.4;\r\n\r\nconst renderer3 = new three__WEBPACK_IMPORTED_MODULE_0__.WebGLRenderer({ antialias: true, alpha: true });\r\nrenderer3.setSize(div2.offsetWidth, div2.offsetHeight);\r\n\r\nconst light = new three__WEBPACK_IMPORTED_MODULE_0__.SpotLight(0xffffff, .000001);\r\nlight.position.set(0, 8, 15).normalize();\r\nlight.angle = Math.PI/1;\r\nlight.penumbra = 1;\r\n\r\nscene3.add(light);\r\n\r\nvar geometry = new three__WEBPACK_IMPORTED_MODULE_0__.BoxGeometry(1, 1, 1);\r\nvar material = new three__WEBPACK_IMPORTED_MODULE_0__.MeshBasicMaterial({ wireframe: true, color: 0x7974F5 });\r\nvar cube = new three__WEBPACK_IMPORTED_MODULE_0__.Mesh(geometry, material);\r\nscene3.add(cube);\r\n\r\ndiv2.appendChild(renderer3.domElement);\r\n\r\nfunction animate() {\r\n    requestAnimationFrame(animate);\r\n    \r\n    cube.rotation.x += 0.001;\r\n    cube.rotation.y += 0.007;\r\n    /*cube.rotation.z += 0.006;*/\r\n    renderer3.render(scene3, camera);\r\n}\r\nanimate();\r\n\n\n//# sourceURL=webpack://room-teste/./bgscript3.js?");

/***/ }),

/***/ "./node_modules/three/build/three.module.js":
/*!**************************************************!*\
  !*** ./node_modules/three/build/three.module.js ***!
  \**************************************************/
/***/ ((__unused_webpack___webpack_module__, __webpack_exports__, __webpack_require__) => {


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./bgscript3.js");
/******/ 	
/******/ })()
;