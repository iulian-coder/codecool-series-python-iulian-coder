let actorsOfShow = document.getElementsByClassName('showName');


for (show of actorsOfShow) {
    show.addEventListener('click', handleShowClick)
}

function handleShowClick(event) {
    // console.log(event.target.id);
    let showId = event.target.id;
    fetch(`http://127.0.0.1:5000/api/show-actors/${showId}`)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            // console.log(mata[0].name);
            writeActors(data[0].name, showId);
        });
};

function writeActors(actorName, showId) {
    let actorsShow = document.getElementById(`show-${showId}`);
    actorsShow.innerHTML = `${actorName}`;
};