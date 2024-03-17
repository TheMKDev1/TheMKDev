

function LoadFrame(frameId) {
    var gameFrame = document.getElementById(frameId);

    gameFrame.src = gameFrame.getAttribute('data-link');
    document.getElementById(gameFrame.getAttribute('data-container')).style.border = "2px black solid";
}

function UnloadFrame(frameId) {
    var gameFrame = document.getElementById(frameId);

    gameFrame.src = "about:blank";
    document.getElementById(gameFrame.getAttribute('data-container')).style.border = "0px black solid";
}


document.getElementById("CableClimbingPlay").onclick = function() {
    LoadFrame("CableClimbingFrame");
};

document.getElementById("CableClimbingStop").onclick = function() {
    UnloadFrame("CableClimbingFrame");
};


document.getElementById("ManiacTanksPlay").onclick = function() {
    LoadFrame("ManiacTanksFrame");
};

document.getElementById("ManiacTanksStop").onclick = function() {
    UnloadFrame("ManiacTanksFrame");
};


document.getElementById("VariableWarfarePlay").onclick = function() {
    LoadFrame("VariableWarfareFrame");
};

document.getElementById("VariableWarfareStop").onclick = function() {
    UnloadFrame("VariableWarfareFrame");
};


document.getElementById("OrbiterPlay").onclick = function() {
    LoadFrame("OrbiterFrame");
};

document.getElementById("OrbiterStop").onclick = function() {
    UnloadFrame("OrbiterFrame");
};

