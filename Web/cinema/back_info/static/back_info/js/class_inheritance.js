function checkAge(func) {
  return function (age, ...args) {
    if (age < 0) {
      alert("Invalid age value.");
      return;
    }

    const result = func.apply(this, args);
    if (age < result) {
      alert("This content is not suitable for your age.");
    } else {
      return result;
    }
  };
}

class Film {
  constructor(title, cost, author, duration) {
    this._title = title;
    this._cost = cost;
    this._author = author;
    this._duration = duration;
  }

  get title() {
    return this._title;
  }

  set title(newTitle) {
    this._title = newTitle;
  }

  get cost() {
    return this._cost;
  }

  set cost(newCost) {
    if (newCost > 0) {
      this._cost = newCost;
    } else {
      alert("Invalid cost format");
    }
  }

  get author() {
    return this._author;
  }

  set author(newAuthor) {
    this._author = newAuthor;
  }

  get duration() {
    return this._duration;
  }

  set duration(newDuration) {
    if (newDuration > 0) {
      this._duration = newDuration;
    } else {
      alert("Invalid duration format");
    }
  }

  updateCost(newCost) {
    this.cost = newCost;
    alert('Cost updated: ' + this._cost);
  }

  getFilmInfo() {
    return "Title: " + this._title +
      "\nCost: " + this._cost +
      "\nAuthor: " + this._author +
      "\nDuration: " + this._duration;
  }

  checkYears() {
    return 18;
  }
}

Film.prototype.checkYears = checkAge(Film.prototype.checkYears);

class Tusk extends Film {
  constructor(title, cost, author, duration, years) {
    super(title, cost, author, duration);
    this._years = years;
  }

  get years() {
    return this._years;
  }

  set years(newYears) {
    if (newYears >= 13 && newYears <= 100) {
      this._years = newYears;
    } else {
      alert("Invalid year content value.");
    }
  }

  checkOld(age) {
    return this.checkYears(age);
  }

  getTuskInfo() {
    return super.getFilmInfo() + "\nYears: " + this._years;
  }
}

const tusk = new Tusk("Tusk", 9.99, "Christopher Nolan", 120, 24);

tusk.updateCost(12.00);
tusk.title = "Tusks";
tusk.duration = 160;

alert(tusk.getTuskInfo());

const userAge = prompt("Enter your age:");
tusk.checkOld(userAge);
