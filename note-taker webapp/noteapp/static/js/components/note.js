import notes from "./notes.js";

export default (note) => {
    const card = document.createElement("article"),
    done  = document.createElement("section"),
    btn = document.createElement("button"),
    msg = document.createElement("section");
    btn.textContent="Delete";   
    btn.onclick = e => {
        document.querySelector(".container").removeChild(card);
        fetch("/delete",{
            method:"DELETE",
            headers: {
                "Content-Type":"application/json; charset=utf-8"
            },
            body:JSON.stringify({"id": "note id"})
        }).then(res => res.json())
        .then(data =>  console.log(data))
        .catch(err => console.error(`Bothata ke bo: ${err}`))
    }  
    done.appendChild(btn);
    msg.textContent = note;
    card.classList.add('note');
    done.classList.add("done");
    msg.classList.add("msg");
    [done, msg].forEach(val => card.appendChild(val));

    fetch("/create_note",{
        method: "POST",
        headers: {
            "Content-Type": "application/json; charset=utf-8"
        },
        body:JSON.stringify({'body': note})
    }).then(res => res.json())
    .then( data => console.log(data))
    .catch( err => console.error(`Bothata ke bo =>: ${err}`));
    notes(card);
}