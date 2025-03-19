console.log("---Registro de Personas---")

let personas = []

console.log("///Ingrese los siguientes datos///")
console.log("si desea terminar escriba 'finalizar' en el campo nombre")
while (true){
    let nombre = prompt("Nombre: ")
    if(nombre == "finalizar") {break;}
   
    let edad = prompt("Edad: ")
   
    let nota = prompt("Nota: ")
    personas.push({ nombre: nombre, edad: edad, nota: parseFloat(nota) });
};

console.log("Lista de Personas: ", personas);

personas.sort((a, b) => b.nota - a.nota);


console.log("Lista por Notas (de mayor a menor):");
console.log(personas);
