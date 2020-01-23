import note from "./note.js";
export default () => {
    // create a form for note to be created.
    const form = document.createElement("div"),
        label = document.createElement("label"),
        textarea = document.createElement("textarea"),
        saveBtn = document.createElement("input"),
        cancelBtn = document.createElement("button"),
        option = document.createElement("div");
    label.for = "note";
    label.textContent = "Write note";
    textarea.id = "note";
    textarea.rows = "6";
    textarea.cols = "12";
    textarea.minLength = "5";
    saveBtn.type = "submit";
    saveBtn.value = "Save";
    saveBtn.id = "save_note";
    cancelBtn.textContent = "Cancel";
    cancelBtn.id = "cancel";
    option.id = "choice";

    [saveBtn, cancelBtn].forEach(v => option.appendChild(v));
    
    [label, textarea, option].forEach(val => form.appendChild(val));
    form.classList.add("note_form");

    cancelBtn.onclick = e =>  document.body.removeChild(form);
 
    saveBtn.onclick = e => {
        note(textarea.value);
        document.body.removeChild(form);
    }

    document.body.appendChild(form);
}