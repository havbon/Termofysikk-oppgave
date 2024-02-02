const resultat = document.getElementById("resultat")

function regnut() {
    let luftmasse = parseFloat(document.getElementById("luftmasse").value)
    let lufttemperatur = parseFloat(document.getElementById("lufttemperatur").value) + 273
    let jernmasse = parseFloat(document.getElementById("jernmasse").value)
    let jerntemperatur = parseFloat(document.getElementById("jerntemperatur").value) + 273

    let cluft = 1005;
    let cjern = 450;

    let svar = (cluft * luftmasse * lufttemperatur + cjern * jernmasse * jerntemperatur) / (jernmasse * cjern + cluft * luftmasse);

    resultat.innerText = Math.round(svar - 273);
}