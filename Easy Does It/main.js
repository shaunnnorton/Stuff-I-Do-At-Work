
// Grab Elements for discount calculations. 
op_input = document.getElementById("op_input")
dp_input = document.getElementById("dp_input")
dc_button = document.getElementById("dc_button")
dc_title = document.getElementById("dc_title")
// Perform discount calculations
let calculate_discount = () => {
    if(op_input.value == 0){
        return(NaN)
    }
    let discount_percentage =  100*(1-(dp_input.value/op_input.value))
    console.log(discount_percentage.toFixed(2))
    return(discount_percentage.toFixed(2))
}
dc_button.addEventListener("click", ()=>{
    let discount = calculate_discount()
    dc_title.innerHTML = "Discount Calculated: " + discount + "%"
})