// Keeps the homepage hero stat strip in sync with the site's own data files
// (software.json for apps/systems/recipes/smoke tests, campaigns.json for the
// campaign count). The numbers committed in index.md remain as the no-JS and
// fetch-failure fallback, so this can only make the strip MORE accurate.
(function () {
  "use strict";
  var SCRIPT_SRC = (document.currentScript && document.currentScript.src) || "";
  function dataUrl(rel) {
    return SCRIPT_SRC ? new URL(rel, SCRIPT_SRC).href : rel;
  }

  function set(key, value) {
    var node = document.querySelector('.tx-stat__n[data-stat="' + key + '"]');
    if (node && value != null) node.textContent = value;
  }

  function init() {
    if (!document.querySelector(".tx-stats")) return;  // homepage only

    fetch(dataUrl("../software/software.json"))
      .then(function (r) { return r.json(); })
      .then(function (d) {
        var recipes = d.apps.reduce(function (n, a) {
          return n + Object.keys(a.systems || {}).length;
        }, 0);
        var pass = d.smokes.filter(function (s) { return s.state === "pass"; }).length;
        set("apps", d.apps.length);
        set("systems", d.systems.length);
        set("recipes", recipes);
        set("smoke", pass + "/" + d.smokes.length);
      })
      .catch(function () { /* keep the committed fallback numbers */ });

    fetch(dataUrl("../campaigns/campaigns.json"))
      .then(function (r) { return r.json(); })
      .then(function (d) { set("campaigns", d.campaigns.length); })
      .catch(function () { /* keep the committed fallback numbers */ });
  }

  // document$ fires on initial load AND after every instant-navigation.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
