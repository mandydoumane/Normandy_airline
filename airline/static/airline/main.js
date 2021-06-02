const depart = document.getElementById('id_departure');
const arrive = document.getElementById('id_arrival');
const paris = arrive[1]
const marseille = arrive[2]
const rome = arrive[3]
const barcelone = arrive[4]
function filtre_arrive() {

        arrive[0].classList.add('ville_cache')
        paris.classList.add('ville_cache')
        marseille.classList.add('ville_cache')
        rome.classList.add('ville_cache')
        barcelone.classList.add('ville_cache')

    if (depart.value == '1'){
        
        marseille.classList.remove('ville_cache')
   
    }

    else if (depart.value == '2'){
        paris.classList.remove('ville_cache')
   
    }

    else if (depart.value == '3'){
        barcelone.classList.remove('ville_cache')
        paris.classList.remove('ville_cache')
   
    }

    else if (depart.value == '4'){
        rome.classList.remove('ville_cache')

    }
}
depart.addEventListener('click', filtre_arrive);
