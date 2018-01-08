var d6 = {
  sides: 6,
  roll: function () {
    var randomNumber = Math.floor(Math.random() * this.sides) + 1;
    return randomNumber;
  }
}
var d4 = {
  sides: 4,
  roll: function () {
    var randomNumber = Math.floor(Math.random() * this.sides) + 1;
    return randomNumber;
  }
}
var d8 = {
  sides: 8,
  roll: function () {
    var randomNumber = Math.floor(Math.random() * this.sides) + 1;
    return randomNumber;
  }
}
var d10 = {
  sides: 10,
  roll: function () {
    var randomNumber = Math.floor(Math.random() * this.sides) + 1;
    return randomNumber;
  }
}
var d12 = {
  sides: 12,
  roll: function () {
    var randomNumber = Math.floor(Math.random() * this.sides) + 1;
    return randomNumber;
  }
}
var d20 = {
  sides: 20,
  roll: function () {
    var randomNumber = Math.floor(Math.random() * this.sides) + 1;
    return randomNumber;
  }
}
//Prints dice roll to the page

function printNumber(number) {
  var placeholder = document.getElementById('roll');
  placeholder.innerHTML = number;
}

var b6 = document.getElementById('d6_button');
var b4 = document.getElementById('d4_button');
var b8 = document.getElementById('d8_button');
var b10 = document.getElementById('d10_button');
var b12 = document.getElementById('d12_button');
var b20 = document.getElementById('d20_button');

b6.onclick = function() {
  var result = d6.roll();
  printNumber(result);
};
b4.onclick = function() {
  var result = d4.roll();
  printNumber(result);
};
b8.onclick = function() {
  var result = d8.roll();
  printNumber(result);
};
b10.onclick = function() {
  var result = d10.roll();
  printNumber(result);
};
b12.onclick = function() {
  var result = d12.roll();
  printNumber(result);
};
b20.onclick = function() {
  var result = d20.roll();
  printNumber(result);
};
