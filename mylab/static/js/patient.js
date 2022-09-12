console.log("Hello world")
const url = window.location.href
const searchForm = document.getElementById("search-form")
const searchInput = document.getElementById("search-input")
const resultsBox = document.getElementById("results-box")

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value

const sendSearchData = (patients) => {
  $.ajax({
    type: 'POST',
    url: 'search',
    data: {
      'csrfmiddlewaretoken': csrf,
      'patients': patients
    },
    success: (res)=>{
      console.log(res.data)
      const data = res.data
      if (Array.isArray(data)){
        resultsBox.innerHTML = ""
        data.forEach(patients=>{
          resultsBox.innerHTML += `
          <a href="" class="item">
            <div class='row mt-3 mb-3'
              <div class ="col-2"
                <h5>${patients.first_name}</h5>
              </div>
              <div class ="col-2"
                <h5>${patients.last_name}</h5>
              </div>
            </div>
          </a>
          `
        })
      } else{
        if (searchInput.value.length > 0){
          resultsBox.innerHTML = `<b>${data}</b>`
        } else {
          resultsBox.classList.add('not-visible')
        }
      }
    },
    error: (err) => {
      console.log(err)
    }
  })
}

searchInput.addEventListener("keyup", e=>{
  console.log(e.target.value)

  if (resultsBox.classList.contains('not-visible')){
      resultsBox.classList.remove('not-visible')
  }

  sendSearchData(e.target.value)
})
