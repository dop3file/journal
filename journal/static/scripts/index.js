URL = "http://127.0.0.1:8000"

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function edit_table(id) {
    data = {
        height: [],
        weig    ht: [],
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
     fetch(`${URL}/profile/${id}/`, {
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
     fetch(`${URL}/functional_table/`, {
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

function edit_physicals(id) {
    console.log(1)
    data = {
        run: [],
        incline: [],
        bending: [],
        raising: [],
        pull_up: [],
        squat: []
    }
    for (let i = 1; i < 9; i++) {
        data.run.push(document.getElementById(`run_${i}`).innerText)
        data.incline.push(document.getElementById(`incline_${i}`).innerText)
        data.bending.push(document.getElementById(`bending_${i}`).innerText)
        data.raising.push(document.getElementById(`raising_${i}`).innerText)
        data.pull_up.push(document.getElementById(`pull_up_${i}`).innerText)
        data.squat.push(document.getElementById(`squat_${i}`).innerText)
    }
     fetch(`${URL}/physicals_table/`, {
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

function edit_health(id) {
    data = {
        sleep: [],
        health: [],
        appetite: [],
        pain: [],
        overload: [],
        perfomance: [],
        loads_attitude: [],
        health_result: []
    }
    for (let i = 1; i < 33; i++) {
        data.sleep.push(document.getElementById(`sleep_${i}`).innerText)
        data.health.push(document.getElementById(`health_${i}`).innerText)
        data.appetite.push(document.getElementById(`appetite_${i}`).innerText)
        data.pain.push(document.getElementById(`pain_${i}`).innerText)
        data.overload.push(document.getElementById(`overload_${i}`).innerText)
        data.perfomance.push(document.getElementById(`perfomance_${i}`).innerText)
        data.loads_attitude.push(document.getElementById(`loads_attitude_${i}`).innerText)
        data.health_result.push(document.getElementById(`healthresult_${i}`).innerText)
    }
     fetch(`${URL}/health/`, {
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
        if (document.getElementById(`shtange_${i}`).innerText) {
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
        if (document.getElementById(`functional_ccc_${i}`).innerText) {
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
        if (document.getElementById(`orthostatic_${i}`).innerText) {
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


function colorize_index_table(gender) {
    for (let i = 1; i < 9; i++) {
        if (document.getElementById(`height_idx_${i}`).innerText) {
            element = document.getElementById(`height_idx_${i}`)
            amount = Number(element.innerText)

            if (gender == "male") {
                if (amount >= 350 && amount <= 400) element.style.backgroundColor = "green"
                else element.style.backgroundColor = "red"
            }
            if (gender == "wooman") {
                if (amount >= 325 && amount <= 375) element.style.backgroundColor = "green"
                else element.style.backgroundColor = "red"
            }
        }
       if (document.getElementById(`life_${i}`).innerText) {
            element = document.getElementById(`life_${i}`)
            amount = Number(element.innerText)

            if (gender == "male") {
                if (amount >= 65 && amount <= 70) {
                    element.style.backgroundColor = "green"
                }
                else {
                    element.style.backgroundColor = "red"
                }
            }
            if (gender == "wooman") {
                if (amount >= 55 && amount <= 60) element.style.backgroundColor = "green"
                else element.style.backgroundColor = "red"
            }
        }
        if (document.getElementById(`strength_idx_${i}`).innerText) {
            element = document.getElementById(`strength_idx_${i}`)
            amount = Number(element.innerText)

            if (gender == "male") {
                if (amount >= 70 && amount <= 75) element.style.backgroundColor = "green"
                else element.style.backgroundColor = "red"
            }
            if (gender == "wooman") {
                if (amount >= 50 && amount <= 60) element.style.backgroundColor = "green"
                else element.style.backgroundColor = "red"
            }
        }
        if (document.getElementById(`stan_${i}`).innerText) {
            element = document.getElementById(`stan_${i}`)
            amount = Number(element.innerText)

            if (gender == "male") {
                if (amount >= 200 && amount <= 220) element.style.backgroundColor = "green"
                else element.style.backgroundColor = "red"
            }
            if (gender == "wooman") {
                if (amount >= 135 && amount <= 150) element.style.backgroundColor = "green"
                else element.style.backgroundColor = "red"
            }
        }
    }
}

