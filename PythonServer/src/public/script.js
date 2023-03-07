function requestHtml(url){
    return new Promise(async resolve => {
        const res = await fetch(url);
        const text = await res.text();
        resolve(text);
    })   
}

async function updateResult(){
    const dateInput = document.getElementById('date-input').value
    const html = await requestHtml(`/AI?date=${dateInput}`);
    const el = document.getElementsByClassName('result-window')[0];
    el.innerHTML = html;
    el.classList.add('expand');
}