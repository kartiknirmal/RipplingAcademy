let btnArr = Array.from(document.querySelectorAll(".btn"));
// console.log(btnArr);

let mainText = "";
let prevText = "";

let ce = true;

let ceObj = document.getElementById("CE");

let mainInput = document.querySelector(".input");
let prevInput = document.querySelector(".prev-input");

btnArr.forEach(e =>{
    // console.log(e.innerHTML);
    e.addEventListener('click', f =>{
        // console.log(f.target.innerHTML);
        let k = f.target.innerHTML;
        // console.log(k);
        if(k == "="){
            prevText = mainText + "=";
            try {
                mainText = (eval(mainText)).toString();
            } catch (error) {
                mainText = "Invalid Input!!!";
            }
            ce = true;
            ceObj.innerHTML = "AC";
        }
        else if(k == "CE"){
            if(mainText != ""){
                mainText = mainText.slice(0, -1);
                if(mainText == ""){
                    ceObj.innerHTML = "AC";
                    ce = true;
                }
            }
        }
        else if(k == "AC"){
            prevText = "Ans = " + mainText;
            mainText = "";
        }
        else{
            mainText = mainText + k;
            ce = false;
            ceObj.innerHTML = "CE";
            // console.log(mainText);
        }
        mainInput.value = mainText;
        prevInput.value = prevText;
    });
});