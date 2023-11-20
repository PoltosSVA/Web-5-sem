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

function Film(title, cost, author, duration) {
  this._title = title;
  this._cost = cost;
  this._author = author;
  this._duration = duration;
}

Film.prototype = {
  get title() {
    return this._title;
  },

  set title(newTitle) {
    this._title = newTitle;
  },

  get cost() {
    return this._cost;
  },

  set cost(newCost) {
    if (newCost > 0) {
      this._cost = newCost;
    } else {
      alert("Invalid cost format");
    }
  },

  get author() {
    return this._author;
  },

  set author(newAuthor) {
    this._author = newAuthor;
  },

  get duration() {
    return this._duration;
  },

  set duration(newDuration) {
    if (newDuration > 0) {
      this._duration = newDuration;
    } else {
      alert("Invalid duration format");
    }
  },

  updateCost: function (newCost) {
    this.cost = newCost;  // Исправлено на this.cost
    alert('Cost updated: ' + this._cost);
  },

  getFilmInfo: function () {
    return "Title: " + this._title +
      "\nCost: " + this._cost +
      "\nAuthor: " + this._author +
      "\nDuration: " + this._duration;
  },
  checkYears: function () {
    return 18;
  }
};

Film.prototype.checkYears = checkAge(Film.prototype.checkYears);

function Tusk(title, cost, author, duration, years) {
  Film.call(this, title, cost, author, duration);
  this._years = years;
}

Tusk.prototype = Object.create(Film.prototype);

Tusk.prototype.getYearsContent = function () {
  return this._years;
};

Tusk.prototype.setYearsContent = function (newYearsContent) {
  if (newYearsContent >= 13 && newYearsContent <= 100) {
    this._years = newYearsContent;
  } else {
    alert("Invalid year content value.");
  }
};

Tusk.prototype.checkOld = checkAge(function () {
  return this._years; // Пусть 18 будет возрастным ограничением по умолчанию
});

Tusk.prototype.getTuskInfo = function () {
  return this.getFilmInfo() + "\nYears: " + this._years;
};

const tusk = new Tusk("Tusk", 9.99, "Christopher Nolan", 120, 24);

tusk.updateCost(12.00);
tusk.title = "Tusks";
tusk.duration = 160;

alert(tusk.getTuskInfo());

const userAge = prompt("Enter your age:");
tusk.checkOld(userAge);
