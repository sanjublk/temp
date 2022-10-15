
function sortBySearch(e) {
    let hotels = document.getElementsByClassName('hotel')
    console.log(e.target.value)

    Array.from(hotels).forEach((hotel)=> {
        let hotelName = hotel.querySelector('.lead').innerText
        if (hotelName.toLowerCase().includes(e.target.value) === false && e.target.value != '') {
           hotel.style.display = 'none'
        }
        else {
           hotel.style.display = 'block'
        }
    })

}

function main() {
    let searchInput = document.getElementById('searchInput')
    searchInput.oninput = (e)=> {sortBySearch(e)}

}

main()