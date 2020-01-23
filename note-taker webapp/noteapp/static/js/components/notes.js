
export default (...notes) => {
    const noteList = document.querySelector(".container");
    for (let note of notes) {
        noteList.appendChild(note);
    }
}