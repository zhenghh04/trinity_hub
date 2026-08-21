// Renders the metadata line on campaign pages ("**System:** Polaris · **Outcome:** …")
// as styled chips, with the outcome color-coded. Presentation only — the markdown
// source stays a plain, readable key/value line.
(function () {
  "use strict";

  // Outcome → chip color class; keep in sync with scripts/build_campaign_index.py.
  function classify(text) {
    var o = text.toLowerCase();
    if (/negative|fail|blocked/.test(o)) return "blocked";
    if (/partial|mixed/.test(o)) return "in_progress";
    if (/ongoing|phase|in progress/.test(o)) return "available";
    if (/success|completed|verified|reproduced|confirmed/.test(o)) return "pass";
    return "";
  }

  function isKey(node) {
    return node.nodeType === 1 && node.tagName === "STRONG" &&
      /:\s*$/.test(node.textContent);
  }

  function enhance() {
    // Campaign pages only (not the /campaigns/ overview or category indexes).
    if (!/\/campaigns\/[^/]+\/[^/]+/.test(location.pathname)) return;
    var p = document.querySelector(".md-typeset h1 + p");
    if (!p || p.dataset.txMeta || !p.querySelector("strong")) return;
    if (!isKey(p.querySelector("strong"))) return;  // must START with a **Key:**

    // Split child nodes into {key, valueNodes[]} items. A new item begins at each
    // **Key:**; a "·" inside a text node also terminates the current item.
    var items = [], current = null;
    Array.prototype.slice.call(p.childNodes).forEach(function (node) {
      if (isKey(node)) {
        current = { key: node.textContent.replace(/:\s*$/, ""), nodes: [] };
        items.push(current);
        return;
      }
      if (!current) return;
      if (node.nodeType === 3 && node.nodeValue.indexOf("·") !== -1) {
        var head = node.nodeValue.split("·")[0];
        if (head.trim()) current.nodes.push(document.createTextNode(head.trim()));
        current = null;  // rest (usually whitespace before the next key) is dropped
        return;
      }
      current.nodes.push(node);
    });
    if (items.length < 2) return;  // not a metadata line

    var wrap = document.createElement("div");
    wrap.className = "tx-meta";
    items.forEach(function (item) {
      var chip = document.createElement("span");
      chip.className = "tx-meta__item";
      var valueText = item.nodes.map(function (n) { return n.textContent; }).join("");
      if (/^(outcome|status|result)$/i.test(item.key)) {
        var cls = classify(valueText);
        if (cls) chip.className += " tx-meta__item--" + cls;
      }
      if (valueText.length > 70) chip.className += " tx-meta__item--wide";
      var k = document.createElement("span");
      k.className = "tx-meta__key";
      k.textContent = item.key;
      var v = document.createElement("span");
      v.className = "tx-meta__val";
      item.nodes.forEach(function (n) {
        // Trim leading whitespace-only text nodes so chips hug their content.
        if (n.nodeType === 3) n.nodeValue = n.nodeValue.replace(/\s+/g, " ").trim() ? n.nodeValue.replace(/\s+/g, " ") : "";
        v.appendChild(n);
      });
      chip.appendChild(k);
      chip.appendChild(v);
      wrap.appendChild(chip);
    });

    p.dataset.txMeta = "1";
    p.replaceChildren(wrap);
    p.classList.add("tx-meta-host");
  }

  // document$ fires on initial load AND after every instant-navigation.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(enhance);
  } else if (document.readyState !== "loading") {
    enhance();
  } else {
    document.addEventListener("DOMContentLoaded", enhance);
  }
})();
