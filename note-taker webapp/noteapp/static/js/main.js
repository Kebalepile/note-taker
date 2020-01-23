import about from "./components/about.js";
import addnote from "./components/addNote.js";

const aboutBtn = document.querySelector("#aboutBtn"),
    // logout = document.querySelector("#logout"),
    newNote = document.querySelector("#newNote");

newNote.onclick = e => addnote();
aboutBtn.onclick = e => {
    about();
    aboutBtn.disabled=true;
};
