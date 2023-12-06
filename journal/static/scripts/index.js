function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function edit_table(id) {
    data = {
        height: [],
        weight: [],
        vital_capacity: [],
        strength: [],
        right_hand_strength: [],
        left_hand_strength: [],
        chs: [],
        ads: [],
        add: []
    }
    for (let i = 1; i < 9; i++) {
        data.height.push(document.getElementById(`height_${i}`).innerText)
        data.weight.push(document.getElementById(`weight_${i}`).innerText)
        data.vital_capacity.push(document.getElementById(`vital_capacity_${i}`).innerText)
        data.strength.push(document.getElementById(`strength_${i}`).innerText)
        data.right_hand_strength.push(document.getElementById(`right_hand_strength_${i}`).innerText)
        data.left_hand_strength.push(document.getElementById(`left_hand_strength_${i}`).innerText)
        data.chs.push(document.getElementById(`chs_${i}`).innerText)
        data.ads.push(document.getElementById(`ads_${i}`).innerText)
        data.add.push(document.getElementById(`add_${i}`).innerText)
    }
     fetch(`http://127.0.0.1:8000/profile/${id}/`, {
          method: "POST",
          body: JSON.stringify({
            data
         }),
         headers: {
              "X-CSRFToken": getCookie("csrftoken")
         }
     })
    location.reload(true);
}

function edit_functional_table(id) {
    data = {
        genchi: [],
        shtange: [],
        functional_ccc: [],
        orthostatic: [],
    }
    for (let i = 1; i < 9; i++) {
        data.genchi.push(document.getElementById(`genchi_${i}`).innerText)
        data.shtange.push(document.getElementById(`shtange_${i}`).innerText)
        data.functional_ccc.push(document.getElementById(`functional_ccc_${i}`).innerText)
        data.orthostatic.push(document.getElementById(`orthostatic_${i}`).innerText)
    }
     fetch(`http://127.0.0.1:8000/functional_table/`, {
          method: "POST",
          body: JSON.stringify({
            data
         }),
         headers: {
              "X-CSRFToken": getCookie("csrftoken")
         }
     })
    location.reload(true);
}

function colorize_functional_table() {
    for (let i = 1; i < 9; i++) {
        if (document.getElementById(`genchi_${i}`).innerText) {
            element = document.getElementById(`genchi_${i}`)
            amount = Number(element.innerText)

            if (amount >= 40 && amount <= 60) {
                element.style.backgroundColor = "green"
            }
            if (amount >= 25 && amount <= 39) {
                element.style.backgroundColor = "darkorange"
            }
            if (amount >= 20 && amount <= 24) {
                element.style.backgroundColor = "orangered"
            }
            if (amount <= 20) {
                element.style.backgroundColor = "red"
            }
        }
        else if (document.getElementById(`shtange_${i}`).innerText) {
            element = document.getElementById(`shtange_${i}`)
            amount = Number(element.innerText)

            if (amount >= 59 && amount <= 90) {
                element.style.backgroundColor = "green"
            }
            if (amount >= 40 && amount <= 55) {
                element.style.backgroundColor = "darkorange"
            }
            if (amount >= 30 && amount <= 39) {
                element.style.backgroundColor = "orangered"
            }
            if (amount < 30) {
                element.style.backgroundColor = "red"
            }
        }
        else if (document.getElementById(`functional_ccc_${i}`).innerText) {
            element = document.getElementById(`functional_ccc_${i}`)
            amount = Number(element.innerText)

            if (amount < 20) {
                element.style.backgroundColor = "green"
            }
            if (amount >= 21 && element <= 40) {
                element.style.backgroundColor = "darkorange"
            }
            if (amount >= 41 && amount <= 65) {
                element.style.backgroundColor = "orangered"
            }
            if (amount >= 66 && amount <= 75) {
                element.style.backgroundColor = "red"
            }
        }
        else if (document.getElementById(`orthostatic_${i}`).innerText) {
            element = document.getElementById(`orthostatic_${i}`)
            amount = Number(element.innerText)

            if (amount < 10) {
                element.style.backgroundColor = "green"
            }
            if (amount >= 11 && element <= 16) {
                element.style.backgroundColor = "darkorange"
            }
            if (amount >= 17 && amount <= 22) {
                element.style.backgroundColor = "orangered"
            }
            if (amount >= -2 && amount <= -5) {
                element.style.backgroundColor = "red"
            }
        }
    }

}

