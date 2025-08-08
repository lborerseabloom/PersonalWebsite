// HTML elements
const main = document.getElementById("page");
const switcher = document.getElementById("themeButton");

// Function to store theme
const storeTheme = (theme) => {
  try {
    localStorage.setItem("theme", theme);
  } catch (e) {
    console.error("Could not store theme:", e);
  }
};

// Function to change theme
const changeTheme = (theme) => {
  if (theme === "dark") {
    main.classList.add("dark");
  } else {
    main.classList.remove("dark");
  }
};

// Load theme on page load
window.addEventListener("DOMContentLoaded", () => {
  const storedTheme = localStorage.getItem("theme") || "light";
  changeTheme(storedTheme);
});

// Handle click event on theme toggle
switcher.addEventListener("click", () => {
  const isDark = main.classList.contains("dark");
  const newTheme = isDark ? "light" : "dark";

  changeTheme(newTheme);
  storeTheme(newTheme);

  if (switcher._tippy) {
    switcher._tippy.setContent(isDark ? "Dark theme" : "Light theme");
  }
});