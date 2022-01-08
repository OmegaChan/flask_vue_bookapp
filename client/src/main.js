import { createApp } from 'vue';
import App from './App.vue';


import router from './router';

// import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'

// import $ from 'jquery'

// import 'bootstrap/dist/js/ bootstrap.bundle.min.js '

import 'bootstrap/dist/js/bootstrap.min.js'

createApp(App).use(router).mount('#app')