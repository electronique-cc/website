const menuToggle = document.querySelector(".menu-toggle");
const navList = document.querySelector(".nav-list");

menuToggle.addEventListener("click", function () {
  menuToggle.classList.toggle("active");
  navList.classList.toggle("active");
});

document.addEventListener("click", function (event) {
  if (!event.target.closest("header")) {
    menuToggle.classList.remove("active");
    navList.classList.remove("active");
  }
});

// Get all elements with class "language-switcher"
const languageSwitchers = document.querySelectorAll(".language-switcher");

// Check if a language preference is stored in local storage
let language = localStorage.getItem("language");

// If no language preference is stored, try to infer the language from the URL
if (!language) {
  const urlLanguage = window.location.href.includes("/fr/") ? "fr" : "en";
  localStorage.setItem("language", urlLanguage);
  language = urlLanguage;
}

// Add click event listener to each language switcher element
languageSwitchers.forEach((switcher) => {
  switcher.addEventListener("click", () => {
    // Determine the current language and the new language to switch to
    const currentLanguage = localStorage.getItem("language");
    const newLanguage = currentLanguage === "en" ? "fr" : "en";

    // Replace the language code in the URL with the new language
    const currentUrl = window.location.href;
    const newUrl = currentUrl.replace(
      `/${currentLanguage}/`,
      `/${newLanguage}/`
    );
    localStorage.setItem("language", newLanguage);

    // Redirect the user to the new URL
    window.location.href = newUrl;
  });
});
