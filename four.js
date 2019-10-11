/*
var contacts = [{
    firstName: 'John',
    lastName: 'Doe',
    phone: '(512) 355-0453',
    email: 'johndoe@email.com'
  }, {
    firstName: 'Jane',
    lastName: 'Doe',
    phone: '(313) 641-2203',
    email: 'janedoe@email.com'
  }, {
    firstName: 'Suzie',
    lastName: 'Smith',
    phone: '(415) 604-4219',
    email: 'suziesmith@email.com'
  }];
  
  var listContacts = function() {
    return contacts.map(function(contact) {
      return contact.firstName + " " + contact.lastName
    })
  };
  
  console.log(listContacts());


------------------------------

export const menuDinner = [{
    "steak": "$12.00",
    "fish": "$15.00",
    "burger": "$8.50"
}];

export const menuBreakfast = [
    {"waffles": "$2.00"},
    {"sandwich": "$3.00"},
    {"bagels": "$1.50"}
];

export const sideDishes = [
    {"fries": "$2.25"},
    {"pita Chips": "$3.25"},
    {"guacamole": "$3.75"}
];

---------------------------------------

import { menuDinner,menuBreakfast,sideDishes } from './two.js'

const iterationMenu = theMenu => {
    theMenu.forEach(food => {
        for (var key in food) {
        return (`${key} cost ${food[key]}`) //?
        }
    })
}

const selectingMenu = (selection) => {
    if (selection === 'dinner' ) {
        return Object.values(menuDinner) 
    } else if ( selection === 'sides') {
        return Object.values(sideDishes) 
    } else if ( selection === 'breakfast') {
        return Object.values (menuBreakfast) 
    } else {
        return ("Makes a selection from the menu please")
    }
}

const itemSelection = (menuItems, food) => {
    for (let i in menuItems) {
        for (let key in menuItems[i]) { 
            if (key ===  food) {
                return (`${key} cost ${Object.values(menuItems[i])}`) //? 
            } else {
                return ("Please select an item")
            }
        }
    }
}

iterationMenu(sideDishes)
iterationMenu(menuDinner)
iterationMenu(menuBreakfast)

const dinner = selectingMenu('dinner') //?
const sides = selectingMenu('sides') //?
const breakfast = selectingMenu('breakfast') //?

itemSelection (dinner,"steak")//?
itemSelection (dinner,"burger") //?
itemSelection (dinner,"fish") //?




*/

