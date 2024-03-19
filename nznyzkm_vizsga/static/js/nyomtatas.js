

const megrendelesID = document.getElementById("id").value;

const getURL = 'http://127.0.0.1:8000/api/megrendelesek?format=json';
getMegrendelesek();

function getMegrendelesek(){
    fetch(getURL).then( res => res.json()).then(data => {
        
        filterMegrendeles(data, megrendelesID)
        
    })
    
}
function filterMegrendeles(data, id){
    for(var i = 0; i<data.length; i++){
        
        
        if (data[i].id == megrendelesID) {
            
            generateValues(data[i])
        }
    }
}

function generateValues(jsondata){
    var kiallito_neve = document.getElementById('kialitoneve');
    var munkalap_szama = document.getElementById('munkalap_szama');
    var bizonylat_kelte = document.getElementById('bizonylat_kelte');
    var teljesites_datuma = document.getElementById('teljesites_datuma');
    var cikkszam = document.getElementById('cikkszam');
    
    var mennyiseg = document.getElementById('mennyiseg');
    var meret = document.getElementById('meret');
    var anyag = document.getElementById('anyag');

    
    kiallito_neve.innerText = 
        'Kiállító neve: '+jsondata.dolgozo.first_name+' '+jsondata.dolgozo.last_name;

    munkalap_szama.innerText = 'Munkalap száma: '+jsondata.munkalap_szama;
    bizonylat_kelte.innerText = 'Bizonylat kelte: '+jsondata.datumKezdes;
    teljesites_datuma.innerText = 'Teljesítés dátuma: '+jsondata.datumBefejezes;
    cikkszam.innerText = jsondata.alapanyag.id;
    mennyiseg.innerText = jsondata.felhasznaltMennyiseg;
    meret.innerText = jsondata.alapanyag.meret_valaszt;
    anyag.innerText = jsondata.alapanyag.anyagtipusa;

   // window.print();

   // window.history.back();
    
}
