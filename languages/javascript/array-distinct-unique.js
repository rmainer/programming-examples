// classic JS
const unique = (value, index, self) => {
	return self.indexOf(value) === index;
}

const a = [1,2,3,4,3,2,5,8,6,2,1,8,4];
const u = a.filter(unique);
console.log("Method 1: "+u);

// Since ES6, using spread operator and Set()
const v = [...new Set(a)];
console.log("Method 2: "+v);
