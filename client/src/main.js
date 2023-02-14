import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faUserSecret,faLink, faChevronRight, faXmark, faHouseLaptop, faBookmark, faMagnifyingGlass, faDeleteLeft, faArrowLeft } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret, faLink, faChevronRight, faXmark, faHouseLaptop, faBookmark, faMagnifyingGlass, faDeleteLeft, faArrowLeft)

import "./assets/main.css";

const app = createApp(App);

app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon)

app.mount("#app");
