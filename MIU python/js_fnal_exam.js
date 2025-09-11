// fizz buzz problem

for (let i = 1; i <= 20; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}


// Document Object Model (DOM)

// Definition:
// The DOM is a programming interface for web documents. It represents the entire HTML page as a tree of objects.
// প্রতিটি HTML element (tag) কে DOM একটি “object” হিসেবে ধরে, আর সব element গুলো মিলে একটা গাছের (tree) মতো স্ট্রাকচার তৈরি করে।


Summary of Manipulating & Creating Elements in the DOM

innerHTML → Reads or changes an element’s HTML content (can include tags).

textContent → Reads or changes only the plain text of an element (no tags).

element.style → Changes inline CSS styles of an element (e.g., color, fontSize).

setAttribute() / getAttribute() → Set or read any attribute of an element (e.g., src, alt, href).

createElement() → Creates a new HTML element in memory.

appendChild() → Adds (appends) a created element as a child of another element in the DOM.

removeChild() → Removes an existing child element from its parent.