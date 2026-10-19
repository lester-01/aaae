(function () {
  var page = encodeURIComponent(location.origin + location.pathname);
  var text = encodeURIComponent("Jasiri for Android: A pocket computer, with an integrated AI assistant.");

  var nets = {
    linkedin: "https://www.linkedin.com/sharing/share-offsite/?url=" + page,
    x: "https://twitter.com/intent/tweet?url=" + page + "&text=" + text,
    whatsapp: "https://wa.me/?text=" + text + "%20" + page,
    reddit: "https://www.reddit.com/submit?url=" + page + "&title=" + text
  };

  document.querySelectorAll("[data-share]").forEach(function (box) {
    box.querySelectorAll("[data-net]").forEach(function (a) {
      a.href = nets[a.getAttribute("data-net")];
    });
    var copy = box.querySelector("[data-copy]");
    if (!copy) return;
    if (navigator.share) {
      var native = document.createElement("button");
      native.type = "button";
      native.textContent = "Share\u2026";
      native.addEventListener("click", function () {
        navigator.share({ title: document.title, url: location.origin + location.pathname }).catch(function () {});
      });
      box.insertBefore(native, box.querySelector("[data-net]"));
    }
    copy.addEventListener("click", function () {
      var url = location.origin + location.pathname;
      var done = function () {
        copy.textContent = "Copied";
        setTimeout(function () { copy.textContent = "Copy link"; }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(done, done);
      } else {
        done();
      }
    });
  });

  var menu = document.querySelector(".menu");
  var nav = document.getElementById("site-nav");
  if (menu && nav) {
    var setOpen = function (open) {
      nav.classList.toggle("is-open", open);
      menu.setAttribute("aria-expanded", open ? "true" : "false");
      menu.textContent = open ? "Close" : "Menu";
    };
    menu.addEventListener("click", function () {
      setOpen(!nav.classList.contains("is-open"));
    });
    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && nav.classList.contains("is-open")) {
        setOpen(false);
        menu.focus();
      }
    });
  }

})();
