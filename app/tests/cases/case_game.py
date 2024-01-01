# flake8: noqa
# pylint: skip-file

GAME_PAGE = """<!DOCTYPE html>
<html data-version="klecko-" data-root="/home/pfr/build" lang="en" class="no-js">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0"/>
        <link rel="dns-prefetch" href="https://cdn.ssref.net/req/202311303"/>
        <!-- Quantcast Choice. Consent Manager Tag v2.0 (for TCF 2.0) -->
        <script type="text/javascript" async=true>
            (function() {
                var host = window.location.hostname;
                var element = document.createElement('script');
                var firstScript = document.getElementsByTagName('script')[0];
                var url = 'https://cmp.quantcast.com'.concat('/choice/', 'XwNYEpNeFfhfr', '/', host, '/choice.js?tag_version=V2');
                var uspTries = 0;
                var uspTriesLimit = 3;
                element.async = true;
                element.type = 'text/javascript';
                element.src = url;

                firstScript.parentNode.insertBefore(element, firstScript);

                function makeStub() {
                    var TCF_LOCATOR_NAME = '__tcfapiLocator';
                    var queue = [];
                    var win = window;
                    var cmpFrame;

                    function addFrame() {
                        var doc = win.document;
                        var otherCMP = !!(win.frames[TCF_LOCATOR_NAME]);

                        if (!otherCMP) {
                            if (doc.body) {
                                var iframe = doc.createElement('iframe');

                                iframe.style.cssText = 'display:none';
                                iframe.name = TCF_LOCATOR_NAME;
                                doc.body.appendChild(iframe);
                            } else {
                                setTimeout(addFrame, 5);
                            }
                        }
                        return !otherCMP;
                    }

                    function tcfAPIHandler() {
                        var gdprApplies;
                        var args = arguments;

                        if (!args.length) {
                            return queue;
                        } else if (args[0] === 'setGdprApplies') {
                            if (args.length > 3 && args[2] === 2 && typeof args[3] === 'boolean') {
                                gdprApplies = args[3];
                                if (typeof args[2] === 'function') {
                                    args[2]('set', true);
                                }
                            }
                        } else if (args[0] === 'ping') {
                            var retr = {
                                gdprApplies: gdprApplies,
                                cmpLoaded: false,
                                cmpStatus: 'stub'
                            };

                            if (typeof args[2] === 'function') {
                                args[2](retr);
                            }
                        } else {
                            if (args[0] === 'init' && typeof args[3] === 'object') {
                                args[3] = Object.assign(args[3], {
                                    tag_version: 'V2'
                                });
                            }
                            queue.push(args);
                        }
                    }

                    function postMessageEventHandler(event) {
                        var msgIsString = typeof event.data === 'string';
                        var json = {};

                        try {
                            if (msgIsString) {
                                json = JSON.parse(event.data);
                            } else {
                                json = event.data;
                            }
                        } catch (ignore) {}

                        var payload = json.__tcfapiCall;

                        if (payload) {
                            window.__tcfapi(payload.command, payload.version, function(retValue, success) {
                                var returnMsg = {
                                    __tcfapiReturn: {
                                        returnValue: retValue,
                                        success: success,
                                        callId: payload.callId
                                    }
                                };
                                if (msgIsString) {
                                    returnMsg = JSON.stringify(returnMsg);
                                }
                                if (event && event.source && event.source.postMessage) {
                                    event.source.postMessage(returnMsg, '*');
                                }
                            }, payload.parameter);
                        }
                    }

                    while (win) {
                        try {
                            if (win.frames[TCF_LOCATOR_NAME]) {
                                cmpFrame = win;
                                break;
                            }
                        } catch (ignore) {}

                        if (win === window.top) {
                            break;
                        }
                        win = win.parent;
                    }
                    if (!cmpFrame) {
                        addFrame();
                        win.__tcfapi = tcfAPIHandler;
                        win.addEventListener('message', postMessageEventHandler, false);
                    }
                }
                ;
                makeStub();

                var uspStubFunction = function() {
                    var arg = arguments;
                    if (typeof window.__uspapi !== uspStubFunction) {
                        setTimeout(function() {
                            if (typeof window.__uspapi !== 'undefined') {
                                window.__uspapi.apply(window.__uspapi, arg);
                            }
                        }, 500);
                    }
                };

                var checkIfUspIsReady = function() {
                    uspTries++;
                    if (window.__uspapi === uspStubFunction && uspTries < uspTriesLimit) {
                        console.warn('USP is not accessible');
                    } else {
                        clearInterval(uspInterval);
                    }
                };

                if (typeof window.__uspapi === 'undefined') {
                    window.__uspapi = uspStubFunction;
                    var uspInterval = setInterval(checkIfUspIsReady, 6000);
                }
            }
            )();
        </script>
        <!-- End Quantcast Choice. Consent Manager Tag v2.0 (for TCF 2.0) -->
        <title>Denver Broncos at Detroit Lions - December 16th, 2023 | Pro-Football-Reference.com</title>
        <meta name="Description" content="Denver Broncos 17 at Detroit Lions 42 on December 16th, 2023  - Full team and player stats and box score">
        <link rel="canonical" href="https://www.pro-football-reference.com/boxscores/202312160det.htm"/>
        <!-- include:start  ="/inc/klecko_header_full_pfr.html_f" -->
        <!-- yes:cookie regular load the cached css -->
        <script>
            function gup(n) {
                n = n.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
                var r = new RegExp('[\\?&]' + n + '=([^&#]*)');
                var re = r.exec(location.search);
                return re === null ? '' : decodeURIComponent(re[1].replace(/\+/g, ' '));
            }
            ;document.srdev = gup('srdev')
        </script>
        <script>
            if (!document.srdev && (location.hostname === 'sup.fb.srdevel.com')) {
                document.srdev = 'aw';
            }
            /* sf: hardcode this in for sup.fb.srdevel.com for testing purposes. */
        </script>
        <link rel="preconnect" href="https://cdn.ssref.net" crossorigin>
        <link rel="preconnect" href="https://www.google-analytics.com" crossorigin>
        <link rel="preconnect" href="https://www.googletagservices.com" crossorigin>
        <link rel="preload" href="https://cdn.ssref.net/req/202311303/js/pfr/sr-min.js" as="script" crossorigin>
        <link rel="preload" href="https://cdn.ssref.net/req/202311303/icons/sr_icons-min.svg?pfr" as="fetch" crossorigin>
        <link rel="preload" href="https://www.pro-football-reference.com/short/inc/main_nav_menu.json" as="fetch" crossorigin>
        <link rel="preload" href="https://cdn.ssref.net/req/201604190/images/chosen-sprite.png" as="image" crossorigin>
        <link rel="preload" href="https://cdn.ssref.net/req/202311303/css/pfr/sr-min.css" as="style" crossorigin>
        <!-- CSS start -->
        <link rel="stylesheet" href="https://cdn.ssref.net/req/202311303/css/pfr/sr-min.css" type="text/css" onload="if (document.srdev) { this.href = 'https://cdn.ssref.net/nocdn/dev/'.concat(document.srdev.substr(0,2),'/css/pfr/sr.css'); }"/>
        <!-- CSS END -->
        <!-- JS START -->
        <script class="allowed">
            var sr_is_production = true;
            function vjs_getUrlParameter(e) {
                e = e.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
                e = new RegExp("[\\?&]" + e + "=([^&#]*)").exec(location.search);
                return null === e ? "" : decodeURIComponent(e[1].replace(/\+/g, " "))
            }
            document.lang = "",
            "/es/" === window.location.pathname.substr(0, 4) ? document.lang = "es" : "/pt/" === window.location.pathname.substr(0, 4) ? document.lang = "pt" : "/fr/" === window.location.pathname.substr(0, 4) ? document.lang = "fr" : "/it/" === window.location.pathname.substr(0, 4) ? document.lang = "it" : "/de/" === window.location.pathname.substr(0, 4) ? document.lang = "de" : (window.location.pathname.substr(0, 4),
            document.lang = "en"),
            vjs_getUrlParameter("lang") && (document.lang = vjs_getUrlParameter("lang")),
            document.srdev = null,
            vjs_getUrlParameter("srdev") ? document.srdev = vjs_getUrlParameter("srdev") : "sup" === window.location.host.substr(0, 3) && (document.srdev = "aw");
            var el, log_performance = !0, is_new_jscss_version = !1, sr_detect_operaMini = -1 < navigator.userAgent.indexOf("Opera Mini"), sr_detect_firefox = (sr_detect_operaMini && ((el = document.querySelector("html")).className = el.className.concat(" operamini")),
            -1 < navigator.userAgent.indexOf("Firefox")), sr_detect_firefoxMobile = (sr_detect_firefox && ((el = document.querySelector("html")).className = el.className.concat(" firefox")),
            -1 < navigator.userAgent.indexOf("Firefox") && (-1 < navigator.userAgent.indexOf("Mobile") || -1 < navigator.userAgent.indexOf("Tablet"))), sr_detect_ie = (sr_detect_firefoxMobile && ((el = document.querySelector("html")).className = el.className.concat(" firefox-mobile")),
            function() {
                var e = window.navigator.userAgent;
                if (0 < e.indexOf("Trident/7.0"))
                    return 11;
                if (0 < e.indexOf("Trident/6.0"))
                    return 10;
                if (0 < e.indexOf("Trident/5.0"))
                    return 9;
                for (var t = 3, n = document.createElement("div"), r = n.getElementsByTagName("i"); n.innerHTML = "\x3c!--[if gt IE " + ++t + "]><i></i><![endif]--\x3e",
                r[0]; )
                    ;
                return 4 < t && t
            }()), sr_detect_edge = !sr_detect_ie && !!window.StyleMedia, sr_detect_safari = /Safari/.test(navigator.userAgent) && /Apple Computer/.test(navigator.vendor), className = "no-js", patt = ((el = document.querySelector("html")).classList ? el.classList.remove(className) : el.className = el.className.replace(new RegExp("(^|\\b)" + className.split(" ").join("|") + "(\\b|$)","gi"), " "),
            el.className = el.className.concat(" js"),
            !function(s, d, S) {
                function E(e, t) {
                    return typeof e === t
                }
                function T(e) {
                    return "function" != typeof d.createElement ? d.createElement(e) : m ? d.createElementNS.call(d, "http://www.w3.org/2000/svg", e) : d.createElement.apply(d, arguments)
                }
                function R(e, t, n, r) {
                    var o, i, s, a, l = "modernizr", c = T("div");
                    (a = d.body) || ((a = T(m ? "svg" : "body")).fake = !0);
                    if (parseInt(n, 10))
                        for (; n--; )
                            (i = T("div")).id = r ? r[n] : l + (n + 1),
                            c.appendChild(i);
                    return (o = T("style")).type = "text/css",
                    o.id = "s" + l,
                    (a.fake ? a : c).appendChild(o),
                    a.appendChild(c),
                    o.styleSheet ? o.styleSheet.cssText = e : o.appendChild(d.createTextNode(e)),
                    c.id = l,
                    a.fake && (a.style.background = "",
                    a.style.overflow = "hidden",
                    s = u.style.overflow,
                    u.style.overflow = "hidden",
                    u.appendChild(a)),
                    o = t(c, e),
                    a.fake ? (a.parentNode.removeChild(a),
                    u.style.overflow = s,
                    u.offsetHeight) : c.parentNode.removeChild(c),
                    !!o
                }
                function U(e) {
                    return e.replace(/([a-z])-([a-z])/g, function(e, t, n) {
                        return t + n.toUpperCase()
                    }).replace(/^-/, "")
                }
                function D(e) {
                    return e.replace(/([A-Z])/g, function(e, t) {
                        return "-" + t.toLowerCase()
                    }).replace(/^ms-/, "-ms-")
                }
                function q(e, t) {
                    var n = e.length;
                    if ("CSS"in s && "supports"in s.CSS) {
                        for (; n--; )
                            if (s.CSS.supports(D(e[n]), t))
                                return !0;
                        return !1
                    }
                    if ("CSSSupportsRule"in s) {
                        for (var r = []; n--; )
                            r.push("(" + D(e[n]) + ":" + t + ")");
                        return R("@supports (" + (r = r.join(" or ")) + ") { #modernizr { position: absolute; } }", function(e) {
                            return "absolute" == (e = e,
                            t = null,
                            n = "position",
                            "getComputedStyle"in s ? (r = getComputedStyle.call(s, e, t),
                            o = s.console,
                            null !== r ? n && (r = r.getPropertyValue(n)) : o && o[o.error ? "error" : "log"].call(o, "getComputedStyle returning null, its possible modernizr test results are inaccurate")) : r = !t && e.currentStyle && e.currentStyle[n],
                            r);
                            var t, n, r, o
                        })
                    }
                    return S
                }
                function r(e, t, n, r, o) {
                    var i, s, a = e.charAt(0).toUpperCase() + e.slice(1), l = (e + " " + re.join(a + " ") + a).split(" ");
                    if (E(t, "string") || void 0 === t) {
                        var c = l
                          , d = t
                          , u = r
                          , m = o;
                        function f() {
                            p && (delete L.style,
                            delete L.modElem)
                        }
                        if (m = void 0 !== m && m,
                        void 0 !== u) {
                            l = q(c, u);
                            if (void 0 !== l)
                                return l
                        }
                        for (var p, h, g, v, _, w = ["modernizr", "tspan", "samp"]; !L.style && w.length; )
                            p = !0,
                            L.modElem = T(w.shift()),
                            L.style = L.modElem.style;
                        for (g = c.length,
                        h = 0; h < g; h++)
                            if (v = c[h],
                            _ = L.style[v],
                            ~("" + v).indexOf("-") && (v = U(v)),
                            L.style[v] !== S) {
                                if (m || void 0 === u)
                                    return f(),
                                    "pfx" != d || v;
                                try {
                                    L.style[v] = u
                                } catch (e) {}
                                if (L.style[v] != _)
                                    return f(),
                                    "pfx" != d || v
                            }
                        f()
                    } else {
                        var y = (e + " " + P.join(a + " ") + a).split(" ")
                          , b = t
                          , x = n;
                        for (s in y)
                            if (y[s]in b)
                                if (!1 === x)
                                    return y[s];
                                else {
                                    i = b[y[s]];
                                    if (E(i, "function")) {
                                        var M = i;
                                        var z = x || b;
                                        return function() {
                                            return M.apply(z, arguments)
                                        }
                                        ;
                                        return
                                    } else
                                        return i
                                }
                    }
                    return !1
                }
                function F(e, t, n) {
                    return r(e, S, S, t, n)
                }
                var $ = []
                  , o = []
                  , e = {
                    _version: "3.6.0",
                    _config: {
                        classPrefix: "",
                        enableClasses: !0,
                        enableJSClass: !0,
                        usePrefixes: !0
                    },
                    _q: [],
                    on: function(e, t) {
                        var n = this;
                        setTimeout(function() {
                            t(n[e])
                        }, 0)
                    },
                    addTest: function(e, t, n) {
                        o.push({
                            name: e,
                            fn: t,
                            options: n
                        })
                    },
                    addAsyncTest: function(e) {
                        o.push({
                            name: null,
                            fn: e
                        })
                    }
                }
                  , n = function() {}
                  , a = (n.prototype = e,
                (n = new n).addTest("cookies", function() {
                    try {
                        d.cookie = "cookietest=1";
                        var e = -1 != d.cookie.indexOf("cookietest=");
                        return d.cookie = "cookietest=1; expires=Thu, 01-Jan-1970 00:00:01 GMT",
                        e
                    } catch (e) {
                        return !1
                    }
                }),
                n.addTest("localstorage", function() {
                    var e = "modernizr";
                    try {
                        return localStorage.setItem(e, e),
                        localStorage.removeItem(e),
                        !0
                    } catch (e) {
                        return !1
                    }
                }),
                n.addTest("sessionstorage", function() {
                    var e = "modernizr";
                    try {
                        return sessionStorage.setItem(e, e),
                        sessionStorage.removeItem(e),
                        !0
                    } catch (e) {
                        return !1
                    }
                }),
                n.addTest("cors", "XMLHttpRequest"in s && "withCredentials"in new XMLHttpRequest),
                n.addTest("history", function() {
                    var e = navigator.userAgent;
                    return (-1 === e.indexOf("Android 2.") && -1 === e.indexOf("Android 4.0") || -1 === e.indexOf("Mobile Safari") || -1 !== e.indexOf("Chrome") || -1 !== e.indexOf("Windows Phone") || "file:" === location.protocol) && s.history && "pushState"in s.history
                }),
                e._config.usePrefixes ? " -webkit- -moz- -o- -ms- ".split(" ") : ["", ""])
                  , u = (e._prefixes = a,
                d.documentElement)
                  , m = "svg" === u.nodeName.toLowerCase();
                if (!m) {
                    var t = void 0 !== s ? s : this
                      , l = d;
                    function I(e, t) {
                        var n = e.createElement("p")
                          , e = e.getElementsByTagName("head")[0] || e.documentElement;
                        return n.innerHTML = "x<style>" + t + "</style>",
                        e.insertBefore(n.lastChild, e.firstChild)
                    }
                    function f() {
                        var e = w.elements;
                        return "string" == typeof e ? e.split(" ") : e
                    }
                    function p(e) {
                        var t = X[e[G]];
                        return t || (t = {},
                        v++,
                        e[G] = v,
                        X[v] = t),
                        t
                    }
                    function W(e, t, n) {
                        return t = t || l,
                        h ? t.createElement(e) : !(t = (n = n || p(t)).cache[e] ? n.cache[e].cloneNode() : V.test(e) ? (n.cache[e] = n.createElem(e)).cloneNode() : n.createElem(e)).canHaveChildren || J.test(e) || t.tagUrn ? t : n.frag.appendChild(t)
                    }
                    function i(e) {
                        var t, n, r = p(e = e || l);
                        return !w.shivCSS || c || r.hasCSS || (r.hasCSS = !!I(e, "article,aside,dialog,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}mark{background:#FF0;color:#000}template{display:none}")),
                        h || (t = e,
                        (n = r).cache || (n.cache = {},
                        n.createElem = t.createElement,
                        n.createFrag = t.createDocumentFragment,
                        n.frag = n.createFrag()),
                        t.createElement = function(e) {
                            return w.shivMethods ? W(e, t, n) : n.createElem(e)
                        }
                        ,
                        t.createDocumentFragment = Function("h,f", "return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&(" + f().join().replace(/[\w\-:]+/g, function(e) {
                            return n.createElem(e),
                            n.frag.createElement(e),
                            'c("' + e + '")'
                        }) + ");return n}")(w, n.frag)),
                        e
                    }
                    function H(e) {
                        for (var t, n = e.getElementsByTagName("*"), r = n.length, o = RegExp("^(?:" + f().join("|") + ")$", "i"), i = []; r--; )
                            t = n[r],
                            o.test(t.nodeName) && i.push(t.applyElement(function(e) {
                                for (var t, n = e.attributes, r = n.length, o = e.ownerDocument.createElement(y + ":" + e.nodeName); r--; )
                                    (t = n[r]).specified && o.setAttribute(t.nodeName, t.nodeValue);
                                return o.style.cssText = e.style.cssText,
                                o
                            }(t)));
                        return i
                    }
                    function B(a) {
                        function l() {
                            clearTimeout(n._removeSheetTimer),
                            c && c.removeNode(!0),
                            c = null
                        }
                        var c, d, n = p(a), e = a.namespaces, t = a.parentWindow;
                        return !K || a.printShived || (void 0 === e[y] && e.add(y),
                        t.attachEvent("onbeforeprint", function() {
                            l();
                            for (var e, t, n, r = a.styleSheets, o = [], i = r.length, s = Array(i); i--; )
                                s[i] = r[i];
                            for (; n = s.pop(); )
                                if (!n.disabled && Z.test(n.media)) {
                                    try {
                                        t = (e = n.imports).length
                                    } catch (e) {
                                        t = 0
                                    }
                                    for (i = 0; i < t; i++)
                                        s.push(e[i]);
                                    try {
                                        o.push(n.cssText)
                                    } catch (e) {}
                                }
                            o = function(e) {
                                for (var t, n = e.split("{"), r = n.length, o = RegExp("(^|[\\s,>+~])(" + f().join("|") + ")(?=[[\\s,>+~#.:]|$)", "gi"), i = "$1" + y + "\\:$2"; r--; )
                                    (t = n[r] = n[r].split("}"))[t.length - 1] = t[t.length - 1].replace(o, i),
                                    n[r] = t.join("}");
                                return n.join("{")
                            }(o.reverse().join("")),
                            d = H(a),
                            c = I(a, o)
                        }),
                        t.attachEvent("onafterprint", function() {
                            for (var e = d, t = e.length; t--; )
                                e[t].removeNode();
                            clearTimeout(n._removeSheetTimer),
                            n._removeSheetTimer = setTimeout(l, 500)
                        }),
                        a.printShived = !0),
                        a
                    }
                    var c, h, g = t.html5 || {}, J = /^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i, V = /^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i, G = "_html5shiv", v = 0, X = {};
                    try {
                        var _ = l.createElement("a");
                        _.innerHTML = "<xyz></xyz>",
                        c = "hidden"in _,
                        h = 1 == _.childNodes.length || (l.createElement("a"),
                        void 0 === (O = l.createDocumentFragment()).cloneNode) || void 0 === O.createDocumentFragment || void 0 === O.createElement
                    } catch (e) {
                        h = c = !0
                    }
                    var w = {
                        elements: g.elements || "abbr article aside audio bdi canvas data datalist details dialog figcaption figure footer header hgroup main mark meter nav output picture progress section summary template time video",
                        version: "3.7.3",
                        shivCSS: !1 !== g.shivCSS,
                        supportsUnknownElements: h,
                        shivMethods: !1 !== g.shivMethods,
                        type: "default",
                        shivDocument: i,
                        createElement: W,
                        createDocumentFragment: function(e, t) {
                            if (e = e || l,
                            h)
                                return e.createDocumentFragment();
                            for (var n = (t = t || p(e)).frag.cloneNode(), r = 0, o = f(), i = o.length; r < i; r++)
                                n.createElement(o[r]);
                            return n
                        },
                        addElements: function(e, t) {
                            var n = w.elements;
                            "string" != typeof n && (n = n.join(" ")),
                            "string" != typeof e && (e = e.join(" ")),
                            w.elements = n + " " + e,
                            i(t)
                        }
                    }
                      , Z = (t.html5 = w,
                    i(l),
                    /^$|\b(?:all|print)\b/)
                      , y = "html5shiv"
                      , K = !(h || (_ = l.documentElement,
                    void 0 === l.namespaces) || void 0 === l.parentWindow || void 0 === _.applyElement || void 0 === _.removeNode || void 0 === t.attachEvent);
                    w.type += " print",
                    (w.shivPrint = B)(l),
                    "object" == typeof module && module.exports && (module.exports = w)
                }
                n.addTest("csspositionsticky", function() {
                    var e = "position:"
                      , t = T("a").style;
                    return t.cssText = e + a.join("sticky;" + e).slice(0, -e.length),
                    -1 !== t.position.indexOf("sticky")
                });
                function Q(e) {
                    var t, n = a.length, r = s.CSSRule;
                    if (void 0 === r)
                        return S;
                    if (e) {
                        if ((t = (e = e.replace(/^@/, "")).replace(/-/g, "_").toUpperCase() + "_RULE")in r)
                            return "@" + e;
                        for (var o = 0; o < n; o++) {
                            var i = a[o];
                            if (i.toUpperCase() + "_" + t in r)
                                return "@-" + i.toLowerCase() + "-" + e
                        }
                    }
                    return !1
                }
                Y = !("onblur"in d.documentElement);
                var Y, b, x, M, z, C, N, j, ee, k, A, te = function(e, t) {
                    var n;
                    return !!e && (!(n = (e = "on" + e)in (t = t && "string" != typeof t ? t : T(t || "div"))) && Y && ((t = t.setAttribute ? t : T("div")).setAttribute(e, ""),
                    n = "function" == typeof t[e],
                    t[e] !== S && (t[e] = S),
                    t.removeAttribute(e)),
                    n)
                }, ne = (e.hasEvent = te,
                e.testStyles = R), O = (n.addTest("touchevents", function() {
                    var t, e;
                    return "ontouchstart"in s || s.DocumentTouch && d instanceof DocumentTouch ? t = !0 : (e = ["@media (", a.join("touch-enabled),("), "heartz", ")", "{#modernizr{top:9px;position:absolute}}"].join(""),
                    ne(e, function(e) {
                        t = 9 === e.offsetTop
                    })),
                    t
                }),
                "Moz O ms Webkit"), P = e._config.usePrefixes ? O.toLowerCase().split(" ") : [], re = (e._domPrefixes = P,
                n.addTest("pointerevents", function() {
                    for (var e = !1, t = P.length, e = n.hasEvent("pointerdown"); t-- && !e; )
                        te(P[t] + "pointerdown") && (e = !0);
                    return e
                }),
                e._config.usePrefixes ? O.split(" ") : []), oe = (e._cssomPrefixes = re,
                e.atRule = Q,
                {
                    elem: T("modernizr")
                }), L = (n._q.push(function() {
                    delete oe.elem
                }),
                {
                    style: oe.elem.style
                }), g = (n._q.unshift(function() {
                    delete L.style
                }),
                e.testAllProps = r,
                e.prefixed = function(e, t, n) {
                    return 0 === e.indexOf("@") ? Q(e) : (-1 != e.indexOf("-") && (e = U(e)),
                    t ? r(e, t, n) : r(e, "pfx"))
                }
                );
                for (j in n.addTest("matchmedia", !!g("matchMedia", s)),
                e.testAllProps = F,
                n.addTest("flexwrap", F("flexWrap", "wrap", !0)),
                o)
                    if (o.hasOwnProperty(j)) {
                        if (b = [],
                        (x = o[j]).name && (b.push(x.name.toLowerCase()),
                        x.options) && x.options.aliases && x.options.aliases.length)
                            for (M = 0; M < x.options.aliases.length; M++)
                                b.push(x.options.aliases[M].toLowerCase());
                        for (z = E(x.fn, "function") ? x.fn() : x.fn,
                        C = 0; C < b.length; C++)
                            1 === (N = b[C].split(".")).length ? n[N[0]] = z : (!n[N[0]] || n[N[0]]instanceof Boolean || (n[N[0]] = new Boolean(n[N[0]])),
                            n[N[0]][N[1]] = z),
                            $.push((z ? "" : "no-") + N.join("-"))
                    }
                t = $,
                k = u.className,
                A = n._config.classPrefix || "",
                m && (k = k.baseVal),
                n._config.enableJSClass && (ee = new RegExp("(^|\\s)" + A + "no-js(\\s|$)"),
                k = k.replace(ee, "$1" + A + "js$2")),
                n._config.enableClasses && (k += " " + A + t.join(" " + A),
                m ? u.className.baseVal = k : u.className = k),
                delete e.addTest,
                delete e.addAsyncTest;
                for (var ie = 0; ie < n._q.length; ie++)
                    n._q[ie]();
                s.Modernizr = n
            }(window, document),
            Modernizr.viewport_width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0),
            Modernizr.viewport_height = Math.max(document.documentElement.clientHeight, window.innerHeight || 0),
            Modernizr.narrow = Modernizr.viewport_width <= 704,
            Modernizr.constrained = Modernizr.viewport_width <= 1200,
            Modernizr.site_menu = Modernizr.viewport_width <= 1020 ? "button" : "nav_bar",
            Modernizr.touch = Modernizr.touchevents || Modernizr.pointerevents && (0 < navigator.MaxTouchPoints || 0 < navigator.msMaxTouchPoints),
            Modernizr.phone = Modernizr.narrow && Modernizr.touch,
            Modernizr.tablet = Modernizr.viewport_width < 1075 && Modernizr.touch,
            Modernizr.desktop = !Modernizr.constrained && !Modernizr.touch,
            Modernizr.laptop = !(Modernizr.desktop || Modernizr.tablet || Modernizr.phone),
            new RegExp("hideallads")), sr_html = (Modernizr.adfree = patt.test(window.location.href),
            document.querySelector("html")), cn = sr_html.className, sr_host_parts = (Modernizr.phone ? sr_html.className = cn.concat(" phone") : Modernizr.tablet ? sr_html.className = cn.concat(" tablet") : (Modernizr.desktop || Modernizr.laptop) && (sr_html.className = cn.concat(" desktop")),
            window.location.hostname.split(".")), cn = sr_html.className, sr_logger = (Modernizr.is_build = Modernizr.is_live = Modernizr.is_dev = !1,
            "www" === sr_host_parts[0] || "fbref" === sr_host_parts[0] ? (Modernizr.is_live = !0,
            sr_html.className = cn.concat(" is_live")) : sr_host_parts[0].startsWith("b") ? (Modernizr.is_build = !0,
            sr_html.className = cn.concat(" is_build")) : (sr_host_parts[0].startsWith("d") || sr_host_parts[0].startsWith("r")) && (Modernizr.is_dev = !0,
            sr_html.className = cn.concat(" is_dev")),
            Modernizr.is_stathead = !1,
            ("stathead" === sr_host_parts[1] && "srdevel" === sr_host_parts[2] || "stathead" === sr_host_parts[0] || "www" === sr_host_parts[0] && "stathead" === sr_host_parts[1]) && (cn = sr_html.className,
            sr_html.className = cn.concat(" is_stathead"),
            Modernizr.is_stathead = !0),
            function() {
                var e = null
                  , t = {
                    enableLogger: function() {
                        null != e && (window.console.log = e)
                    },
                    disableLogger: function() {
                        e = console.log,
                        window.console.log = function() {}
                    }
                };
                return t
            }()), sr_utilities_js_loader = (!document.srdev && sr_is_production && sr_logger.disableLogger(),
            Modernizr.is_modern = 1,
            Modernizr.lang = document.lang || "",
            Modernizr.srdev = document.srdev,
            []);
            function vjs_readCookie(e) {
                for (var t = e + "=", n = document.cookie.split(";"), r = 0; r < n.length; r++) {
                    for (var o = n[r]; " " === o.charAt(0); )
                        o = o.substring(1, o.length);
                    if (0 === o.indexOf(t))
                        return decodeURIComponent(o.substring(t.length, o.length))
                }
                return null
            }
            function vjs_createCookie(e, t, n) {
                var r, o = "", o = n ? ((r = new Date).setTime(r.getTime() + 24 * n * 60 * 60 * 1e3),
                "; expires=" + r.toGMTString()) : "", n = encodeURIComponent(e) + "=" + encodeURIComponent(t) + o + "; path=/";
                document.cookie = n
            }
            !function(o) {
                function e(e, t) {
                    "use strict";
                    var n = o.document.getElementsByTagName("script")[0]
                      , r = o.document.createElement("script");
                    return r.src = e,
                    r.async = !0,
                    n.parentNode.insertBefore(r, n),
                    t && "function" == typeof t && (r.onload = t),
                    r
                }
                "undefined" != typeof module ? module.exports = e : o.loadJS = e
            }("undefined" != typeof global ? global : this),
            String.prototype.vjs_isMatch = function(e) {
                return null !== this.match(e)
            }
            ;
            var sr_time_begin = new Date
              , sr_perf_startTime = new Date
              , sr_perf_log = "<strong>Performance:</strong>"
              , sr_perf_lastTime = new Date;
            function vjs_ready(e) {
                "loading" != document.readyState ? e() : document.addEventListener("DOMContentLoaded", e)
            }
        </script>
        <script>
            let server = (document.srdev) ? 'https://cdn.ssref.net/nocdn/dev/' + document.srdev.substring(0, 2) : "https://cdn.ssref.net/req/202311303";
            let _sr_modern_url = server + "/js/pfr" + "/sr" + ((document.srdev) ? "" : "-min") + ".js";
            loadJS(_sr_modern_url, function() {
                vjs_ready(sr_fire_js);
            });
        </script>
        <!-- JS END -->
        <!-- include:end  ="/inc/klecko_header_full_pfr.html_f" -->
        <meta name="revised" content="06:28:42 23-Dec-2023"/>
        <meta name="HandheldFriendly" content="True"/>
        <meta name="HandheldFriendly" content="True"/>
        <meta name="generated-by" content="build_all_boxscores.pl"/>
        <meta name="format-detection" content="telephone=no"/>
        <meta name="apple-mobile-web-app-capable" content="no"/>
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="theme-color" content="#384d42"/>
        <meta name="msapplication-navbutton-color" content="#384d42"/>
        <meta name="apple-mobile-web-app-status-bar-style" content="#384d42"/>
        <!-- HeaderSeoSocial -->
        <meta name="keywords" content="">
        <meta itemprop="url" content="https://www.pro-football-reference.com">
        <meta itemprop="name" content="Pro Football Reference">
        <meta itemprop="alternateName" content="PFRef">
        <meta property="fb:app_id" content="">
        <meta property="og:url" content="https://www.pro-football-reference.com/boxscores/202312160det.htm">
        <meta property="og:title" content="Denver Broncos at Detroit Lions - December 16th, 2023 | Pro-Football-Reference.com">
        <meta property="og:site_name" content="Pro-Football-Reference.com">
        <meta property="og:type" content="    article"/>
        <meta property="og:description" content="Denver Broncos 17 at Detroit Lions 42 on December 16th, 2023  - Full team and player stats and box score">
        <meta property="og:image" content="http://ssref.net/scripts/image_resize.cgi?foo=bar&flat=0&url1=https://cdn.ssref.net/req/202311303/tlogo/pfr/den-2023.png&url2=https://cdn.ssref.net/req/202311303/tlogo/pfr/det-2023.png">
        <meta name="twitter:card" content="summary">
        <meta name="twitter:site" content="@pfref">
        <meta name="twitter:creator" content="@pfref">
        <meta property="twitter:image" content="http://ssref.net/scripts/image_resize.cgi?foo=bar&flat=0&url1=https://cdn.ssref.net/req/202311303/tlogo/pfr/den-2023.png&url2=https://cdn.ssref.net/req/202311303/tlogo/pfr/det-2023.png">
        <meta name="twitter:domain" content="Pro-Football-Reference.com">
        <meta name="referrer" content="unsafe-url">
        <!-- HeaderSeoSocial:END -->
        <!-- tiles, touch, favicons -->
        <link rel="apple-touch-icon-precomposed" sizes="180x180" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-180x180-precomposed.png">
        <link rel="icon" sizes="48x48" href="https://cdn.ssref.net/req/202311303/favicons/pfr/favicon-48.png">
        <link rel="shortcut icon" sizes="228x228" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-228x228-precomposed.png">
        <link rel="apple-touch-icon" sizes="228x228" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-228x228-precomposed.png">
        <link rel="apple-touch-icon" sizes="195x195" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-195x195-precomposed.png">
        <link rel="apple-touch-icon" sizes="180x180" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-180x180-precomposed.png">
        <link rel="apple-touch-icon" sizes="152x152" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-152x152-precomposed.png">
        <link rel="apple-touch-icon" sizes="144x144" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-144x144-precomposed.png">
        <link rel="apple-touch-icon" sizes="128x128" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-128x128-precomposed.png">
        <link rel="apple-touch-icon" sizes="120x120" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-120x120-precomposed.png">
        <link rel="apple-touch-icon" sizes="114x114" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-114x114-precomposed.png">
        <link rel="apple-touch-icon" sizes="76x76" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-76x76-precomposed.png">
        <link rel="apple-touch-icon" sizes="72x72" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-72x72-precomposed.png">
        <link rel="apple-touch-icon" sizes="57x57" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-57x57-precomposed.png">
        <link rel="icon" sizes="32x32" href="https://cdn.ssref.net/req/202311303/favicons/pfr/favicon-32.png">
        <!--[if IE]>
    <link rel="shortcut icon"                                href="https://cdn.ssref.net/req/202311303/favicons/pfr/favicon.ico"><![endif]-->
        <meta name="msapplication-TileColor" content="#005629"/>
        <meta name="msapplication-TileImage" content="https://cdn.ssref.net/req/202311303/favicons/pfr/ms-tile-144.png"/>
        <link rel=search type="application/opensearchdescription+xml" href="https://cdn.ssref.net/req/202311303/opensearch/opensearch-pfr.xml" title=" Player and Team Search">
        <!-- tiles, touch, favicons:end -->
        <!-- ad code: begin -->
        <link rel="preconnect" href="https://a.pub.network/" crossorigin/>
        <link rel="preconnect" href="https://b.pub.network/" crossorigin/>
        <link rel="preconnect" href="https://c.pub.network/" crossorigin/>
        <link rel="preconnect" href="https://d.pub.network/" crossorigin/>
        <link rel="preconnect" href="https://c.amazon-adsystem.com" crossorigin/>
        <link rel="preconnect" href="https://s.amazon-adsystem.com" crossorigin/>
        <link rel="preconnect" href="https://btloader.com/" crossorigin/>
        <link rel="preconnect" href="https://api.btloader.com/" crossorigin/>
        <link rel="preconnect" href="https://confiant-integrations.global.ssl.fastly.net" crossorigin/>
        <script data-ad-client="ca-pub-5319453360923253" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <link rel="stylesheet" href="https://a.pub.network/pro-football-reference/cls.css" type="text/css">
        <script>
            var freestar = freestar || {};
            freestar.config = freestar.config || {};
            freestar.config.enabled_slots = ["div-gpt-ad-728x90-GeneralHeader", "div-gpt-ad-728x90-BTF-1", "div-gpt-ad-728x90-BTF-2", "div-gpt-ad-728x90-BTF-3", "div-gpt-ad-728x90-Footer"];
            if (sr_detect_ie || sr_detect_edge || Modernizr.adfree || document.getElementById('sr_suppress_ads') || Modernizr.viewport_width < 1810) {// do not include the rails
            } else {
                freestar.config.enabled_slots.push('div-gpt-ad-160x600-1');
                freestar.config.enabled_slots.push('div-gpt-ad-160x600-2');
            }
        </script>
        <script data-cfasync="false" type="text/javascript">
            var fs_debug = window.location.search.indexOf('fsdebug') == -1 ? false : true;
            freestar.hitTime = Date.now();
            freestar.queue = freestar.queue || [];
            freestar.config = freestar.config || {};
            freestar.queue.push(function() {
                // Include the line reflecting the area/section of the site you are on
                googletag.pubads().setTargeting('sr_site_id', 'pfr');
            });
            !function(a, b) {
                if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {
                    return;
                }
                var c = b.getElementsByTagName("script")[0]
                  , d = b.createElement("script")
                  , e = "https://a.pub.network/pro-football-reference";
                e += fs_debug ? "/qa/pubfig.min.js" : "/pubfig.min.js",
                d.async = !0,
                d.src = e,
                c.parentNode.insertBefore(d, c)
            }(window, document);
        </script>
        <!-- ad code:end -->
    </head>
    <body class="pfr">
        <div id="wrap">
            <div id="header" role="banner">
                <ul id="subnav" class="notranslate">
                    <li>
                        <a href="https://www.sports-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">
                            <svg height="15px" width="20px">
                                <use xlink:href="#ic-sr-pennant"></use>
                            </svg>
                            Sports &nbsp;Reference &#8239;&reg;
                        </a>
                    </li>
                    <li>
                        <a href="https://www.baseball-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Baseball</a>
                    </li>
                    <li class="current">
                        <a href="https://www.pro-football-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Football</a>
                        <a href="https://www.sports-reference.com/cfb/">(college)</a>
                    </li>
                    <li>
                        <a href="https://www.basketball-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Basketball</a>
                        <a href="https://www.sports-reference.com/cbb/">(college)</a>
                    </li>
                    <li>
                        <a href="https://www.hockey-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Hockey</a>
                    </li>
                    <li>
                        <a href="https://fbref.com/it/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Calcio</a>
                    </li>
                    <li>
                        <a href="https://www.sports-reference.com/blog/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Blog</a>
                    </li>
                    <li>
                        <a href="https://stathead.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Stathead &#8239;&reg;</a>
                    </li>
                    <li>
                        <a href="https://www.immaculategrid.com/football/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Immaculate Grid</a>
                    </li>
                    <li>
                        <a href="https://www.sports-reference.com/feedback/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Questions or Comments?</a>
                    </li>
                    <li class="user logged_in">
                        Welcome <span class="username"></span>
                        &nbsp;&#183;&nbsp;<a href="https://stathead.com/profile/?utm_source=pfr&amp;utm_medium=sr_xsite&amp;utm_campaign=2023_01_srnav_account">Your Account</a>
                    </li>
                    <li class="user logged_in">
                        <a class="logout" onclick="sr_auth_logout_page_elements();if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/profile/?do=logout">Logout</a>
                    </li>
                    <li class="user not_logged_in">
                        <a class="login" onclick="if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/users/login.cgi?token=1">Ad-Free Login</a>
                    </li>
                    <li class="user not_logged_in">
                        <a href="https://stathead.com/users/signup.cgi">Create Account</a>
                    </li>
                </ul>
                <a href="/">
                    <img src="https://cdn.ssref.net/req/202311303/logos/pfr-logo.svg" onerror="this.src='https://cdn.ssref.net/req/202311303/logos/pfr-logo.png'; this.onerror = null;" alt="Pro-Football-Reference.com Logo &amp; Link to home page"/>
                </a>
                <div id="nav_trigger" role="button">
                    <a href="#site_menu_link">MENU</a>
                </div>
                <div id="nav" role="navigation" aria-label="Pro-Football-Reference.com sections">
                    <ul id="main_nav" class="hoversmooth nohover">
                        <li id="header_players">
                            <a href="/players">Players</a>
                        </li>
                        <li id="header_teams">
                            <a href="/teams/">Teams</a>
                        </li>
                        <li id="header_years">
                            <a href="/years/">Seasons</a>
                        </li>
                        <li id="header_leaders">
                            <a href="/leaders/">Leaders</a>
                        </li>
                        <li id="header_scores" class="current">
                            <a href="/boxscores/">NFL Scores</a>
                        </li>
                        <li id="header_draft" class="">
                            <a href="/draft/">Draft</a>
                        </li>
                        <li id="header_playindex" class="">
                            <a href="https://stathead.com/sport/football/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_topnav_stathead&utm_content=lnk_top">Stathead</a>
                        </li>
                        <li>
                            <a href="https://www.pro-football-reference.com/email/">Newsletter</a>
                        </li>
                        <li>
                            <a data-scroll href="#site_menu_link" class="opener">Full Site Menu Below</a>
                        </li>
                    </ul>
                    <div class="breadcrumbs">
                        You are here: 
                        <div itemscope itemtype="https://schema.org/BreadcrumbList" class="crumbs">
                            <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                                <a itemprop="item" href="/">
                                    <span itemprop="name">PFR Home Page</span>
                                </a>
                                <meta itemprop="position" content="1"/>
                            </span>
                            &gt;
                            <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                                <a itemprop="item" href="/boxscores/">
                                    <span itemprop="name">Boxscores</span>
                                </a>
                                <meta itemprop="position" content="2"/>
                            </span>
                            &gt;<strong>Denver Broncos at Detroit Lions - December 16th, 2023</strong>
                        </div>
                    </div>
                    <ul class="usertools bullets-inline">
                        <li class="user logged_in">
                            Welcome <span class="username"></span>
                            &nbsp;&#183;&nbsp;<a href="https://stathead.com/profile/?utm_source=pfr&amp;utm_medium=sr_xsite&amp;utm_campaign=2023_01_srnav_account">Your Account</a>
                        </li>
                        <li class="user logged_in">
                            <a class="logout" onclick="sr_auth_logout_page_elements();if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/profile/?do=logout">Logout</a>
                        </li>
                        <li class="user not_logged_in">
                            <a class="login" onclick="if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/users/login.cgi?token=1">Ad-Free Login</a>
                        </li>
                        <li class="user not_logged_in">
                            <a href="https://stathead.com/users/signup.cgi">Create Account</a>
                        </li>
                    </ul>
                    <!-- ul.user -->
                </div>
                <!-- div#nav -->
                <script>
                    function sr_menus_setupMainNav_button_inline() {
                        if (sr_detect_operaMini || !("classList"in document.createElement("_"))) {
                            return false;
                        }
                        var nav_trigger = document.getElementById('nav_trigger');
                        if (!nav_trigger || nav_trigger.triggered) {
                            return false;
                        }
                        nav_trigger.triggered = true;
                        var nav = document.getElementById('nav');
                        var nav_trigger_a = nav_trigger.querySelector('a');
                        if (nav_trigger_a) {
                            nav_trigger_a.setAttribute('href', 'javascript:void(0)');
                            nav_trigger.onclick = function(event) {
                                nav.classList.toggle('open');
                                var is_open = nav.classList.contains('open');
                                if (is_open) {
                                    nav_trigger.classList.add('open');
                                } else {
                                    nav_trigger.classList.remove('open');
                                }
                                event.preventDefault();
                                try {
                                    sr_record_analytics_event('MainNavButtonClick_inline', sr_record_directory(), sr_record_page());
                                } catch (err) {}
                            }
                            ;
                        }
                        return true;
                    }
                    sr_menus_setupMainNav_button_inline();
                </script>
                <div class="search" role="search" aria-label="Site Search for players, teams and sections">
                    <form method="get" name="f_big" action="/search/search.fcgi">
                        <div class="ac-outline">
                            <div class="ac-wrapper">
                                <input type="search" tabindex="-1" class="ac-hint" name="hint" placeholder="" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" dir="auto" aria-label="Search suggestions based on user search input">
                                <input tabindex="1" type="search" class="ac-input completely" name="search" placeholder="Enter Person, Team, Section, etc" aria-label="Enter a player, team or section name" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" dir="auto"/>
                                <div class="ac-dropdown"></div>
                            </div>
                        </div>
                        <input type="submit" value="Search" tabindex="2"/>
                        <input type="hidden" name="pid" value="" data-search-id>
                        <input type="hidden" name="idx" value="" data-search-idx>
                    </form>
                </div>
                <!-- div.search -->
            </div>
            <!-- div#header -->
            <style>
                .site_announcement {
                    background-color: #fffea6;
                    text-align: center;
                    padding: .4em 0;
                    width: 100%;
                }

                .site_announcement div {
                    margin: 0 .3em;
                }

                .site_announcement span {
                    white-space: nowrap;
                }

                @media only screen and (max-width: 1000px) {
                    .site_annoucement_extra {
                        display: none;
                    }
                }
            </style>
            <div id="srcom">
                <!-- fs_general_header -->
                <div class="adblock">
                    <!-- div#fs_fs_general_header  -->
                    <style>
                        #srcom .adblock.stn, #content .adblock.stn {
                            height: auto;
                            width: 728px;
                            max-width: 100%;
                            aspect-ratio: 1.677419;
                            margin: auto;
                            overflow: visible;
                        }

                        body:not(#stnPriority1):not(#stnPriority2):not(#stnPriority3) {
                            z-index: revert !important;
                        }
                    </style>
                    <script>
                        function apiFunction(ApiHandshake) {
                            const playerDiv = document.querySelector('[data-stn-api="apiFunction"]');
                            const api = ApiHandshake(playerDiv);
                            new IntersectionObserver(moes=>{
                                const bcr = moes.pop().boundingClientRect;
                                api.float = bcr.y <= 0;
                            }
                            ,{
                                threshold: [0.9]
                            }).observe(document.querySelector('[data-stn-api="apiFunction"]'));
                        }
                    </script>
                    <div class="adblock stn">
                        <div class='s2nPlayer k-PV0o3K0Y' data-type='float' data-stn-api="apiFunction"></div>
                        <script type='text/javascript' async src='//embed.sendtonews.com/player3/embedcode.js?fk=PV0o3K0Y&cid=13629&offsetx=0&offsety=0&floatwidth=400&floatposition=bottom-right' data-type='s2nScript'></script>
                    </div>
                    <!-- /div.#fs_fs_general_header -->
                </div>
            </div>
            <div id="inner_nav" role="navigation" aria-label="Sections on this page and/or other pages related to this page" class=" inactive suppress_inpage_nav">
                <ul class="hoversmooth">
                    <li class="index ">
                        <a href="/boxscores/">NFL Scores & Boxes</a>
                    </li>
                    <li class="full ">
                        <a href="/years/2023/">2023 NFL Scores & Schedule</a>
                    </li>
                    <li class="full ">
                        <a href="/teams/det/2023.htm">Detroit Lions Schedule</a>
                    </li>
                    <li class="full ">
                        <a href="/teams/den/2023.htm">Denver Broncos Schedule</a>
                    </li>
                    <li data-fade-selector="#inpage_nav" class="condensed hasmore ">
                        <a href="#">Schedules & Boxscores</a>
                        <div>
                            <ul class=" in_list">
                                <li>
                                    <a href="/years/2023/">2023 NFL Scores & Schedule</a>
                                </li>
                                <li>
                                    <a href="/teams/det/2023.htm">Detroit Lions Schedule</a>
                                </li>
                                <li>
                                    <a href="/teams/den/2023.htm">Denver Broncos Schedule</a>
                                </li>
                            </ul>
                        </div>
                    </li>
                </ul>
                <div id="inpage_nav" class="html_built">
                    <p class="listhead inpage">On this page:</p>
                    <ul class="in_list inpage">
                        <li>
                            <a href="#all_scoring">Scoring</a>
                        </li>
                        <li>
                            <a href="#all_game_info">Game Info</a>
                        </li>
                        <li>
                            <a href="#all_expected_points">Expected Points Summary</a>
                        </li>
                        <li>
                            <a href="#all_team_stats">Team Stats</a>
                        </li>
                        <li>
                            <a href="#all_player_offense">Passing, Rushing, & Receiving</a>
                        </li>
                        <li>
                            <a href="#all_player_defense">Defense</a>
                        </li>
                        <li>
                            <a href="#all_returns">Kick/Punt Returns</a>
                        </li>
                        <li>
                            <a href="#all_kicking">Kicking & Punting</a>
                        </li>
                        <li>
                            <a href="#all_passing_advanced">Advanced Passing</a>
                        </li>
                        <li>
                            <a href="#all_rushing_advanced">Advanced Rushing</a>
                        </li>
                        <li>
                            <a href="#all_receiving_advanced">Advanced Receiving</a>
                        </li>
                        <li>
                            <a href="#all_defense_advanced">Advanced Defense</a>
                        </li>
                        <li>
                            <a href="#all_home_starters">Lions Starters</a>
                        </li>
                        <li>
                            <a href="#all_home_snap_counts">Lions Snap Counts</a>
                        </li>
                        <li>
                            <a href="#all_home_drives">Lions Drives</a>
                        </li>
                        <li>
                            <a href="#all_pbp">Full Play-By-Play</a>
                        </li>
                        <li>
                            <a href="#site_menu_link">Full Site Menu</a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- div#inner_nav -->
            <div id="content" role="main" class="box">
                <h1>Denver Broncos at Detroit Lions - December 16th, 2023</h1>
                <div class="section_wrapper setup_commented commented" id="all_other_scores">
                    <div class="section_heading assoc_other_scores" id="other_scores_sh">
                        <span class="section_anchor" id="other_scores_link" data-label="All Week 15 Games"></span>
                    </div>
                    <div class="placeholder"></div>
                    <!--     <div class="section_content" id="div_other_scores">
	    <div class="game_summaries compressed">
   <h2>NFL Scores &mdash; <a href="/years/2023/week_15.htm">Week 15</a></h2>
   
      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/sdg/2023.htm">LAC</a></td>
			<td class="right">21</td>
			<td class="right gamelink">
				<a href="/boxscores/202312140rai.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/rai/2023.htm">LVR</a></strong></td>
			<td class="right">63</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/min/2023.htm">MIN</a></td>
			<td class="right">24</td>
			<td class="right gamelink">
				<a href="/boxscores/202312160cin.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/cin/2023.htm">CIN</a></strong></td>
			<td class="right">27</td>
			<td class="right">OT
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/pit/2023.htm">PIT</a></td>
			<td class="right">13</td>
			<td class="right gamelink">
				<a href="/boxscores/202312160clt.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/clt/2023.htm">IND</a></strong></td>
			<td class="right">30</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover current ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/den/2023.htm">DEN</a></td>
			<td class="right">17</td>
			<td class="right gamelink">
				<a href="/boxscores/202312160det.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/det/2023.htm">DET</a></strong></td>
			<td class="right">42</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/dal/2023.htm">DAL</a></td>
			<td class="right">10</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170buf.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/buf/2023.htm">BUF</a></strong></td>
			<td class="right">31</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/atl/2023.htm">ATL</a></td>
			<td class="right">7</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170car.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/car/2023.htm">CAR</a></strong></td>
			<td class="right">9</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/chi/2023.htm">CHI</a></td>
			<td class="right">17</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170cle.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/cle/2023.htm">CLE</a></strong></td>
			<td class="right">20</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><strong><a href="/teams/sfo/2023.htm">SFO</a></strong></td>
			<td class="right">45</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170crd.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><a href="/teams/crd/2023.htm">ARI</a></td>
			<td class="right">29</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><strong><a href="/teams/tam/2023.htm">TAM</a></strong></td>
			<td class="right">34</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170gnb.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><a href="/teams/gnb/2023.htm">GNB</a></td>
			<td class="right">20</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><strong><a href="/teams/rav/2023.htm">BAL</a></strong></td>
			<td class="right">23</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170jax.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><a href="/teams/jax/2023.htm">JAX</a></td>
			<td class="right">7</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/nyj/2023.htm">NYJ</a></td>
			<td class="right">0</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170mia.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/mia/2023.htm">MIA</a></strong></td>
			<td class="right">30</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/nyg/2023.htm">NYG</a></td>
			<td class="right">6</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170nor.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/nor/2023.htm">NOR</a></strong></td>
			<td class="right">24</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><strong><a href="/teams/kan/2023.htm">KAN</a></strong></td>
			<td class="right">27</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170nwe.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><a href="/teams/nwe/2023.htm">NWE</a></td>
			<td class="right">17</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><strong><a href="/teams/htx/2023.htm">HOU</a></strong></td>
			<td class="right">19</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170oti.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><a href="/teams/oti/2023.htm">TEN</a></td>
			<td class="right">16</td>
			<td class="right">OT
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/was/2023.htm">WAS</a></td>
			<td class="right">20</td>
			<td class="right gamelink">
				<a href="/boxscores/202312170ram.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/ram/2023.htm">LAR</a></strong></td>
			<td class="right">28</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

      <div class="game_summary nohover ">
	<table class="teams">
		<tbody>       
		<tr class="">
			<td><a href="/teams/phi/2023.htm">PHI</a></td>
			<td class="right">17</td>
			<td class="right gamelink">
				<a href="/boxscores/202312180sea.htm">F<span class="no_mobile">inal</span></a>
				
			</td>
		</tr>
		<tr class="">
			<td><strong><a href="/teams/sea/2023.htm">SEA</a></strong></td>
			<td class="right">20</td>
			<td class="right">&nbsp;
			</td>
		</tr>
		</tbody>
	</table>
	

</div>

   
</div>

		
    </div>
-->
                </div>
                <div class="scorebox">
                    <div>
                        <div>
                            <div class="media-item logo loader">
                                <img class="teamlogo" src="https://cdn.ssref.net/req/202312151/tlogo/pfr/den-2023.png" alt="2023 Denver Broncos Logo">
                                <p>
                                    <a href="http://www.sportslogos.net/">via Sports Logos.net</a>
                                </p>
                                <p>
                                    <a href="https://www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">About logos</a>
                                </p>
                            </div>
                            <strong>
                                <a href="/teams/den/2023.htm">Denver Broncos</a>
                            </strong>
                        </div>
                        <div class="scores">
                            <div class="score">17</div>
                        </div>
                        <div>7-7</div>
                        <div class="prevnext">
                            <a href="/boxscores/202312100sdg.htm" class="button2 prev">Prev Game</a>
                            <a href="/boxscores/202312240den.htm" class="button2 next">Next Game</a>
                        </div>
                        <div class="datapoint">
                            <strong>Coach</strong>
                            : <a href="/coaches/PaytSe0.htm">Sean Payton</a>
                        </div>
                    </div>
                    <div>
                        <div>
                            <div class="media-item logo loader">
                                <img class="teamlogo" src="https://cdn.ssref.net/req/202312151/tlogo/pfr/det-2023.png" alt="2023 Detroit Lions Logo">
                                <p>
                                    <a href="http://www.sportslogos.net/">via Sports Logos.net</a>
                                </p>
                                <p>
                                    <a href="https://www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">About logos</a>
                                </p>
                            </div>
                            <strong>
                                <a href="/teams/det/2023.htm">Detroit Lions</a>
                            </strong>
                        </div>
                        <div class="scores">
                            <div class="score">42</div>
                        </div>
                        <div>10-4</div>
                        <div class="prevnext">
                            <a href="/boxscores/202312100chi.htm" class="button2 prev">Prev Game</a>
                            <a href="/boxscores/202312240min.htm" class="button2 next">Next Game</a>
                        </div>
                        <div class="datapoint">
                            <strong>Coach</strong>
                            : <a href="/coaches/CampDa1.htm">Dan Campbell</a>
                        </div>
                    </div>
                    <div class="scorebox_meta">
                        <div>Saturday Dec 16, 2023</div>
                        <div>
                            <strong>Start Time</strong>
                            : 8:15pm
                        </div>
                        <div>
                            <strong>Stadium</strong>
                            : <a href="/stadiums/DET00.htm">Ford Field</a>
                        </div>
                        <div>
                            <strong>Attendance</strong>
                            : <a href="/years/2023/attendance.htm">64,500</a>
                        </div>
                        <div>
                            <strong>Time of Game</strong>
                            : 3:03
                        </div>
                        <div>
                            <em>
                                Logos <a href="http://www.sportslogos.net/">via Sports Logos.net</a>
                                / <a href="//www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">About logos</a>
                            </em>
                        </div>
                    </div>
                </div>
                <style>
                    .fb .scorebox {
                        position: relative;
                        max-width: 640px;
                    }

                    .fb .scorebox > div:first-child .scores > div:after {
                        position: absolute;
                        left: 0;
                        content: ':';
                        width: 100%;
                    }

                    .fb .scorebox .scorebox_meta {
                        margin-top: 10px;
                    }

                    .fb .scorebox .score {
                        font-size: 1.9em;
                        font-weight: 800;
                    }

                    .fb .scorebox .score_pen, .fb .scorebox .score_aggr, .fb .scorebox .score_xg {
                        font-size: 1.28em;
                        font-weight: bold;
                        margin-top: 12px;
                    }

                    .fb .scorebox > div:first-child .score_pen:before, .fb .scorebox > div:first-child .score_aggr:before, .fb .scorebox > div:first-child .score_xg:before {
                        position: absolute;
                        width: 100%;
                        left: 0;
                        margin-top: -11px;
                        color: #777;
                        font-size: 13px;
                        font-weight: bold;
                    }

                    .fb .scorebox > div:first-child .score_pen:before {
                        content: 'Penalties';
                    }

                    .fb .scorebox > div:first-child .score_aggr:before {
                        content: 'Aggregate';
                    }

                    .fb .scorebox > div:first-child .score_xg:before {
                        content: 'xG';
                    }

                    @media screen and (min-width: 470px) {
                        .fb .scorebox .prevnext {
                            min-width: 200px;
                        }
                    }

                    @media screen and (min-width: 800px) {
                        .fb .scorebox .scores {
                            position: absolute;
                            top: 35px;
                            left: 0;
                        }

                        .fb .scorebox > div:first-child .scores {
                            left: auto;
                            right: 0;
                        }

                        .fb .scorebox .scores > div {
                            padding: 0 10px;
                        }

                        .fb .scorebox > div:first-child .scores > div:after {
                            width: 200%;
                        }

                        .fb .scorebox .score {
                            font-size: 2.7em;
                        }

                        .fb .scorebox .score_pen, .fb .scorebox .score_aggr, .fb .scorebox .score_xg {
                            margin-top: 17px;
                        }

                        .fb .scorebox > div:first-child .score_pen:before, .fb .scorebox > div:first-child .score_aggr:before, .fb .scorebox > div:first-child .score_xg:before {
                            width: 200%;
                            margin-top: -15px;
                        }

                        .fb .scorebox > div {
                            padding: 0 8%;
                            position: relative;
                        }

                        .fb .scorebox .event {
                            position: absolute;
                            padding: 0;
                            top: 15px;
                            right: -160px;
                            text-align: left;
                        }

                        .fb .scorebox .event#a {
                            text-align: right;
                            left: -160px;
                            right: auto;
                        }

                        .fb .scorebox .event > div {
                            margin-bottom: 6px;
                        }
                    }

                    @media screen and (max-width: 1020px) {
                        .fb .scorebox .event {
                            display: none;
                        }
                    }
                </style>
                <div class="linescore_wrap">
                    <table class="linescore nohover stats_table no_freeze">
                        <thead>
                            <tr>
                                <th>&nbsp;</th>
                                <th>&nbsp;</th>
                                <th>1</th>
                                <th>2</th>
                                <th>3</th>
                                <th>4</th>
                                <th>Final</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="center">
                                    <div class="media-item logo loader">
                                        <img class="teamlogo" src="https://cdn.ssref.net/req/202312151/tlogo/pfr/den-2023.png" alt="2023 Denver Broncos Logo">
                                        <p>
                                            <a href="http://www.sportslogos.net/">via Sports Logos.net</a>
                                        </p>
                                        <p>
                                            <a href="https://www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">About logos</a>
                                        </p>
                                    </div>
                                </td>
                                <td>
                                    <a href="/teams/den/2023.htm">Denver Broncos</a>
                                </td>
                                <td class="center">0</td>
                                <td class="center">0</td>
                                <td class="center">10</td>
                                <td class="center">7</td>
                                <td class="center">17</td>
                            </tr>
                            <tr>
                                <td class="center">
                                    <div class="media-item logo loader">
                                        <img class="teamlogo" src="https://cdn.ssref.net/req/202312151/tlogo/pfr/det-2023.png" alt="2023 Detroit Lions Logo">
                                        <p>
                                            <a href="http://www.sportslogos.net/">via Sports Logos.net</a>
                                        </p>
                                        <p>
                                            <a href="https://www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">About logos</a>
                                        </p>
                                    </div>
                                </td>
                                <td>
                                    <a href="/teams/det/2023.htm">Detroit Lions</a>
                                </td>
                                <td class="center">0</td>
                                <td class="center">21</td>
                                <td class="center">7</td>
                                <td class="center">14</td>
                                <td class="center">42</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="filter">
                    <div class="">
                        <a data-scroll href="#all_team_stats">Team Stats</a>
                    </div>
                    <div class="">
                        <a data-scroll href="#all_expected_points">Expected Points</a>
                    </div>
                    <div class="">
                        <a data-scroll href="#all_player_offense">Player Stats</a>
                    </div>
                    <div class="">
                        <a data-scroll href="#all_vis_starters">Starting Lineups</a>
                    </div>
                    <div class="">
                        <a data-scroll href="#all_vis_snap_counts">Snap Counts</a>
                    </div>
                    <div class="">
                        <a data-scroll href="#all_vis_drives">Drives</a>
                    </div>
                    <div class="">
                        <a data-scroll href="#all_pbp">Play-by-Play</a>
                    </div>
                </div>
                <!-- fs_btf_3 -->
                <div class="adblock">
                    <!-- div#fs_fs_btf_3  -->
                    <div align="center" id="div-gpt-ad-728x90-BTF-3" data-freestar-ad="__300x250 __970x90">
                        <script data-cfasync="false" type='text/javascript'>
                            if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {} else {
                                console.log('push ad:div-gpt-ad-728x90-BTF-3');
                                freestar.queue.push(function() {
                                    googletag.display('div-gpt-ad-728x90-BTF-3');
                                });
                            }
                        </script>
                    </div>
                    <!-- /div.#fs_fs_btf_3 -->
                </div>
                <div id="all_scoring" class="table_wrapper">
                    <div class="section_heading assoc_scoring" id="scoring_sh">
                        <span class="section_anchor" id="scoring_link" data-label="Scoring"></span>
                        <h2>Scoring</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="table_container" id="div_scoring">
                        <table class="stats_table" id="scoring" data-cols-to-freeze="1,2">
                            <caption>Scoring Table</caption>
                            <colgroup>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                            </colgroup>
                            <thead>
                                <tr>
                                    <th aria-label="Quarter" data-stat="quarter" scope="col" class=" poptip center">Quarter</th>
                                    <th aria-label="time" data-stat="time" scope="col" class=" poptip center">Time</th>
                                    <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left">Tm</th>
                                    <th aria-label="Detail" data-stat="description" scope="col" class=" poptip left" data-tip="Play description">Detail</th>
                                    <th aria-label="DEN" data-stat="vis_team_score" scope="col" class=" poptip center">DEN</th>
                                    <th aria-label="DET" data-stat="home_team_score" scope="col" class=" poptip center">DET</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row" class="center " data-stat="quarter">2</th>
                                    <td class="right " data-stat="time">12:31</td>
                                    <td class="left " data-stat="team">Lions</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a>
                                        19 yard pass from <a href="/players/G/GoffJa00.htm">Jared Goff</a>
                                        (<a href="/players/B/BadgMi00.htm">Michael Badgley</a>
                                        kick)
                                    </td>
                                    <td class="right iz" data-stat="vis_team_score">0</td>
                                    <td class="right " data-stat="home_team_score">7</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="center iz" data-stat="quarter"></th>
                                    <td class="right " data-stat="time">8:15</td>
                                    <td class="left " data-stat="team">Lions</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a>
                                        9 yard pass from <a href="/players/G/GoffJa00.htm">Jared Goff</a>
                                        (<a href="/players/B/BadgMi00.htm">Michael Badgley</a>
                                        kick)
                                    </td>
                                    <td class="right iz" data-stat="vis_team_score">0</td>
                                    <td class="right " data-stat="home_team_score">14</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="center iz" data-stat="quarter"></th>
                                    <td class="right " data-stat="time">0:19</td>
                                    <td class="left " data-stat="team">Lions</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a>
                                        15 yard pass from <a href="/players/G/GoffJa00.htm">Jared Goff</a>
                                        (<a href="/players/B/BadgMi00.htm">Michael Badgley</a>
                                        kick)
                                    </td>
                                    <td class="right iz" data-stat="vis_team_score">0</td>
                                    <td class="right " data-stat="home_team_score">21</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="center " data-stat="quarter">3</th>
                                    <td class="right " data-stat="time">10:34</td>
                                    <td class="left " data-stat="team">Broncos</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a>
                                        3 yard pass from <a href="/players/W/WilsRu00.htm">Russell Wilson</a>
                                        (<a href="/players/L/LutzWi00.htm">Wil Lutz</a>
                                        kick)
                                    </td>
                                    <td class="right " data-stat="vis_team_score">7</td>
                                    <td class="right " data-stat="home_team_score">21</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="center iz" data-stat="quarter"></th>
                                    <td class="right " data-stat="time">6:57</td>
                                    <td class="left " data-stat="team">Lions</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a>
                                        3 yard pass from <a href="/players/G/GoffJa00.htm">Jared Goff</a>
                                        (<a href="/players/B/BadgMi00.htm">Michael Badgley</a>
                                        kick)
                                    </td>
                                    <td class="right " data-stat="vis_team_score">7</td>
                                    <td class="right " data-stat="home_team_score">28</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="center iz" data-stat="quarter"></th>
                                    <td class="right " data-stat="time">0:43</td>
                                    <td class="left " data-stat="team">Broncos</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/L/LutzWi00.htm">Wil Lutz</a>
                                        23 yard field goal 
                                    </td>
                                    <td class="right " data-stat="vis_team_score">10</td>
                                    <td class="right " data-stat="home_team_score">28</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="center " data-stat="quarter">4</th>
                                    <td class="right " data-stat="time">12:12</td>
                                    <td class="left " data-stat="team">Lions</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a>
                                        12 yard rush (<a href="/players/B/BadgMi00.htm">Michael Badgley</a>
                                        kick)
                                    </td>
                                    <td class="right " data-stat="vis_team_score">10</td>
                                    <td class="right " data-stat="home_team_score">35</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="center iz" data-stat="quarter"></th>
                                    <td class="right " data-stat="time">6:28</td>
                                    <td class="left " data-stat="team">Broncos</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/W/WilsRu00.htm">Russell Wilson</a>
                                        1 yard rush (<a href="/players/L/LutzWi00.htm">Wil Lutz</a>
                                        kick)
                                    </td>
                                    <td class="right " data-stat="vis_team_score">17</td>
                                    <td class="right " data-stat="home_team_score">35</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="center iz" data-stat="quarter"></th>
                                    <td class="right " data-stat="time">2:21</td>
                                    <td class="left " data-stat="team">Lions</td>
                                    <td class="left " data-stat="description">
                                        <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a>
                                        10 yard pass from <a href="/players/G/GoffJa00.htm">Jared Goff</a>
                                        (<a href="/players/B/BadgMi00.htm">Michael Badgley</a>
                                        kick)
                                    </td>
                                    <td class="right " data-stat="vis_team_score">17</td>
                                    <td class="right " data-stat="home_team_score">42</td>
                                </tr>
                        </table>
                    </div>
                </div>
                <div class="content_grid">
                    <div>
                        <div id="all_game_info" class="table_wrapper setup_commented commented">
                            <div class="section_heading assoc_game_info" id="game_info_sh">
                                <span class="section_anchor" id="game_info_link" data-label="Game Info"></span>
                                <h2>Game Info</h2>
                                <div class="section_heading_text">
                                    <ul></ul>
                                </div>
                            </div>
                            <div class="placeholder"></div>
                            <!--

<div class="table_container" id="div_game_info">
    
    <table class="suppress_all sortable stats_table" id="game_info" data-cols-to-freeze="0">
    <caption>Game Info Table</caption>
    <tr class="thead onecell" ><td class="right center" data-stat="onecell" colspan="2" >Game Info</td></tr>
<tr ><th scope="row" class="center " data-stat="info" >Won Toss</th><td class="center " data-stat="stat" >Lions</td></tr>
<tr ><th scope="row" class="center " data-stat="info" >Roof</th><td class="center " data-stat="stat" >dome</td></tr>
<tr ><th scope="row" class="center " data-stat="info" >Surface</th><td class="center " data-stat="stat" >fieldturf</td></tr>
<tr ><th scope="row" class="center " data-stat="info" >Duration</th><td class="center " data-stat="stat" >3:03</td></tr>
<tr ><th scope="row" class="center " data-stat="info" >Attendance</th><td class="center " data-stat="stat" ><a href="/years/2023/attendance.htm">64,500</a></td></tr>
<tr ><th scope="row" class="center " data-stat="info" >Vegas Line</th><td class="center " data-stat="stat" >Detroit Lions -4.5</td></tr>
<tr ><th scope="row" class="center " data-stat="info" >Over/Under</th><td class="center " data-stat="stat" >48.0 <b>(over)</b></td></tr>

</table>


</div>
-->
                        </div>
                    </div>
                    <div>
                        <div id="all_officials" class="table_wrapper setup_commented commented">
                            <div class="section_heading assoc_officials" id="officials_sh">
                                <span class="section_anchor" id="officials_link" data-label="Officials"></span>
                                <h2>Officials</h2>
                                <div class="section_heading_text">
                                    <ul></ul>
                                </div>
                            </div>
                            <div class="placeholder"></div>
                            <!--

<div class="table_container" id="div_officials">
    
    <table class="suppress_all sortable stats_table" id="officials" data-cols-to-freeze="0">
    <caption>Officials Table</caption>
    <tr class="thead onecell" ><td class="right center" data-stat="onecell" colspan="2" >Officials</td></tr>
<tr ><th scope="row" class="center " data-stat="ref_pos" >Referee</th><td class="center " data-stat="name" ><a href="/officials/HussJo0r.htm">John Hussey</a></td></tr>
<tr ><th scope="row" class="center " data-stat="ref_pos" >Umpire</th><td class="center " data-stat="name" ><a href="/officials/PagaCa0r.htm">Carl Paganelli</a></td></tr>
<tr ><th scope="row" class="center " data-stat="ref_pos" >Down Judge</th><td class="center " data-stat="name" ><a href="/officials/LeBlFr0r.htm">Frank LeBlanc</a></td></tr>
<tr ><th scope="row" class="center " data-stat="ref_pos" >Line Judge</th><td class="center " data-stat="name" ><a href="/officials/JohnCa0r.htm">Carl Johnson</a></td></tr>
<tr ><th scope="row" class="center " data-stat="ref_pos" >Back Judge</th><td class="center " data-stat="name" ><a href="/officials/EdwaMa0r.htm">Matt Edwards</a></td></tr>
<tr ><th scope="row" class="center " data-stat="ref_pos" >Side Judge</th><td class="center " data-stat="name" ><a href="/officials/BaynAl0r.htm">Allen Baynes</a></td></tr>
<tr ><th scope="row" class="center " data-stat="ref_pos" >Field Judge</th><td class="center " data-stat="name" ><a href="/officials/FlemAn0r.htm">Anthony Flemming</a></td></tr>

</table>


</div>
-->
                        </div>
                    </div>
                </div>
                <!-- fs_btf_1 -->
                <div class="adblock">
                    <!-- div#fs_fs_btf_1  -->
                    <div align="center" id="div-gpt-ad-728x90-BTF-1" data-freestar-ad="__300x250 __970x90">
                        <script data-cfasync="false" type='text/javascript'>
                            if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {} else {
                                console.log('push ad:div-gpt-ad-728x90-BTF-1');
                                freestar.queue.push(function() {
                                    googletag.display('div-gpt-ad-728x90-BTF-1');
                                });
                            }
                        </script>
                    </div>
                    <!-- /div.#fs_fs_btf_1 -->
                </div>
                <div id="all_expected_points" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_expected_points" id="expected_points_sh">
                        <span class="section_anchor" id="expected_points_link" data-label="Expected Points Summary"></span>
                        <h2>Expected Points Summary</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_expected_points">
    
    <table class="sortable stats_table" id="expected_points" data-cols-to-freeze=",1">
    <caption>Expected Points Summary Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>

      
      <tr class="over_header">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="pbp_exp_points_off" colspan="4" class=" over_header center" >Offense</th>
         <th aria-label="" data-stat="pbp_exp_points_def" colspan="4" class=" over_header center" >Defense</th>
         <th aria-label="" data-stat="pbp_exp_points_st_sum" colspan="6" class=" over_header center" >Special Teams</th>
      </tr>
            
      <tr>
         <th aria-label="Tm" data-stat="team_name" scope="col" class=" poptip sort_default_asc left" >Tm</th>
         <th aria-label="Total" data-stat="pbp_exp_points_tot" scope="col" class=" poptip right" data-tip="Total expected points for the game" >Total</th>
         <th aria-label="Tot" data-stat="pbp_exp_points_off_tot" scope="col" class=" poptip right" data-tip="Total offensive expected points (rushing + passing + penalties)" data-over-header="Offense" >Tot</th>
         <th aria-label="Pass" data-stat="pbp_exp_points_off_pass" scope="col" class=" poptip right" data-tip="Expected points contributed by passing offense" data-over-header="Offense" >Pass</th>
         <th aria-label="Rush" data-stat="pbp_exp_points_off_rush" scope="col" class=" poptip right" data-tip="Expected points contributed by rushing offense" data-over-header="Offense" >Rush</th>
         <th aria-label="TOvr" data-stat="pbp_exp_points_off_to" scope="col" class=" poptip right" data-tip="Expected points contributed by turnovers on offense" data-over-header="Offense" >TOvr</th>
         <th aria-label="Tot" data-stat="pbp_exp_points_def_tot" scope="col" class=" poptip right" data-tip="Total defensive expected points (rushing defense + passing defense + defensive penalties)" data-over-header="Defense" >Tot</th>
         <th aria-label="Pass" data-stat="pbp_exp_points_def_pass" scope="col" class=" poptip right" data-tip="Expected points contributed by passing defense" data-over-header="Defense" >Pass</th>
         <th aria-label="Rush" data-stat="pbp_exp_points_def_rush" scope="col" class=" poptip right" data-tip="Expected points contributed by rushing defense" data-over-header="Defense" >Rush</th>
         <th aria-label="TOvr" data-stat="pbp_exp_points_def_to" scope="col" class=" poptip right" data-tip="Expected points contributed by turnovers recovered on defense" data-over-header="Defense" >TOvr</th>
         <th aria-label="Tot" data-stat="pbp_exp_points_st" scope="col" class=" poptip right" data-tip="All special teams expected points combined" data-over-header="Special Teams" >Tot</th>
         <th aria-label="KO" data-stat="pbp_exp_points_k" scope="col" class=" poptip right" data-tip="Expected points contributed by kickoffs" data-over-header="Special Teams" >KO</th>
         <th aria-label="KR" data-stat="pbp_exp_points_kr" scope="col" class=" poptip right" data-tip="Expected points contributed by kick return teams" data-over-header="Special Teams" >KR</th>
         <th aria-label="P" data-stat="pbp_exp_points_p" scope="col" class=" poptip right" data-tip="Expected points contributed by punt teams" data-over-header="Special Teams" >P</th>
         <th aria-label="PR" data-stat="pbp_exp_points_pr" scope="col" class=" poptip right" data-tip="Expected points contributed by punt return teams" data-over-header="Special Teams" >PR</th>
         <th aria-label="FG/XP" data-stat="pbp_exp_points_fgxp" scope="col" class=" poptip right" data-tip="Expected points contributed by FG & XP kicking and defensive teams" data-over-header="Special Teams" >FG/XP</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-stat="team_name" >Broncos</th><td class="right " data-stat="pbp_exp_points_tot" >-25.00</td><td class="right " data-stat="pbp_exp_points_off_tot" >3.20</td><td class="right " data-stat="pbp_exp_points_off_pass" >5.03</td><td class="right " data-stat="pbp_exp_points_off_rush" >-1.20</td><td class="right " data-stat="pbp_exp_points_off_to" >-6.81</td><td class="right " data-stat="pbp_exp_points_def_tot" >-29.35</td><td class="right " data-stat="pbp_exp_points_def_pass" >-21.35</td><td class="right " data-stat="pbp_exp_points_def_rush" >-8.00</td><td class="right iz" data-stat="pbp_exp_points_def_to" >0.00</td><td class="right " data-stat="pbp_exp_points_st" >3.14</td><td class="right " data-stat="pbp_exp_points_k" >-4.48</td><td class="right " data-stat="pbp_exp_points_kr" >3.73</td><td class="right " data-stat="pbp_exp_points_p" >3.29</td><td class="right " data-stat="pbp_exp_points_pr" >0.61</td><td class="right " data-stat="pbp_exp_points_fgxp" >-0.01</td></tr>
<tr ><th scope="row" class="left " data-stat="team_name" >Lions</th><td class="right " data-stat="pbp_exp_points_tot" >25.00</td><td class="right " data-stat="pbp_exp_points_off_tot" >29.35</td><td class="right " data-stat="pbp_exp_points_off_pass" >21.35</td><td class="right " data-stat="pbp_exp_points_off_rush" >8.00</td><td class="right iz" data-stat="pbp_exp_points_off_to" >0.00</td><td class="right " data-stat="pbp_exp_points_def_tot" >-3.20</td><td class="right " data-stat="pbp_exp_points_def_pass" >-5.03</td><td class="right " data-stat="pbp_exp_points_def_rush" >1.20</td><td class="right " data-stat="pbp_exp_points_def_to" >6.81</td><td class="right " data-stat="pbp_exp_points_st" >-3.14</td><td class="right " data-stat="pbp_exp_points_k" >-3.73</td><td class="right " data-stat="pbp_exp_points_kr" >4.48</td><td class="right " data-stat="pbp_exp_points_p" >-0.61</td><td class="right " data-stat="pbp_exp_points_pr" >-3.29</td><td class="right " data-stat="pbp_exp_points_fgxp" >0.01</td></tr>

</table>


</div>
-->
                </div>
                <div id="all_team_stats" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_team_stats" id="team_stats_sh">
                        <span class="section_anchor" id="team_stats_link" data-label="Team Stats"></span>
                        <h2>Team Stats</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_team_stats">
    
    <table class="add_controls stats_table" id="team_stats" data-cols-to-freeze=",1">
    <caption>Team Stats Table</caption>
    

   <colgroup><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="stat" data-stat="stat" scope="col" class=" poptip center" ></th>
         <th aria-label="DEN" data-stat="vis_stat" scope="col" class=" poptip center" >DEN</th>
         <th aria-label="DET" data-stat="home_stat" scope="col" class=" poptip center" >DET</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="right " data-stat="stat" >First Downs</th><td class="center " data-stat="vis_stat" >20</td><td class="center " data-stat="home_stat" >29</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Rush-Yds-TDs</th><td class="center " data-stat="vis_stat" >28-83-1</td><td class="center " data-stat="home_stat" >28-185-1</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Cmp-Att-Yd-TD-INT</th><td class="center " data-stat="vis_stat" >18-32-223-1-0</td><td class="center " data-stat="home_stat" >24-34-278-5-0</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Sacked-Yards</th><td class="center " data-stat="vis_stat" >2-19</td><td class="center " data-stat="home_stat" >2-15</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Net Pass Yards</th><td class="center " data-stat="vis_stat" >204</td><td class="center " data-stat="home_stat" >263</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Total Yards</th><td class="center " data-stat="vis_stat" >287</td><td class="center " data-stat="home_stat" >448</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Fumbles-Lost</th><td class="center " data-stat="vis_stat" >1-1</td><td class="center " data-stat="home_stat" >0-0</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Turnovers</th><td class="center " data-stat="vis_stat" >1</td><td class="center iz" data-stat="home_stat" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Penalties-Yards</th><td class="center " data-stat="vis_stat" >4-40</td><td class="center " data-stat="home_stat" >2-54</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Third Down Conv.</th><td class="center " data-stat="vis_stat" >5-13</td><td class="center " data-stat="home_stat" >5-10</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Fourth Down Conv.</th><td class="center " data-stat="vis_stat" >2-2</td><td class="center " data-stat="home_stat" >1-1</td></tr>
<tr ><th scope="row" class="right " data-stat="stat" >Time of Possession</th><td class="center " data-stat="vis_stat" >28:42</td><td class="center " data-stat="home_stat" >31:18</td></tr>

</table>


</div>
-->
                </div>
                <!-- fs_btf_2 -->
                <div class="adblock">
                    <!-- div#fs_fs_btf_2  -->
                    <div align="center" id="div-gpt-ad-728x90-BTF-2" data-freestar-ad="__300x250 __970x90">
                        <script data-cfasync="false" type='text/javascript'>
                            if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {} else {
                                console.log('push ad:div-gpt-ad-728x90-BTF-2');
                                freestar.queue.push(function() {
                                    googletag.display('div-gpt-ad-728x90-BTF-2');
                                });
                            }
                        </script>
                    </div>
                    <!-- /div.#fs_fs_btf_2 -->
                </div>
                <div id="all_player_offense" class="table_wrapper">
                    <div class="section_heading assoc_player_offense" id="player_offense_sh">
                        <span class="section_anchor" id="player_offense_link" data-label="Passing, Rushing, & Receiving"></span>
                        <h2>Passing, Rushing, & Receiving</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="table_container" id="div_player_offense">
                        <table class="sortable stats_table" id="player_offense" data-cols-to-freeze=",1">
                            <caption>Passing, Rushing, & Receiving Table</caption>
                            <colgroup>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                                <col>
                            </colgroup>
                            <thead>
                                <tr class="over_header">
                                    <th aria-label="" data-stat="" colspan="2" class=" over_header center"></th>
                                    <th aria-label="" data-stat="header_pass" colspan="9" class=" over_header center">Passing</th>
                                    <th aria-label="" data-stat="header_rush" colspan="4" class=" over_header center">Rushing</th>
                                    <th aria-label="" data-stat="header_rec" colspan="5" class=" over_header center">Receiving</th>
                                    <th aria-label="" data-stat="header_fumbles" colspan="2" class=" over_header center">Fumbles</th>
                                </tr>
                                <tr>
                                    <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left">Player</th>
                                    <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left">Tm</th>
                                    <th aria-label="Passes Completed" data-stat="pass_cmp" scope="col" class=" poptip center" data-tip="Passes completed" data-over-header="Passing">Cmp</th>
                                    <th aria-label="Pass Attempts" data-stat="pass_att" scope="col" class=" poptip center" data-tip="Passes attempted" data-over-header="Passing">Att</th>
                                    <th aria-label="Passing Yds" data-stat="pass_yds" scope="col" class=" poptip center" data-tip="Yards Gained by Passing<br>For teams, sack yardage is deducted from this total" data-over-header="Passing">Yds</th>
                                    <th aria-label="Passing TD" data-stat="pass_td" scope="col" class=" poptip center" data-tip="Passing Touchdowns" data-over-header="Passing">TD</th>
                                    <th aria-label="Passes Intercepted" data-stat="pass_int" scope="col" class=" poptip center" data-tip="Interceptions thrown" data-over-header="Passing">Int</th>
                                    <th aria-label="Sacked " data-stat="pass_sacked" scope="col" class=" poptip center" data-tip="Times Sacked (official since 1969, complete NFL coverage since 1963, partial NFL coverage from 1960-62)" data-over-header="Passing">Sk</th>
                                    <th aria-label="Sacked Yds Lost" data-stat="pass_sacked_yds" scope="col" class=" poptip center" data-tip="Yards lost due to sacks (official since 1969, complete NFL coverage since 1947)" data-over-header="Passing">Yds</th>
                                    <th aria-label="Long Pass" data-stat="pass_long" scope="col" class=" poptip center" data-tip="Longest Completed Pass Thrown (complete since 1975)" data-over-header="Passing">Lng</th>
                                    <th aria-label="Passer Rating" data-stat="pass_rating" scope="col" class=" poptip hide_non_quals center" data-tip="Quarterback Rating, <a href='https://www.pro-football-reference.com/about/glossary.htm'>see glossary</a> for details<br>Different ratings are used by the NFL and NCAA.<br />Minimum 1500 pass attempts to qualify as career leader, minimum 150 pass attempts for playoffs leader." data-over-header="Passing" data-filter="1" data-name="Passer Rating">Rate</th>
                                    <th aria-label="Rushing Att" data-stat="rush_att" scope="col" class=" poptip center" data-tip="Rushing Attempts (sacks not included in NFL)" data-over-header="Rushing">Att</th>
                                    <th aria-label="Rushing Yds" data-stat="rush_yds" scope="col" class=" poptip center" data-tip="Rushing Yards Gained (sack yardage is not included by NFL)" data-over-header="Rushing">Yds</th>
                                    <th aria-label="Rushing TD" data-stat="rush_td" scope="col" class=" poptip center" data-tip="Rushing Touchdowns" data-over-header="Rushing">TD</th>
                                    <th aria-label="Long Rush" data-stat="rush_long" scope="col" class=" poptip center" data-tip="Longest Rushing Attempt" data-over-header="Rushing">Lng</th>
                                    <th aria-label="Targets" data-stat="targets" scope="col" class=" poptip center" data-tip="Pass Targets (since 1992, derived from NFL play-by-play data)" data-over-header="Receiving">Tgt</th>
                                    <th aria-label="Receptions" data-stat="rec" scope="col" class=" poptip center" data-tip="Receptions" data-over-header="Receiving">Rec</th>
                                    <th aria-label="Receiving Yds" data-stat="rec_yds" scope="col" class=" poptip center" data-tip="Receiving Yards" data-over-header="Receiving">Yds</th>
                                    <th aria-label="Receiving TD" data-stat="rec_td" scope="col" class=" poptip center" data-tip="Receiving Touchdowns" data-over-header="Receiving">TD</th>
                                    <th aria-label="Long Reception" data-stat="rec_long" scope="col" class=" poptip center" data-tip="Longest Reception" data-over-header="Receiving">Lng</th>
                                    <th aria-label="Fumbles" data-stat="fumbles" scope="col" class=" poptip center" data-tip="Number of times fumbled both lost and recovered by own team<br />These represent ALL fumbles by the player on offense, defense, and special teams.<br />Available for player games since 1989." data-over-header="Fumbles">Fmb</th>
                                    <th aria-label="Fumbles Lost" data-stat="fumbles_lost" scope="col" class=" poptip center" data-tip="Fumbles Lost by Player (since 1994) or Team" data-over-header="Fumbles">FL</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="WilsRu00" data-stat="player">
                                        <a href="/players/W/WilsRu00.htm">Russell Wilson</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right " data-stat="pass_cmp">18</td>
                                    <td class="right " data-stat="pass_att">32</td>
                                    <td class="right " data-stat="pass_yds">223</td>
                                    <td class="right " data-stat="pass_td">1</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right " data-stat="pass_sacked">2</td>
                                    <td class="right " data-stat="pass_sacked_yds">19</td>
                                    <td class="right " data-stat="pass_long">40</td>
                                    <td class="right " data-stat="pass_rating">88.4</td>
                                    <td class="right " data-stat="rush_att">7</td>
                                    <td class="right " data-stat="rush_yds">6</td>
                                    <td class="right " data-stat="rush_td">1</td>
                                    <td class="right " data-stat="rush_long">2</td>
                                    <td class="right iz" data-stat="targets">0</td>
                                    <td class="right iz" data-stat="rec">0</td>
                                    <td class="right iz" data-stat="rec_yds">0</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right iz" data-stat="rec_long">0</td>
                                    <td class="right " data-stat="fumbles">1</td>
                                    <td class="right " data-stat="fumbles_lost">1</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="PeriSa00" data-stat="player">
                                        <a href="/players/P/PeriSa00.htm">Samaje Perine</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right " data-stat="rush_att">6</td>
                                    <td class="right " data-stat="rush_yds">37</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right " data-stat="rush_long">12</td>
                                    <td class="right " data-stat="targets">1</td>
                                    <td class="right " data-stat="rec">1</td>
                                    <td class="right " data-stat="rec_yds">11</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">11</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="WillJa10" data-stat="player">
                                        <a href="/players/W/WillJa10.htm">Javonte Williams</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right " data-stat="rush_att">12</td>
                                    <td class="right " data-stat="rush_yds">27</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right " data-stat="rush_long">8</td>
                                    <td class="right " data-stat="targets">2</td>
                                    <td class="right " data-stat="rec">2</td>
                                    <td class="right " data-stat="rec_yds">-7</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">-2</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="MimsMa00" data-stat="player">
                                        <a href="/players/M/MimsMa00.htm">Marvin Mims</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right " data-stat="rush_att">1</td>
                                    <td class="right " data-stat="rush_yds">11</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right " data-stat="rush_long">11</td>
                                    <td class="right " data-stat="targets">2</td>
                                    <td class="right iz" data-stat="rec">0</td>
                                    <td class="right iz" data-stat="rec_yds">0</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right iz" data-stat="rec_long">0</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="McLaJa00" data-stat="player">
                                        <a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right " data-stat="rush_att">2</td>
                                    <td class="right " data-stat="rush_yds">2</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right " data-stat="rush_long">1</td>
                                    <td class="right " data-stat="targets">3</td>
                                    <td class="right " data-stat="rec">2</td>
                                    <td class="right " data-stat="rec_yds">16</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">8</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="JeudJe00" data-stat="player">
                                        <a href="/players/J/JeudJe00.htm">Jerry Jeudy</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">7</td>
                                    <td class="right " data-stat="rec">3</td>
                                    <td class="right " data-stat="rec_yds">74</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">40</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="SuttCo00" data-stat="player">
                                        <a href="/players/S/SuttCo00.htm">Courtland Sutton</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">6</td>
                                    <td class="right " data-stat="rec">5</td>
                                    <td class="right " data-stat="rec_yds">71</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">23</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="TrauAd00" data-stat="player">
                                        <a href="/players/T/TrauAd00.htm">Adam Trautman</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">3</td>
                                    <td class="right " data-stat="rec">1</td>
                                    <td class="right " data-stat="rec_yds">24</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">24</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="KrulLu00" data-stat="player">
                                        <a href="/players/K/KrulLu00.htm">Lucas Krull</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">3</td>
                                    <td class="right " data-stat="rec">1</td>
                                    <td class="right " data-stat="rec_yds">18</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">18</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="HumpLi01" data-stat="player">
                                        <a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">4</td>
                                    <td class="right " data-stat="rec">3</td>
                                    <td class="right " data-stat="rec_yds">16</td>
                                    <td class="right " data-stat="rec_td">1</td>
                                    <td class="right " data-stat="rec_long">8</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="JohnBr23" data-stat="player">
                                        <a href="/players/J/JohnBr23.htm">Brandon Johnson</a>
                                    </th>
                                    <td class="left " data-stat="team">DEN</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">1</td>
                                    <td class="right iz" data-stat="rec">0</td>
                                    <td class="right iz" data-stat="rec_yds">0</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right iz" data-stat="rec_long">0</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr class="over_header thead">
                                    <th aria-label="" data-stat="" colspan="2" class=" over_header center"></th>
                                    <th aria-label="" data-stat="header_pass" colspan="9" class=" over_header center">Passing</th>
                                    <th aria-label="" data-stat="header_rush" colspan="4" class=" over_header center">Rushing</th>
                                    <th aria-label="" data-stat="header_rec" colspan="5" class=" over_header center">Receiving</th>
                                    <th aria-label="" data-stat="header_fumbles" colspan="2" class=" over_header center">Fumbles</th>
                                </tr>
                                <tr class="thead">
                                    <th aria-label="Player" data-stat="player" class=" sort_default_asc show_partial_when_sorting left">Player</th>
                                    <th aria-label="Tm" data-stat="team" class=" sort_default_asc show_partial_when_sorting left">Tm</th>
                                    <th aria-label="Passes Completed" data-stat="pass_cmp" class=" center" data-tip="Passes completed" data-over-header="Passing">Cmp</th>
                                    <th aria-label="Pass Attempts" data-stat="pass_att" class=" center" data-tip="Passes attempted" data-over-header="Passing">Att</th>
                                    <th aria-label="Passing Yds" data-stat="pass_yds" class=" center" data-tip="Yards Gained by Passing<br>For teams, sack yardage is deducted from this total" data-over-header="Passing">Yds</th>
                                    <th aria-label="Passing TD" data-stat="pass_td" class=" center" data-tip="Passing Touchdowns" data-over-header="Passing">TD</th>
                                    <th aria-label="Passes Intercepted" data-stat="pass_int" class=" center" data-tip="Interceptions thrown" data-over-header="Passing">Int</th>
                                    <th aria-label="Sacked " data-stat="pass_sacked" class=" center" data-tip="Times Sacked (official since 1969, complete NFL coverage since 1963, partial NFL coverage from 1960-62)" data-over-header="Passing">Sk</th>
                                    <th aria-label="Sacked Yds Lost" data-stat="pass_sacked_yds" class=" center" data-tip="Yards lost due to sacks (official since 1969, complete NFL coverage since 1947)" data-over-header="Passing">Yds</th>
                                    <th aria-label="Long Pass" data-stat="pass_long" class=" center" data-tip="Longest Completed Pass Thrown (complete since 1975)" data-over-header="Passing">Lng</th>
                                    <th aria-label="Passer Rating" data-stat="pass_rating" class=" hide_non_quals center" data-tip="Quarterback Rating, <a href='https://www.pro-football-reference.com/about/glossary.htm'>see glossary</a> for details<br>Different ratings are used by the NFL and NCAA.<br />Minimum 1500 pass attempts to qualify as career leader, minimum 150 pass attempts for playoffs leader." data-over-header="Passing" data-filter="1" data-name="Passer Rating">Rate</th>
                                    <th aria-label="Rushing Att" data-stat="rush_att" class=" center" data-tip="Rushing Attempts (sacks not included in NFL)" data-over-header="Rushing">Att</th>
                                    <th aria-label="Rushing Yds" data-stat="rush_yds" class=" center" data-tip="Rushing Yards Gained (sack yardage is not included by NFL)" data-over-header="Rushing">Yds</th>
                                    <th aria-label="Rushing TD" data-stat="rush_td" class=" center" data-tip="Rushing Touchdowns" data-over-header="Rushing">TD</th>
                                    <th aria-label="Long Rush" data-stat="rush_long" class=" center" data-tip="Longest Rushing Attempt" data-over-header="Rushing">Lng</th>
                                    <th aria-label="Targets" data-stat="targets" class=" center" data-tip="Pass Targets (since 1992, derived from NFL play-by-play data)" data-over-header="Receiving">Tgt</th>
                                    <th aria-label="Receptions" data-stat="rec" class=" center" data-tip="Receptions" data-over-header="Receiving">Rec</th>
                                    <th aria-label="Receiving Yds" data-stat="rec_yds" class=" center" data-tip="Receiving Yards" data-over-header="Receiving">Yds</th>
                                    <th aria-label="Receiving TD" data-stat="rec_td" class=" center" data-tip="Receiving Touchdowns" data-over-header="Receiving">TD</th>
                                    <th aria-label="Long Reception" data-stat="rec_long" class=" center" data-tip="Longest Reception" data-over-header="Receiving">Lng</th>
                                    <th aria-label="Fumbles" data-stat="fumbles" class=" center" data-tip="Number of times fumbled both lost and recovered by own team<br />These represent ALL fumbles by the player on offense, defense, and special teams.<br />Available for player games since 1989." data-over-header="Fumbles">Fmb</th>
                                    <th aria-label="Fumbles Lost" data-stat="fumbles_lost" class=" center" data-tip="Fumbles Lost by Player (since 1994) or Team" data-over-header="Fumbles">FL</th>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="GoffJa00" data-stat="player">
                                        <a href="/players/G/GoffJa00.htm">Jared Goff</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right " data-stat="pass_cmp">24</td>
                                    <td class="right " data-stat="pass_att">34</td>
                                    <td class="right " data-stat="pass_yds">278</td>
                                    <td class="right " data-stat="pass_td">5</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right " data-stat="pass_sacked">2</td>
                                    <td class="right " data-stat="pass_sacked_yds">15</td>
                                    <td class="right " data-stat="pass_long">29</td>
                                    <td class="right " data-stat="pass_rating">134.6</td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right iz" data-stat="targets">0</td>
                                    <td class="right iz" data-stat="rec">0</td>
                                    <td class="right iz" data-stat="rec_yds">0</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right iz" data-stat="rec_long">0</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="GibbJa01" data-stat="player">
                                        <a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right " data-stat="rush_att">11</td>
                                    <td class="right " data-stat="rush_yds">100</td>
                                    <td class="right " data-stat="rush_td">1</td>
                                    <td class="right " data-stat="rush_long">34</td>
                                    <td class="right " data-stat="targets">2</td>
                                    <td class="right " data-stat="rec">2</td>
                                    <td class="right " data-stat="rec_yds">8</td>
                                    <td class="right " data-stat="rec_td">1</td>
                                    <td class="right " data-stat="rec_long">9</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="MontDa01" data-stat="player">
                                        <a href="/players/M/MontDa01.htm">David Montgomery</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right " data-stat="rush_att">17</td>
                                    <td class="right " data-stat="rush_yds">85</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right " data-stat="rush_long">13</td>
                                    <td class="right " data-stat="targets">3</td>
                                    <td class="right " data-stat="rec">2</td>
                                    <td class="right " data-stat="rec_yds">-3</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">4</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="StxxAm00" data-stat="player">
                                        <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">9</td>
                                    <td class="right " data-stat="rec">7</td>
                                    <td class="right " data-stat="rec_yds">112</td>
                                    <td class="right " data-stat="rec_td">1</td>
                                    <td class="right " data-stat="rec_long">29</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="LaPoSa01" data-stat="player">
                                        <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">6</td>
                                    <td class="right " data-stat="rec">5</td>
                                    <td class="right " data-stat="rec_yds">56</td>
                                    <td class="right " data-stat="rec_td">3</td>
                                    <td class="right " data-stat="rec_long">19</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="WillJa11" data-stat="player">
                                        <a href="/players/W/WillJa11.htm">Jameson Williams</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">7</td>
                                    <td class="right " data-stat="rec">4</td>
                                    <td class="right " data-stat="rec_yds">47</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">18</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="ReynJo00" data-stat="player">
                                        <a href="/players/R/ReynJo00.htm">Josh Reynolds</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">3</td>
                                    <td class="right " data-stat="rec">2</td>
                                    <td class="right " data-stat="rec_yds">41</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">21</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="RaymKa00" data-stat="player">
                                        <a href="/players/R/RaymKa00.htm">Kalif Raymond</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">1</td>
                                    <td class="right " data-stat="rec">1</td>
                                    <td class="right " data-stat="rec_yds">12</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">12</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="left " data-append-csv="PeopDo00" data-stat="player">
                                        <a href="/players/P/PeopDo00.htm">Donovan Peoples-Jones</a>
                                    </th>
                                    <td class="left " data-stat="team">DET</td>
                                    <td class="right iz" data-stat="pass_cmp">0</td>
                                    <td class="right iz" data-stat="pass_att">0</td>
                                    <td class="right iz" data-stat="pass_yds">0</td>
                                    <td class="right iz" data-stat="pass_td">0</td>
                                    <td class="right iz" data-stat="pass_int">0</td>
                                    <td class="right iz" data-stat="pass_sacked">0</td>
                                    <td class="right iz" data-stat="pass_sacked_yds">0</td>
                                    <td class="right iz" data-stat="pass_long">0</td>
                                    <td class="right iz" data-stat="pass_rating"></td>
                                    <td class="right iz" data-stat="rush_att">0</td>
                                    <td class="right iz" data-stat="rush_yds">0</td>
                                    <td class="right iz" data-stat="rush_td">0</td>
                                    <td class="right iz" data-stat="rush_long">0</td>
                                    <td class="right " data-stat="targets">1</td>
                                    <td class="right " data-stat="rec">1</td>
                                    <td class="right " data-stat="rec_yds">5</td>
                                    <td class="right iz" data-stat="rec_td">0</td>
                                    <td class="right " data-stat="rec_long">5</td>
                                    <td class="right iz" data-stat="fumbles">0</td>
                                    <td class="right iz" data-stat="fumbles_lost">0</td>
                                </tr>
                        </table>
                    </div>
                </div>
                <div id="all_player_defense" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_player_defense" id="player_defense_sh">
                        <span class="section_anchor" id="player_defense_link" data-label="Defense"></span>
                        <h2>Defense</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_player_defense">
    
    <table class="sortable stats_table shade_zero" id="player_defense" data-cols-to-freeze=",1">
    <caption>Defense Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>

      
      <tr class="over_header">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="header_def_int" colspan="5" class=" over_header center" >Def Interceptions</th><th></th>
         <th aria-label="" data-stat="header_other_defense" colspan="5" class=" over_header center" >Tackles</th>
         <th aria-label="" data-stat="header_fumbles" colspan="4" class=" over_header center" >Fumbles</th>
      </tr>
            
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Interceptions" data-stat="def_int" scope="col" class=" poptip center" data-tip="Passes intercepted on defense" data-over-header="Def Interceptions" >Int</th>
         <th aria-label="Intercept. Ret. Yds" data-stat="def_int_yds" scope="col" class=" poptip center" data-tip="Yards interceptions were returned" data-over-header="Def Interceptions" >Yds</th>
         <th aria-label="Intercept. Ret. TD" data-stat="def_int_td" scope="col" class=" poptip center" data-tip="Interceptions returned for touchdowns" data-over-header="Def Interceptions" >TD</th>
         <th aria-label="Long Intercep. Return" data-stat="def_int_long" scope="col" class=" poptip center" data-tip="longest interception return" data-over-header="Def Interceptions" >Lng</th>
         <th aria-label="Passes Defended" data-stat="pass_defended" scope="col" class=" poptip center" data-tip="Passes defended by a defensive player, since 1999" data-over-header="Def Interceptions" >PD</th>
         <th aria-label="Sacks" data-stat="sacks" scope="col" class=" poptip center" data-tip="Sacks (official since 1982,<br />based on play-by-play, game film<br />and other research since 1960)" data-filter="1" data-name="Sacks" >Sk</th>
         <th aria-label="Tackles Combined" data-stat="tackles_combined" scope="col" class=" poptip center" data-tip="Tackles<br>Combined solo + assisted tackles<br />Prior to 1994, all tackles are put into 'combined', though<br />they are unofficial and inconsistently recorded from team to team. For amusement only." data-over-header="Tackles" >Comb</th>
         <th aria-label="Tackles Solo" data-stat="tackles_solo" scope="col" class=" poptip center" data-tip="Tackles<br>Before 1994: unofficial and inconsistently recorded from team to team. For amusement only.<br>1994-now: unofficial but consistently recorded.<br>" data-over-header="Tackles" >Solo</th>
         <th aria-label="Assists" data-stat="tackles_assists" scope="col" class=" poptip center" data-tip="Assists on tackles<br>Before 1994: combined with solo tackles<br>1994-now: unofficial, but consistently recorded<br>" data-over-header="Tackles" >Ast</th>
         <th aria-label="Tackles For Loss" data-stat="tackles_loss" scope="col" class=" poptip center" data-tip="Tackles For Loss, recorded for 95% of games from 1999-2007 and 100% since 2008" data-over-header="Tackles" >TFL</th>
         <th aria-label="QB Hits" data-stat="qb_hits" scope="col" class=" poptip center" data-tip="Quarterback hits, recorded since 2006" data-over-header="Tackles" >QBHits</th>
         <th aria-label="Fumbles Recovered" data-stat="fumbles_rec" scope="col" class=" poptip center" data-tip="Fumbles recovered by a Player or Team<br>Original fumble by either team" data-over-header="Fumbles" >FR</th>
         <th aria-label="Fumble Return Yds" data-stat="fumbles_rec_yds" scope="col" class=" poptip center" data-tip="Yards recovered fumbles were returned" data-over-header="Fumbles" >Yds</th>
         <th aria-label="Fumble Return TD" data-stat="fumbles_rec_td" scope="col" class=" poptip center" data-tip="Fumbles recovered resulting in a touchdown for the recoverer" data-over-header="Fumbles" >TD</th>
         <th aria-label="Fumbles Forced" data-stat="fumbles_forced" scope="col" class=" poptip center" data-tip="Number of times forced a fumble by the opposition recovered by either team" data-over-header="Fumbles" >FF</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="CoopJo02" data-stat="player" ><a href="/players/C/CoopJo02.htm">Jonathon Cooper</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right " data-stat="sacks" >1.0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_solo" >5</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right " data-stat="tackles_loss" >1</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoneD.01" data-stat="player" ><a href="/players/J/JoneD.01.htm">D.J. Jones</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right " data-stat="sacks" >1.0</td><td class="right " data-stat="tackles_combined" >4</td><td class="right " data-stat="tackles_solo" >3</td><td class="right " data-stat="tackles_assists" >1</td><td class="right " data-stat="tackles_loss" >2</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JeweJo00" data-stat="player" ><a href="/players/J/JeweJo00.htm">Josey Jewell</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >9</td><td class="right " data-stat="tackles_solo" >7</td><td class="right " data-stat="tackles_assists" >2</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MoreFa00" data-stat="player" ><a href="/players/M/MoreFa00.htm">Fabian Moreau</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >8</td><td class="right " data-stat="tackles_solo" >7</td><td class="right " data-stat="tackles_assists" >1</td><td class="right " data-stat="tackles_loss" >1</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HarrJo05" data-stat="player" ><a href="/players/H/HarrJo05.htm">Jonathan Harris</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_solo" >3</td><td class="right " data-stat="tackles_assists" >2</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SimmJu00" data-stat="player" ><a href="/players/S/SimmJu00.htm">Justin Simmons</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_solo" >4</td><td class="right " data-stat="tackles_assists" >1</td><td class="right " data-stat="tackles_loss" >1</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SingAl00" data-stat="player" ><a href="/players/S/SingAl00.htm">Alex Singleton</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_solo" >3</td><td class="right " data-stat="tackles_assists" >2</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LockPJ00" data-stat="player" ><a href="/players/L/LockPJ00.htm">P.J. Locke</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >4</td><td class="right " data-stat="tackles_solo" >3</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McMiJa00" data-stat="player" ><a href="/players/M/McMiJa00.htm">Ja'Quan McMillian</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_solo" >2</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PurcMi00" data-stat="player" ><a href="/players/P/PurcMi00.htm">Mike Purcell</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_solo" >1</td><td class="right " data-stat="tackles_assists" >2</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SurtPa01" data-stat="player" ><a href="/players/S/SurtPa01.htm">Patrick Surtain II</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_solo" >2</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BrowBa01" data-stat="player" ><a href="/players/B/BrowBa01.htm">Baron Browning</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_solo" >1</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HennMa01" data-stat="player" ><a href="/players/H/HennMa01.htm">Matt Henningsen</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_solo" >1</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BurtMi00" data-stat="player" ><a href="/players/B/BurtMi00.htm">Michael Burton</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right " data-stat="tackles_solo" >1</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="IncoTh00" data-stat="player" ><a href="/players/I/IncoTh00.htm">Thomas Incoom</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right iz" data-stat="tackles_solo" >0</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MossRi00" data-stat="player" ><a href="/players/M/MossRi00.htm">Riley Moss</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right " data-stat="tackles_solo" >1</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SandDr00" data-stat="player" ><a href="/players/S/SandDr00.htm">Drew Sanders</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right iz" data-stat="tackles_solo" >0</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SmitTr04" data-stat="player" ><a href="/players/S/SmitTr04.htm">Tremon Smith</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right " data-stat="tackles_solo" >1</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AlleZa01" data-stat="player" ><a href="/players/A/AlleZa01.htm">Zach Allen</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="tackles_combined" >0</td><td class="right iz" data-stat="tackles_solo" >0</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>



      
      <tr class="over_header thead">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="header_def_int" colspan="5" class=" over_header center" >Def Interceptions</th><th></th>
         <th aria-label="" data-stat="header_other_defense" colspan="5" class=" over_header center" >Tackles</th>
         <th aria-label="" data-stat="header_fumbles" colspan="4" class=" over_header center" >Fumbles</th>
      </tr>
            
      <tr class="thead">
         <th aria-label="Player" data-stat="player" class=" sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" class=" sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Interceptions" data-stat="def_int" class=" center" data-tip="Passes intercepted on defense" data-over-header="Def Interceptions" >Int</th>
         <th aria-label="Intercept. Ret. Yds" data-stat="def_int_yds" class=" center" data-tip="Yards interceptions were returned" data-over-header="Def Interceptions" >Yds</th>
         <th aria-label="Intercept. Ret. TD" data-stat="def_int_td" class=" center" data-tip="Interceptions returned for touchdowns" data-over-header="Def Interceptions" >TD</th>
         <th aria-label="Long Intercep. Return" data-stat="def_int_long" class=" center" data-tip="longest interception return" data-over-header="Def Interceptions" >Lng</th>
         <th aria-label="Passes Defended" data-stat="pass_defended" class=" center" data-tip="Passes defended by a defensive player, since 1999" data-over-header="Def Interceptions" >PD</th>
         <th aria-label="Sacks" data-stat="sacks" class=" center" data-tip="Sacks (official since 1982,<br />based on play-by-play, game film<br />and other research since 1960)" data-filter="1" data-name="Sacks" >Sk</th>
         <th aria-label="Tackles Combined" data-stat="tackles_combined" class=" center" data-tip="Tackles<br>Combined solo + assisted tackles<br />Prior to 1994, all tackles are put into 'combined', though<br />they are unofficial and inconsistently recorded from team to team. For amusement only." data-over-header="Tackles" >Comb</th>
         <th aria-label="Tackles Solo" data-stat="tackles_solo" class=" center" data-tip="Tackles<br>Before 1994: unofficial and inconsistently recorded from team to team. For amusement only.<br>1994-now: unofficial but consistently recorded.<br>" data-over-header="Tackles" >Solo</th>
         <th aria-label="Assists" data-stat="tackles_assists" class=" center" data-tip="Assists on tackles<br>Before 1994: combined with solo tackles<br>1994-now: unofficial, but consistently recorded<br>" data-over-header="Tackles" >Ast</th>
         <th aria-label="Tackles For Loss" data-stat="tackles_loss" class=" center" data-tip="Tackles For Loss, recorded for 95% of games from 1999-2007 and 100% since 2008" data-over-header="Tackles" >TFL</th>
         <th aria-label="QB Hits" data-stat="qb_hits" class=" center" data-tip="Quarterback hits, recorded since 2006" data-over-header="Tackles" >QBHits</th>
         <th aria-label="Fumbles Recovered" data-stat="fumbles_rec" class=" center" data-tip="Fumbles recovered by a Player or Team<br>Original fumble by either team" data-over-header="Fumbles" >FR</th>
         <th aria-label="Fumble Return Yds" data-stat="fumbles_rec_yds" class=" center" data-tip="Yards recovered fumbles were returned" data-over-header="Fumbles" >Yds</th>
         <th aria-label="Fumble Return TD" data-stat="fumbles_rec_td" class=" center" data-tip="Fumbles recovered resulting in a touchdown for the recoverer" data-over-header="Fumbles" >TD</th>
         <th aria-label="Fumbles Forced" data-stat="fumbles_forced" class=" center" data-tip="Number of times forced a fumble by the opposition recovered by either team" data-over-header="Fumbles" >FF</th>
      </tr>
      <tr ><th scope="row" class="left " data-append-csv="MeliIf00" data-stat="player" ><a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >2</td><td class="right " data-stat="sacks" >1.0</td><td class="right " data-stat="tackles_combined" >9</td><td class="right " data-stat="tackles_solo" >6</td><td class="right " data-stat="tackles_assists" >3</td><td class="right " data-stat="tackles_loss" >1</td><td class="right " data-stat="qb_hits" >2</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right " data-stat="fumbles_forced" >1</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PascJo00" data-stat="player" ><a href="/players/P/PascJo00.htm">Josh Paschal</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right " data-stat="sacks" >1.0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_solo" >2</td><td class="right " data-stat="tackles_assists" >1</td><td class="right " data-stat="tackles_loss" >2</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AnzaAl00" data-stat="player" ><a href="/players/A/AnzaAl00.htm">Alex Anzalone</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >12</td><td class="right " data-stat="tackles_solo" >7</td><td class="right " data-stat="tackles_assists" >5</td><td class="right " data-stat="tackles_loss" >1</td><td class="right " data-stat="qb_hits" >2</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="CampJa04" data-stat="player" ><a href="/players/C/CampJa04.htm">Jack Campbell</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_solo" >1</td><td class="right " data-stat="tackles_assists" >4</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ComiJo00" data-stat="player" ><a href="/players/C/ComiJo00.htm">John Cominsky</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_solo" >1</td><td class="right " data-stat="tackles_assists" >4</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HutcAi00" data-stat="player" ><a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >4</td><td class="right " data-stat="tackles_solo" >3</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoseKe03" data-stat="player" ><a href="/players/J/JoseKe03.htm">Kerby Joseph</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >4</td><td class="right " data-stat="tackles_solo" >3</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BarnDe02" data-stat="player" ><a href="/players/B/BarnDe02.htm">Derrick Barnes</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_solo" >3</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="DorsKh00" data-stat="player" ><a href="/players/D/DorsKh00.htm">Khalil Dorsey</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_solo" >2</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SuttCa00" data-stat="player" ><a href="/players/S/SuttCa00.htm">Cameron Sutton</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_solo" >2</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BranBr00" data-stat="player" ><a href="/players/B/BranBr00.htm">Brian Branch</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_solo" >1</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BuggIs00" data-stat="player" ><a href="/players/B/BuggIs00.htm">Isaiah Buggs</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_solo" >1</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right " data-stat="fumbles_rec" >1</td><td class="right " data-stat="fumbles_rec_yds" >33</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MartBr00" data-stat="player" ><a href="/players/M/MartBr00.htm">Brodric Martin</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right iz" data-stat="tackles_solo" >0</td><td class="right " data-stat="tackles_assists" >2</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ReevJa00" data-stat="player" ><a href="/players/R/ReevJa00.htm">Jalen Reeves-Maybin</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_solo" >1</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoneBe03" data-stat="player" ><a href="/players/J/JoneBe03.htm">Benito Jones</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right iz" data-stat="tackles_solo" >0</td><td class="right " data-stat="tackles_assists" >1</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="OnwuLe00" data-stat="player" ><a href="/players/O/OnwuLe00.htm">Levi Onwuzurike</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right " data-stat="tackles_solo" >1</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="RodrMa00" data-stat="player" ><a href="/players/R/RodrMa00.htm">Malcolm Rodriguez</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right iz" data-stat="pass_defended" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right " data-stat="tackles_solo" >1</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right iz" data-stat="qb_hits" >0</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="VildKi00" data-stat="player" ><a href="/players/V/VildKi00.htm">Kindle Vildor</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_int_yds" >0</td><td class="right iz" data-stat="def_int_td" >0</td><td class="right iz" data-stat="def_int_long" >0</td><td class="right " data-stat="pass_defended" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="tackles_combined" >0</td><td class="right iz" data-stat="tackles_solo" >0</td><td class="right iz" data-stat="tackles_assists" >0</td><td class="right iz" data-stat="tackles_loss" >0</td><td class="right " data-stat="qb_hits" >1</td><td class="right iz" data-stat="fumbles_rec" >0</td><td class="right iz" data-stat="fumbles_rec_yds" >0</td><td class="right iz" data-stat="fumbles_rec_td" >0</td><td class="right iz" data-stat="fumbles_forced" >0</td></tr>

</table>


</div>
-->
                </div>
                <div id="all_returns" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_returns" id="returns_sh">
                        <span class="section_anchor" id="returns_link" data-label="Kick/Punt Returns"></span>
                        <h2>Kick/Punt Returns</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_returns">
    
    <table class="sortable stats_table" id="returns" data-cols-to-freeze=",1">
    <caption>Kick/Punt Returns Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>

      
      <tr class="over_header">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="header_kr" colspan="5" class=" over_header center" >Kick Returns</th>
         <th aria-label="" data-stat="header_pr" colspan="5" class=" over_header center" >Punt Returns</th>
      </tr>
            
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Kick Returns" data-stat="kick_ret" scope="col" class=" poptip center" data-tip="Kickoff Returns" data-over-header="Kick Returns" >Rt</th>
         <th aria-label="Kick Return Yds" data-stat="kick_ret_yds" scope="col" class=" poptip center" data-tip="Yardage for Kickoffs Returned" data-over-header="Kick Returns" >Yds</th>
         <th aria-label="Yds/Kick Return" data-stat="kick_ret_yds_per_ret" scope="col" class=" poptip hide_non_quals center" data-tip="Yards per Kickoff Return - Kick Return Yardage/Kickoff Returns<br />Minimum one return per game scheduled to qualify as leader.<br />Minimum 75 kick returns to qualify as career leader" data-over-header="Kick Returns" data-filter="1" data-name="Yds/Kick Return" >Y/Rt</th>
         <th aria-label="Kick Return TD" data-stat="kick_ret_td" scope="col" class=" poptip center" data-tip="Kickoffs Returned for a touchdown" data-over-header="Kick Returns" >TD</th>
         <th aria-label="Long Kick Return" data-stat="kick_ret_long" scope="col" class=" poptip center" data-tip="Longest Kickoff Return" data-over-header="Kick Returns" >Lng</th>
         <th aria-label="Punt Returns" data-stat="punt_ret" scope="col" class=" poptip center" data-tip="Punts Returned" data-over-header="Punt Returns" >Ret</th>
         <th aria-label="Punt Return Yds" data-stat="punt_ret_yds" scope="col" class=" poptip center" data-tip="Punts Return Yardage" data-over-header="Punt Returns" >Yds</th>
         <th aria-label="Yds/Punt Return" data-stat="punt_ret_yds_per_ret" scope="col" class=" poptip hide_non_quals center" data-tip="<b>Yards per Punt Return</b><br>Minimum 1.25 returns per game scheduled to qualify as leader.<br>Minimum 75 punt returns to qualify as career leader." data-over-header="Punt Returns" data-filter="1" data-name="Yds/Punt Return" >Y/R</th>
         <th aria-label="Punt Return TD" data-stat="punt_ret_td" scope="col" class=" poptip center" data-tip="Punts Returned for Touchdown" data-over-header="Punt Returns" >TD</th>
         <th aria-label="Long Punt Return" data-stat="punt_ret_long" scope="col" class=" poptip center" data-tip="Longest Punt Return" data-over-header="Punt Returns" >Lng</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="MimsMa00" data-stat="player" ><a href="/players/M/MimsMa00.htm">Marvin Mims</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="kick_ret" >2</td><td class="right " data-stat="kick_ret_yds" >35</td><td class="right " data-stat="kick_ret_yds_per_ret" >17.5</td><td class="right iz" data-stat="kick_ret_td" >0</td><td class="right " data-stat="kick_ret_long" >20</td><td class="right iz" data-stat="punt_ret" >0</td><td class="right iz" data-stat="punt_ret_yds" >0</td><td class="right iz" data-stat="punt_ret_yds_per_ret" ></td><td class="right iz" data-stat="punt_ret_td" >0</td><td class="right iz" data-stat="punt_ret_long" >0</td></tr>



      
      <tr class="over_header thead">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="header_kr" colspan="5" class=" over_header center" >Kick Returns</th>
         <th aria-label="" data-stat="header_pr" colspan="5" class=" over_header center" >Punt Returns</th>
      </tr>
            
      <tr class="thead">
         <th aria-label="Player" data-stat="player" class=" sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" class=" sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Kick Returns" data-stat="kick_ret" class=" center" data-tip="Kickoff Returns" data-over-header="Kick Returns" >Rt</th>
         <th aria-label="Kick Return Yds" data-stat="kick_ret_yds" class=" center" data-tip="Yardage for Kickoffs Returned" data-over-header="Kick Returns" >Yds</th>
         <th aria-label="Yds/Kick Return" data-stat="kick_ret_yds_per_ret" class=" hide_non_quals center" data-tip="Yards per Kickoff Return - Kick Return Yardage/Kickoff Returns<br />Minimum one return per game scheduled to qualify as leader.<br />Minimum 75 kick returns to qualify as career leader" data-over-header="Kick Returns" data-filter="1" data-name="Yds/Kick Return" >Y/Rt</th>
         <th aria-label="Kick Return TD" data-stat="kick_ret_td" class=" center" data-tip="Kickoffs Returned for a touchdown" data-over-header="Kick Returns" >TD</th>
         <th aria-label="Long Kick Return" data-stat="kick_ret_long" class=" center" data-tip="Longest Kickoff Return" data-over-header="Kick Returns" >Lng</th>
         <th aria-label="Punt Returns" data-stat="punt_ret" class=" center" data-tip="Punts Returned" data-over-header="Punt Returns" >Ret</th>
         <th aria-label="Punt Return Yds" data-stat="punt_ret_yds" class=" center" data-tip="Punts Return Yardage" data-over-header="Punt Returns" >Yds</th>
         <th aria-label="Yds/Punt Return" data-stat="punt_ret_yds_per_ret" class=" hide_non_quals center" data-tip="<b>Yards per Punt Return</b><br>Minimum 1.25 returns per game scheduled to qualify as leader.<br>Minimum 75 punt returns to qualify as career leader." data-over-header="Punt Returns" data-filter="1" data-name="Yds/Punt Return" >Y/R</th>
         <th aria-label="Punt Return TD" data-stat="punt_ret_td" class=" center" data-tip="Punts Returned for Touchdown" data-over-header="Punt Returns" >TD</th>
         <th aria-label="Long Punt Return" data-stat="punt_ret_long" class=" center" data-tip="Longest Punt Return" data-over-header="Punt Returns" >Lng</th>
      </tr>
      <tr ><th scope="row" class="left " data-append-csv="RaymKa00" data-stat="player" ><a href="/players/R/RaymKa00.htm">Kalif Raymond</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="kick_ret" >0</td><td class="right iz" data-stat="kick_ret_yds" >0</td><td class="right iz" data-stat="kick_ret_yds_per_ret" ></td><td class="right iz" data-stat="kick_ret_td" >0</td><td class="right iz" data-stat="kick_ret_long" >0</td><td class="right " data-stat="punt_ret" >2</td><td class="right " data-stat="punt_ret_yds" >8</td><td class="right " data-stat="punt_ret_yds_per_ret" >4.0</td><td class="right iz" data-stat="punt_ret_td" >0</td><td class="right " data-stat="punt_ret_long" >8</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ReynCr00" data-stat="player" ><a href="/players/R/ReynCr00.htm">Craig Reynolds</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="kick_ret" >1</td><td class="right " data-stat="kick_ret_yds" >26</td><td class="right " data-stat="kick_ret_yds_per_ret" >26.0</td><td class="right iz" data-stat="kick_ret_td" >0</td><td class="right " data-stat="kick_ret_long" >26</td><td class="right iz" data-stat="punt_ret" >0</td><td class="right iz" data-stat="punt_ret_yds" >0</td><td class="right iz" data-stat="punt_ret_yds_per_ret" ></td><td class="right iz" data-stat="punt_ret_td" >0</td><td class="right iz" data-stat="punt_ret_long" >0</td></tr>

</table>


</div>
-->
                </div>
                <!-- fs_btf_3 -->
                <div class="adblock">
                    <!-- div#fs_fs_btf_3  -->
                    <div align="center" id="div-gpt-ad-728x90-BTF-3" data-freestar-ad="__300x250 __970x90">
                        <script data-cfasync="false" type='text/javascript'>
                            if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {} else {
                                console.log('push ad:div-gpt-ad-728x90-BTF-3');
                                freestar.queue.push(function() {
                                    googletag.display('div-gpt-ad-728x90-BTF-3');
                                });
                            }
                        </script>
                    </div>
                    <!-- /div.#fs_fs_btf_3 -->
                </div>
                <div id="all_kicking" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_kicking" id="kicking_sh">
                        <span class="section_anchor" id="kicking_link" data-label="Kicking & Punting"></span>
                        <h2>Kicking & Punting</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_kicking">
    
    <table class="sortable stats_table" id="kicking" data-cols-to-freeze=",1">
    <caption>Kicking & Punting Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>

      
      <tr class="over_header">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="header_scoring" colspan="4" class=" over_header center" >Scoring</th>
         <th aria-label="" data-stat="header_punt" colspan="4" class=" over_header center" >Punting</th>
      </tr>
            
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Extra Pt Made" data-stat="xpm" scope="col" class=" poptip center" data-tip="Extra Points Made" data-over-header="Scoring" >XPM</th>
         <th aria-label="Extra Pt Att" data-stat="xpa" scope="col" class=" poptip center" data-tip="Extra Points Attempted" data-over-header="Scoring" >XPA</th>
         <th aria-label="Field Goals Made" data-stat="fgm" scope="col" class=" poptip center" data-tip="Field Goals Made" data-over-header="Scoring" >FGM</th>
         <th aria-label="Field Goals Att" data-stat="fga" scope="col" class=" poptip center" data-tip="Field Goals Attempted" data-over-header="Scoring" >FGA</th>
         <th aria-label="Punts" data-stat="punt" scope="col" class=" poptip center" data-tip="Times Punted" data-over-header="Punting" >Pnt</th>
         <th aria-label="Punting Yds" data-stat="punt_yds" scope="col" class=" poptip center" data-tip="Total Punt Yardage" data-over-header="Punting" >Yds</th>
         <th aria-label="Yds/Punt" data-stat="punt_yds_per_punt" scope="col" class=" poptip hide_non_quals center" data-tip="<b>Yards per Punt</b><br>Minimum one punt per game scheduled to qualify as leader.<br />Minimum 250 punts to qualify as career leader." data-over-header="Punting" data-filter="1" data-name="Yds/Punt" >Y/P</th>
         <th aria-label="Long Punt" data-stat="punt_long" scope="col" class=" poptip center" data-tip="Longest Punt" data-over-header="Punting" >Lng</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="LutzWi00" data-stat="player" ><a href="/players/L/LutzWi00.htm">Wil Lutz</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="xpm" >2</td><td class="right " data-stat="xpa" >2</td><td class="right " data-stat="fgm" >1</td><td class="right " data-stat="fga" >1</td><td class="right iz" data-stat="punt" >0</td><td class="right iz" data-stat="punt_yds" >0</td><td class="right iz" data-stat="punt_yds_per_punt" ></td><td class="right iz" data-stat="punt_long" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="DixoRi00" data-stat="player" ><a href="/players/D/DixoRi00.htm">Riley Dixon</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="xpm" ></td><td class="right iz" data-stat="xpa" ></td><td class="right iz" data-stat="fgm" ></td><td class="right iz" data-stat="fga" ></td><td class="right " data-stat="punt" >5</td><td class="right " data-stat="punt_yds" >259</td><td class="right " data-stat="punt_yds_per_punt" >51.8</td><td class="right " data-stat="punt_long" >56</td></tr>



      
      <tr class="over_header thead">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="header_scoring" colspan="4" class=" over_header center" >Scoring</th>
         <th aria-label="" data-stat="header_punt" colspan="4" class=" over_header center" >Punting</th>
      </tr>
            
      <tr class="thead">
         <th aria-label="Player" data-stat="player" class=" sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" class=" sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Extra Pt Made" data-stat="xpm" class=" center" data-tip="Extra Points Made" data-over-header="Scoring" >XPM</th>
         <th aria-label="Extra Pt Att" data-stat="xpa" class=" center" data-tip="Extra Points Attempted" data-over-header="Scoring" >XPA</th>
         <th aria-label="Field Goals Made" data-stat="fgm" class=" center" data-tip="Field Goals Made" data-over-header="Scoring" >FGM</th>
         <th aria-label="Field Goals Att" data-stat="fga" class=" center" data-tip="Field Goals Attempted" data-over-header="Scoring" >FGA</th>
         <th aria-label="Punts" data-stat="punt" class=" center" data-tip="Times Punted" data-over-header="Punting" >Pnt</th>
         <th aria-label="Punting Yds" data-stat="punt_yds" class=" center" data-tip="Total Punt Yardage" data-over-header="Punting" >Yds</th>
         <th aria-label="Yds/Punt" data-stat="punt_yds_per_punt" class=" hide_non_quals center" data-tip="<b>Yards per Punt</b><br>Minimum one punt per game scheduled to qualify as leader.<br />Minimum 250 punts to qualify as career leader." data-over-header="Punting" data-filter="1" data-name="Yds/Punt" >Y/P</th>
         <th aria-label="Long Punt" data-stat="punt_long" class=" center" data-tip="Longest Punt" data-over-header="Punting" >Lng</th>
      </tr>
      <tr ><th scope="row" class="left " data-append-csv="BadgMi00" data-stat="player" ><a href="/players/B/BadgMi00.htm">Michael Badgley</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="xpm" >6</td><td class="right " data-stat="xpa" >6</td><td class="right iz" data-stat="fgm" ></td><td class="right iz" data-stat="fga" ></td><td class="right iz" data-stat="punt" >0</td><td class="right iz" data-stat="punt_yds" >0</td><td class="right iz" data-stat="punt_yds_per_punt" ></td><td class="right iz" data-stat="punt_long" >0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="FoxxJa01" data-stat="player" ><a href="/players/F/FoxxJa01.htm">Jack Fox</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="xpm" ></td><td class="right iz" data-stat="xpa" ></td><td class="right iz" data-stat="fgm" ></td><td class="right iz" data-stat="fga" ></td><td class="right " data-stat="punt" >4</td><td class="right " data-stat="punt_yds" >141</td><td class="right " data-stat="punt_yds_per_punt" >35.3</td><td class="right " data-stat="punt_long" >48</td></tr>

</table>


</div>
-->
                </div>
                <div id="all_passing_advanced" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_passing_advanced" id="passing_advanced_sh">
                        <span class="section_anchor" id="passing_advanced_link" data-label="Advanced Passing"></span>
                        <h2>Advanced Passing</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_passing_advanced">
    
    <table class="sortable stats_table" id="passing_advanced" data-cols-to-freeze=",1">
    <caption>Advanced Passing Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Passes Completed" data-stat="pass_cmp" scope="col" class=" poptip center" data-tip="Passes completed" >Cmp</th>
         <th aria-label="Pass Attempts" data-stat="pass_att" scope="col" class=" poptip center" data-tip="Passes attempted" >Att</th>
         <th aria-label="Passing Yds" data-stat="pass_yds" scope="col" class=" poptip center" data-tip="Yards Gained by Passing<br>For teams, sack yardage is deducted from this total" >Yds</th>
         <th aria-label="Pass 1st Downs" data-stat="pass_first_down" scope="col" class=" poptip center" data-tip="First downs passing" >1D</th>
         <th aria-label="1D%" data-stat="pass_first_down_pct" scope="col" class=" poptip center" data-tip="First downs passing per pass play (pass attempts and sacks)" >1D%</th>
         <th aria-label="IAY" data-stat="pass_target_yds" scope="col" class=" poptip center" data-tip="Intended air yards - Air yards on all pass attempts, whether completed or incomplete" >IAY</th>
         <th aria-label="IAY/PA" data-stat="pass_tgt_yds_per_att" scope="col" class=" poptip hide_non_quals center" data-tip="Intended air yards per pass attempt - Average depth of target, whether completed or not" >IAY/PA</th>
         <th aria-label="CAY" data-stat="pass_air_yds" scope="col" class=" poptip center" data-tip="Completed air yards - Total yards completed passes traveled in the air past the line of scrimmage before being caught" >CAY</th>
         <th aria-label="CAY/Cmp" data-stat="pass_air_yds_per_cmp" scope="col" class=" poptip hide_non_quals center" data-tip="Completed air yards per completion - yards the ball traveled in the air past the line of scrimmage prior to a completion" >CAY/Cmp</th>
         <th aria-label="CAY/PA" data-stat="pass_air_yds_per_att" scope="col" class=" poptip hide_non_quals center" data-tip="Completed air yards per pass attempt - Air yards (on completed passes) per pass attempt" >CAY/PA</th>
         <th aria-label="YAC" data-stat="pass_yac" scope="col" class=" poptip center" data-tip="Pass yards after catch" >YAC</th>
         <th aria-label="YAC/Cmp" data-stat="pass_yac_per_cmp" scope="col" class=" poptip hide_non_quals center" data-tip="Pass yards after catch per completion" >YAC/Cmp</th>
         <th aria-label="Drops" data-stat="pass_drops" scope="col" class=" poptip center" data-tip="Passes dropped" >Drops</th>
         <th aria-label="Drop%" data-stat="pass_drop_pct" scope="col" class=" poptip hide_non_quals center" data-tip="Percentage of passes dropped per pass attempt, excluding spikes and throwaways" >Drop%</th>
         <th aria-label="BadTh" data-stat="pass_poor_throws" scope="col" class=" poptip center" data-tip="Poor throws" >BadTh</th>
         <th aria-label="Bad%" data-stat="pass_poor_throw_pct" scope="col" class=" poptip hide_non_quals center" data-tip="Percentage of poor throws per pass attempt, excluding spikes and throwaways" >Bad%</th>
         <th aria-label="Sacked " data-stat="pass_sacked" scope="col" class=" poptip center" data-tip="Times Sacked (official since 1969, complete NFL coverage since 1963, partial NFL coverage from 1960-62)" >Sk</th>
         <th aria-label="Bltz" data-stat="pass_blitzed" scope="col" class=" poptip center" data-tip="Times blitzed" >Bltz</th>
         <th aria-label="Hrry" data-stat="pass_hurried" scope="col" class=" poptip center" data-tip="Times hurried" >Hrry</th>
         <th aria-label="Hits" data-stat="pass_hits" scope="col" class=" poptip center" data-tip="Times hit as a QB while passing" >Hits</th>
         <th aria-label="Prss" data-stat="pass_pressured" scope="col" class=" poptip center" data-tip="Times the QB was pressured (hurries + hits+ times sacked)" >Prss</th>
         <th aria-label="Prss%" data-stat="pass_pressured_pct" scope="col" class=" poptip hide_non_quals center" data-tip="Times pressured per dropback" >Prss%</th>
         <th aria-label="Scrm" data-stat="rush_scrambles" scope="col" class=" poptip center" data-tip="Scrambles (rushes on plays designed as passes)" >Scrm</th>
         <th aria-label="Yds/Scr" data-stat="rush_scrambles_yds_per_att" scope="col" class=" poptip center" data-tip="Yards per scramble attempt" >Yds/Scr</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="WilsRu00" data-stat="player" ><a href="/players/W/WilsRu00.htm">Russell Wilson</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="pass_cmp" >18</td><td class="right " data-stat="pass_att" >32</td><td class="right " data-stat="pass_yds" >223</td><td class="right " data-stat="pass_first_down" >12</td><td class="right " data-stat="pass_first_down_pct" >35.3</td><td class="right " data-stat="pass_target_yds" >232</td><td class="right " data-stat="pass_tgt_yds_per_att" >7.3</td><td class="right " data-stat="pass_air_yds" >86</td><td class="right " data-stat="pass_air_yds_per_cmp" >4.8</td><td class="right " data-stat="pass_air_yds_per_att" >2.7</td><td class="right " data-stat="pass_yac" >137</td><td class="right " data-stat="pass_yac_per_cmp" >7.6</td><td class="right " data-stat="pass_drops" >2</td><td class="right " data-stat="pass_drop_pct" >6.3%</td><td class="right " data-stat="pass_poor_throws" >4</td><td class="right " data-stat="pass_poor_throw_pct" >12.5%</td><td class="right " data-stat="pass_sacked" >2</td><td class="right " data-stat="pass_blitzed" >15</td><td class="right " data-stat="pass_hurried" >5</td><td class="right " data-stat="pass_hits" >6</td><td class="right " data-stat="pass_pressured" >13</td><td class="right " data-stat="pass_pressured_pct" >37.1%</td><td class="right " data-stat="rush_scrambles" >1</td><td class="right " data-stat="rush_scrambles_yds_per_att" >1.0</td></tr>

      
      <tr class="thead">
         <th aria-label="Player" data-stat="player" class=" sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" class=" sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Passes Completed" data-stat="pass_cmp" class=" center" data-tip="Passes completed" >Cmp</th>
         <th aria-label="Pass Attempts" data-stat="pass_att" class=" center" data-tip="Passes attempted" >Att</th>
         <th aria-label="Passing Yds" data-stat="pass_yds" class=" center" data-tip="Yards Gained by Passing<br>For teams, sack yardage is deducted from this total" >Yds</th>
         <th aria-label="Pass 1st Downs" data-stat="pass_first_down" class=" center" data-tip="First downs passing" >1D</th>
         <th aria-label="1D%" data-stat="pass_first_down_pct" class=" center" data-tip="First downs passing per pass play (pass attempts and sacks)" >1D%</th>
         <th aria-label="IAY" data-stat="pass_target_yds" class=" center" data-tip="Intended air yards - Air yards on all pass attempts, whether completed or incomplete" >IAY</th>
         <th aria-label="IAY/PA" data-stat="pass_tgt_yds_per_att" class=" hide_non_quals center" data-tip="Intended air yards per pass attempt - Average depth of target, whether completed or not" >IAY/PA</th>
         <th aria-label="CAY" data-stat="pass_air_yds" class=" center" data-tip="Completed air yards - Total yards completed passes traveled in the air past the line of scrimmage before being caught" >CAY</th>
         <th aria-label="CAY/Cmp" data-stat="pass_air_yds_per_cmp" class=" hide_non_quals center" data-tip="Completed air yards per completion - yards the ball traveled in the air past the line of scrimmage prior to a completion" >CAY/Cmp</th>
         <th aria-label="CAY/PA" data-stat="pass_air_yds_per_att" class=" hide_non_quals center" data-tip="Completed air yards per pass attempt - Air yards (on completed passes) per pass attempt" >CAY/PA</th>
         <th aria-label="YAC" data-stat="pass_yac" class=" center" data-tip="Pass yards after catch" >YAC</th>
         <th aria-label="YAC/Cmp" data-stat="pass_yac_per_cmp" class=" hide_non_quals center" data-tip="Pass yards after catch per completion" >YAC/Cmp</th>
         <th aria-label="Drops" data-stat="pass_drops" class=" center" data-tip="Passes dropped" >Drops</th>
         <th aria-label="Drop%" data-stat="pass_drop_pct" class=" hide_non_quals center" data-tip="Percentage of passes dropped per pass attempt, excluding spikes and throwaways" >Drop%</th>
         <th aria-label="BadTh" data-stat="pass_poor_throws" class=" center" data-tip="Poor throws" >BadTh</th>
         <th aria-label="Bad%" data-stat="pass_poor_throw_pct" class=" hide_non_quals center" data-tip="Percentage of poor throws per pass attempt, excluding spikes and throwaways" >Bad%</th>
         <th aria-label="Sacked " data-stat="pass_sacked" class=" center" data-tip="Times Sacked (official since 1969, complete NFL coverage since 1963, partial NFL coverage from 1960-62)" >Sk</th>
         <th aria-label="Bltz" data-stat="pass_blitzed" class=" center" data-tip="Times blitzed" >Bltz</th>
         <th aria-label="Hrry" data-stat="pass_hurried" class=" center" data-tip="Times hurried" >Hrry</th>
         <th aria-label="Hits" data-stat="pass_hits" class=" center" data-tip="Times hit as a QB while passing" >Hits</th>
         <th aria-label="Prss" data-stat="pass_pressured" class=" center" data-tip="Times the QB was pressured (hurries + hits+ times sacked)" >Prss</th>
         <th aria-label="Prss%" data-stat="pass_pressured_pct" class=" hide_non_quals center" data-tip="Times pressured per dropback" >Prss%</th>
         <th aria-label="Scrm" data-stat="rush_scrambles" class=" center" data-tip="Scrambles (rushes on plays designed as passes)" >Scrm</th>
         <th aria-label="Yds/Scr" data-stat="rush_scrambles_yds_per_att" class=" center" data-tip="Yards per scramble attempt" >Yds/Scr</th>
      </tr>
      <tr ><th scope="row" class="left " data-append-csv="GoffJa00" data-stat="player" ><a href="/players/G/GoffJa00.htm">Jared Goff</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="pass_cmp" >24</td><td class="right " data-stat="pass_att" >34</td><td class="right " data-stat="pass_yds" >278</td><td class="right " data-stat="pass_first_down" >18</td><td class="right " data-stat="pass_first_down_pct" >50.0</td><td class="right " data-stat="pass_target_yds" >290</td><td class="right " data-stat="pass_tgt_yds_per_att" >8.5</td><td class="right " data-stat="pass_air_yds" >157</td><td class="right " data-stat="pass_air_yds_per_cmp" >6.5</td><td class="right " data-stat="pass_air_yds_per_att" >4.6</td><td class="right " data-stat="pass_yac" >121</td><td class="right " data-stat="pass_yac_per_cmp" >5.0</td><td class="right iz" data-stat="pass_drops" >0</td><td class="right iz" data-stat="pass_drop_pct" >0.0%</td><td class="right " data-stat="pass_poor_throws" >5</td><td class="right " data-stat="pass_poor_throw_pct" >15.6%</td><td class="right " data-stat="pass_sacked" >2</td><td class="right " data-stat="pass_blitzed" >18</td><td class="right " data-stat="pass_hurried" >1</td><td class="right " data-stat="pass_hits" >5</td><td class="right " data-stat="pass_pressured" >8</td><td class="right " data-stat="pass_pressured_pct" >22.2%</td><td class="right iz" data-stat="rush_scrambles" >0</td><td class="right iz" data-stat="rush_scrambles_yds_per_att" ></td></tr>

</table>


</div>
-->
                </div>
                <div id="all_rushing_advanced" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_rushing_advanced" id="rushing_advanced_sh">
                        <span class="section_anchor" id="rushing_advanced_link" data-label="Advanced Rushing"></span>
                        <h2>Advanced Rushing</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_rushing_advanced">
    
    <table class="sortable stats_table" id="rushing_advanced" data-cols-to-freeze=",1">
    <caption>Advanced Rushing Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Rushing Att" data-stat="rush_att" scope="col" class=" poptip center" data-tip="Rushing Attempts (sacks not included in NFL)" >Att</th>
         <th aria-label="Rushing Yds" data-stat="rush_yds" scope="col" class=" poptip center" data-tip="Rushing Yards Gained (sack yardage is not included by NFL)" >Yds</th>
         <th aria-label="Rushing TD" data-stat="rush_td" scope="col" class=" poptip center" data-tip="Rushing Touchdowns" >TD</th>
         <th aria-label="Rush 1st Downs" data-stat="rush_first_down" scope="col" class=" poptip center" data-tip="First downs rushing" >1D</th>
         <th aria-label="YBC" data-stat="rush_yds_before_contact" scope="col" class=" poptip center" data-tip="Rushing yards before contact" >YBC</th>
         <th aria-label="YBC/Att" data-stat="rush_yds_bc_per_rush" scope="col" class=" poptip hide_non_quals center" data-tip="Rushing yards before contact per rushing attempt" >YBC/Att</th>
         <th aria-label="YAC" data-stat="rush_yac" scope="col" class=" poptip center" data-tip="Rushing yards after contact" >YAC</th>
         <th aria-label="YAC/Att" data-stat="rush_yac_per_rush" scope="col" class=" poptip hide_non_quals center" data-tip="Rushing yards after contact per rush" >YAC/Att</th>
         <th aria-label="BrkTkl" data-stat="rush_broken_tackles" scope="col" class=" poptip center" data-tip="Broken tackles on rushes" >BrkTkl</th>
         <th aria-label="Att/Br" data-stat="rush_broken_tackles_per_rush" scope="col" class=" poptip sort_default_asc hide_non_quals center" data-tip="Rush attempts per broken tackle" >Att/Br</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="WillJa10" data-stat="player" ><a href="/players/W/WillJa10.htm">Javonte Williams</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="rush_att" >12</td><td class="right " data-stat="rush_yds" >27</td><td class="right iz" data-stat="rush_td" >0</td><td class="right " data-stat="rush_first_down" >1</td><td class="right " data-stat="rush_yds_before_contact" >10</td><td class="right " data-stat="rush_yds_bc_per_rush" >0.8</td><td class="right " data-stat="rush_yac" >17</td><td class="right " data-stat="rush_yac_per_rush" >1.4</td><td class="right iz" data-stat="rush_broken_tackles" >0</td><td class="right iz" data-stat="rush_broken_tackles_per_rush" ></td></tr>
<tr ><th scope="row" class="left " data-append-csv="WilsRu00" data-stat="player" ><a href="/players/W/WilsRu00.htm">Russell Wilson</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="rush_att" >7</td><td class="right " data-stat="rush_yds" >6</td><td class="right " data-stat="rush_td" >1</td><td class="right " data-stat="rush_first_down" >3</td><td class="right " data-stat="rush_yds_before_contact" >6</td><td class="right " data-stat="rush_yds_bc_per_rush" >0.9</td><td class="right iz" data-stat="rush_yac" >0</td><td class="right iz" data-stat="rush_yac_per_rush" >0.0</td><td class="right iz" data-stat="rush_broken_tackles" >0</td><td class="right iz" data-stat="rush_broken_tackles_per_rush" ></td></tr>
<tr ><th scope="row" class="left " data-append-csv="PeriSa00" data-stat="player" ><a href="/players/P/PeriSa00.htm">Samaje Perine</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="rush_att" >6</td><td class="right " data-stat="rush_yds" >37</td><td class="right iz" data-stat="rush_td" >0</td><td class="right " data-stat="rush_first_down" >2</td><td class="right " data-stat="rush_yds_before_contact" >9</td><td class="right " data-stat="rush_yds_bc_per_rush" >1.5</td><td class="right " data-stat="rush_yac" >28</td><td class="right " data-stat="rush_yac_per_rush" >4.7</td><td class="right " data-stat="rush_broken_tackles" >1</td><td class="right " data-stat="rush_broken_tackles_per_rush" >6.0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McLaJa00" data-stat="player" ><a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="rush_att" >2</td><td class="right " data-stat="rush_yds" >2</td><td class="right iz" data-stat="rush_td" >0</td><td class="right iz" data-stat="rush_first_down" ></td><td class="right " data-stat="rush_yds_before_contact" >2</td><td class="right " data-stat="rush_yds_bc_per_rush" >1.0</td><td class="right iz" data-stat="rush_yac" >0</td><td class="right iz" data-stat="rush_yac_per_rush" >0.0</td><td class="right iz" data-stat="rush_broken_tackles" >0</td><td class="right iz" data-stat="rush_broken_tackles_per_rush" ></td></tr>
<tr ><th scope="row" class="left " data-append-csv="MimsMa00" data-stat="player" ><a href="/players/M/MimsMa00.htm">Marvin Mims</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="rush_att" >1</td><td class="right " data-stat="rush_yds" >11</td><td class="right iz" data-stat="rush_td" >0</td><td class="right " data-stat="rush_first_down" >1</td><td class="right " data-stat="rush_yds_before_contact" >6</td><td class="right " data-stat="rush_yds_bc_per_rush" >6.0</td><td class="right " data-stat="rush_yac" >5</td><td class="right " data-stat="rush_yac_per_rush" >5.0</td><td class="right iz" data-stat="rush_broken_tackles" >0</td><td class="right iz" data-stat="rush_broken_tackles_per_rush" ></td></tr>

      
      <tr class="thead">
         <th aria-label="Player" data-stat="player" class=" sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" class=" sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Rushing Att" data-stat="rush_att" class=" center" data-tip="Rushing Attempts (sacks not included in NFL)" >Att</th>
         <th aria-label="Rushing Yds" data-stat="rush_yds" class=" center" data-tip="Rushing Yards Gained (sack yardage is not included by NFL)" >Yds</th>
         <th aria-label="Rushing TD" data-stat="rush_td" class=" center" data-tip="Rushing Touchdowns" >TD</th>
         <th aria-label="Rush 1st Downs" data-stat="rush_first_down" class=" center" data-tip="First downs rushing" >1D</th>
         <th aria-label="YBC" data-stat="rush_yds_before_contact" class=" center" data-tip="Rushing yards before contact" >YBC</th>
         <th aria-label="YBC/Att" data-stat="rush_yds_bc_per_rush" class=" hide_non_quals center" data-tip="Rushing yards before contact per rushing attempt" >YBC/Att</th>
         <th aria-label="YAC" data-stat="rush_yac" class=" center" data-tip="Rushing yards after contact" >YAC</th>
         <th aria-label="YAC/Att" data-stat="rush_yac_per_rush" class=" hide_non_quals center" data-tip="Rushing yards after contact per rush" >YAC/Att</th>
         <th aria-label="BrkTkl" data-stat="rush_broken_tackles" class=" center" data-tip="Broken tackles on rushes" >BrkTkl</th>
         <th aria-label="Att/Br" data-stat="rush_broken_tackles_per_rush" class=" sort_default_asc hide_non_quals center" data-tip="Rush attempts per broken tackle" >Att/Br</th>
      </tr>
      <tr ><th scope="row" class="left " data-append-csv="MontDa01" data-stat="player" ><a href="/players/M/MontDa01.htm">David Montgomery</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="rush_att" >17</td><td class="right " data-stat="rush_yds" >85</td><td class="right iz" data-stat="rush_td" >0</td><td class="right " data-stat="rush_first_down" >5</td><td class="right " data-stat="rush_yds_before_contact" >32</td><td class="right " data-stat="rush_yds_bc_per_rush" >1.9</td><td class="right " data-stat="rush_yac" >53</td><td class="right " data-stat="rush_yac_per_rush" >3.1</td><td class="right " data-stat="rush_broken_tackles" >1</td><td class="right " data-stat="rush_broken_tackles_per_rush" >17.0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="GibbJa01" data-stat="player" ><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="rush_att" >11</td><td class="right " data-stat="rush_yds" >100</td><td class="right " data-stat="rush_td" >1</td><td class="right " data-stat="rush_first_down" >5</td><td class="right " data-stat="rush_yds_before_contact" >44</td><td class="right " data-stat="rush_yds_bc_per_rush" >4.0</td><td class="right " data-stat="rush_yac" >56</td><td class="right " data-stat="rush_yac_per_rush" >5.1</td><td class="right " data-stat="rush_broken_tackles" >3</td><td class="right " data-stat="rush_broken_tackles_per_rush" >3.7</td></tr>

</table>


</div>
-->
                </div>
                <div id="all_receiving_advanced" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_receiving_advanced" id="receiving_advanced_sh">
                        <span class="section_anchor" id="receiving_advanced_link" data-label="Advanced Receiving"></span>
                        <h2>Advanced Receiving</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_receiving_advanced">
    
    <table class="sortable stats_table" id="receiving_advanced" data-cols-to-freeze=",1">
    <caption>Advanced Receiving Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Targets" data-stat="targets" scope="col" class=" poptip center" data-tip="Pass Targets (since 1992, derived from NFL play-by-play data)" >Tgt</th>
         <th aria-label="Receptions" data-stat="rec" scope="col" class=" poptip center" data-tip="Receptions" >Rec</th>
         <th aria-label="Receiving Yds" data-stat="rec_yds" scope="col" class=" poptip center" data-tip="Receiving Yards" >Yds</th>
         <th aria-label="Receiving TD" data-stat="rec_td" scope="col" class=" poptip center" data-tip="Receiving Touchdowns" >TD</th>
         <th aria-label="Receiving 1st Downs" data-stat="rec_first_down" scope="col" class=" poptip center" data-tip="First downs receiving" >1D</th>
         <th aria-label="YBC" data-stat="rec_air_yds" scope="col" class=" poptip center" data-tip="Total yards passes traveled in the air before being caught" >YBC</th>
         <th aria-label="YBC/R" data-stat="rec_air_yds_per_rec" scope="col" class=" poptip hide_non_quals center" data-tip="Yards before catch per reception" >YBC/R</th>
         <th aria-label="YAC" data-stat="rec_yac" scope="col" class=" poptip center" data-tip="Yards after catch" >YAC</th>
         <th aria-label="YAC/R" data-stat="rec_yac_per_rec" scope="col" class=" poptip hide_non_quals center" data-tip="Yards after catch per reception" >YAC/R</th>
         <th aria-label="ADOT" data-stat="rec_adot" scope="col" class=" poptip hide_non_quals center" data-tip="Average depth of target when targeted, whether completed or not. 25 targets/16 game pace required for leaderboards." >ADOT</th>
         <th aria-label="BrkTkl" data-stat="rec_broken_tackles" scope="col" class=" poptip center" data-tip="Broken tackles on receptions" >BrkTkl</th>
         <th aria-label="Rec/Br" data-stat="rec_broken_tackles_per_rec" scope="col" class=" poptip sort_default_asc hide_non_quals center" data-tip="Receptions per broken tackle" >Rec/Br</th>
         <th aria-label="Drop" data-stat="rec_drops" scope="col" class=" poptip center" data-tip="Dropped passes" >Drop</th>
         <th aria-label="Drop%" data-stat="rec_drop_pct" scope="col" class=" poptip hide_non_quals center" data-tip="Dropped passes per target" >Drop%</th>
         <th aria-label="Int" data-stat="rec_target_int" scope="col" class=" poptip center" data-tip="Interceptions on passes where targeted" >Int</th>
         <th aria-label="Rat" data-stat="rec_pass_rating" scope="col" class=" poptip hide_non_quals center" data-tip="Passer rating on passes when targeted. 25 targets/16 game pace required for leaderboards." >Rat</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="SuttCo00" data-stat="player" ><a href="/players/S/SuttCo00.htm">Courtland Sutton</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >6</td><td class="right " data-stat="rec" >5</td><td class="right " data-stat="rec_yds" >71</td><td class="right iz" data-stat="rec_td" >0</td><td class="right " data-stat="rec_first_down" >4</td><td class="right " data-stat="rec_air_yds" >45</td><td class="right " data-stat="rec_air_yds_per_rec" >9.0</td><td class="right " data-stat="rec_yac" >26</td><td class="right " data-stat="rec_yac_per_rec" >5.2</td><td class="right " data-stat="rec_adot" >9.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >116.0</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HumpLi01" data-stat="player" ><a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >4</td><td class="right " data-stat="rec" >3</td><td class="right " data-stat="rec_yds" >16</td><td class="right " data-stat="rec_td" >1</td><td class="right " data-stat="rec_first_down" >2</td><td class="right " data-stat="rec_air_yds" >10</td><td class="right " data-stat="rec_air_yds_per_rec" >3.3</td><td class="right " data-stat="rec_yac" >6</td><td class="right " data-stat="rec_yac_per_rec" >2.0</td><td class="right " data-stat="rec_adot" >3.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right " data-stat="rec_drops" >1</td><td class="right " data-stat="rec_drop_pct" >25.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >120.8</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JeudJe00" data-stat="player" ><a href="/players/J/JeudJe00.htm">Jerry Jeudy</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >7</td><td class="right " data-stat="rec" >3</td><td class="right " data-stat="rec_yds" >74</td><td class="right iz" data-stat="rec_td" >0</td><td class="right " data-stat="rec_first_down" >3</td><td class="right " data-stat="rec_air_yds" >25</td><td class="right " data-stat="rec_air_yds_per_rec" >8.3</td><td class="right " data-stat="rec_yac" >49</td><td class="right " data-stat="rec_yac_per_rec" >16.3</td><td class="right " data-stat="rec_adot" >8.6</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right " data-stat="rec_drops" >1</td><td class="right " data-stat="rec_drop_pct" >14.3</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >81.8</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McLaJa00" data-stat="player" ><a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >3</td><td class="right " data-stat="rec" >2</td><td class="right " data-stat="rec_yds" >16</td><td class="right iz" data-stat="rec_td" >0</td><td class="right iz" data-stat="rec_first_down" ></td><td class="right " data-stat="rec_air_yds" >-2</td><td class="right " data-stat="rec_air_yds_per_rec" >-1.0</td><td class="right " data-stat="rec_yac" >18</td><td class="right " data-stat="rec_yac_per_rec" >9.0</td><td class="right " data-stat="rec_adot" >-2.0</td><td class="right " data-stat="rec_broken_tackles" >1</td><td class="right " data-stat="rec_broken_tackles_per_rec" >2.0</td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >79.9</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WillJa10" data-stat="player" ><a href="/players/W/WillJa10.htm">Javonte Williams</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >2</td><td class="right " data-stat="rec" >2</td><td class="right " data-stat="rec_yds" >-7</td><td class="right iz" data-stat="rec_td" >0</td><td class="right iz" data-stat="rec_first_down" >0</td><td class="right " data-stat="rec_air_yds" >-10</td><td class="right " data-stat="rec_air_yds_per_rec" >-5.0</td><td class="right " data-stat="rec_yac" >3</td><td class="right " data-stat="rec_yac_per_rec" >1.5</td><td class="right " data-stat="rec_adot" >-5.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >79.2</td></tr>
<tr ><th scope="row" class="left " data-append-csv="KrulLu00" data-stat="player" ><a href="/players/K/KrulLu00.htm">Lucas Krull</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >3</td><td class="right " data-stat="rec" >1</td><td class="right " data-stat="rec_yds" >18</td><td class="right iz" data-stat="rec_td" >0</td><td class="right " data-stat="rec_first_down" >1</td><td class="right " data-stat="rec_air_yds" >16</td><td class="right " data-stat="rec_air_yds_per_rec" >16.0</td><td class="right " data-stat="rec_yac" >2</td><td class="right " data-stat="rec_yac_per_rec" >2.0</td><td class="right " data-stat="rec_adot" >15.3</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >54.9</td></tr>
<tr ><th scope="row" class="left " data-append-csv="TrauAd00" data-stat="player" ><a href="/players/T/TrauAd00.htm">Adam Trautman</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >3</td><td class="right " data-stat="rec" >1</td><td class="right " data-stat="rec_yds" >24</td><td class="right iz" data-stat="rec_td" >0</td><td class="right " data-stat="rec_first_down" >1</td><td class="right " data-stat="rec_air_yds" >-1</td><td class="right " data-stat="rec_air_yds_per_rec" >-1.0</td><td class="right " data-stat="rec_yac" >25</td><td class="right " data-stat="rec_yac_per_rec" >25.0</td><td class="right " data-stat="rec_adot" >5.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >63.2</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PeriSa00" data-stat="player" ><a href="/players/P/PeriSa00.htm">Samaje Perine</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >1</td><td class="right " data-stat="rec" >1</td><td class="right " data-stat="rec_yds" >11</td><td class="right iz" data-stat="rec_td" >0</td><td class="right " data-stat="rec_first_down" >1</td><td class="right " data-stat="rec_air_yds" >3</td><td class="right " data-stat="rec_air_yds_per_rec" >3.0</td><td class="right " data-stat="rec_yac" >8</td><td class="right " data-stat="rec_yac_per_rec" >8.0</td><td class="right " data-stat="rec_adot" >3.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >112.5</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JohnBr23" data-stat="player" ><a href="/players/J/JohnBr23.htm">Brandon Johnson</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >1</td><td class="right iz" data-stat="rec" >0</td><td class="right iz" data-stat="rec_yds" >0</td><td class="right iz" data-stat="rec_td" >0</td><td class="right iz" data-stat="rec_first_down" ></td><td class="right iz" data-stat="rec_air_yds" >0</td><td class="right iz" data-stat="rec_air_yds_per_rec" ></td><td class="right iz" data-stat="rec_yac" >0</td><td class="right iz" data-stat="rec_yac_per_rec" ></td><td class="right " data-stat="rec_adot" >3.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >39.6</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MimsMa00" data-stat="player" ><a href="/players/M/MimsMa00.htm">Marvin Mims</a></th><td class="left " data-stat="team" >DEN</td><td class="right " data-stat="targets" >2</td><td class="right iz" data-stat="rec" >0</td><td class="right iz" data-stat="rec_yds" >0</td><td class="right iz" data-stat="rec_td" >0</td><td class="right iz" data-stat="rec_first_down" >0</td><td class="right iz" data-stat="rec_air_yds" >0</td><td class="right iz" data-stat="rec_air_yds_per_rec" ></td><td class="right iz" data-stat="rec_yac" >0</td><td class="right iz" data-stat="rec_yac_per_rec" ></td><td class="right " data-stat="rec_adot" >27.5</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >39.6</td></tr>

      
      <tr class="thead">
         <th aria-label="Player" data-stat="player" class=" sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" class=" sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Targets" data-stat="targets" class=" center" data-tip="Pass Targets (since 1992, derived from NFL play-by-play data)" >Tgt</th>
         <th aria-label="Receptions" data-stat="rec" class=" center" data-tip="Receptions" >Rec</th>
         <th aria-label="Receiving Yds" data-stat="rec_yds" class=" center" data-tip="Receiving Yards" >Yds</th>
         <th aria-label="Receiving TD" data-stat="rec_td" class=" center" data-tip="Receiving Touchdowns" >TD</th>
         <th aria-label="Receiving 1st Downs" data-stat="rec_first_down" class=" center" data-tip="First downs receiving" >1D</th>
         <th aria-label="YBC" data-stat="rec_air_yds" class=" center" data-tip="Total yards passes traveled in the air before being caught" >YBC</th>
         <th aria-label="YBC/R" data-stat="rec_air_yds_per_rec" class=" hide_non_quals center" data-tip="Yards before catch per reception" >YBC/R</th>
         <th aria-label="YAC" data-stat="rec_yac" class=" center" data-tip="Yards after catch" >YAC</th>
         <th aria-label="YAC/R" data-stat="rec_yac_per_rec" class=" hide_non_quals center" data-tip="Yards after catch per reception" >YAC/R</th>
         <th aria-label="ADOT" data-stat="rec_adot" class=" hide_non_quals center" data-tip="Average depth of target when targeted, whether completed or not. 25 targets/16 game pace required for leaderboards." >ADOT</th>
         <th aria-label="BrkTkl" data-stat="rec_broken_tackles" class=" center" data-tip="Broken tackles on receptions" >BrkTkl</th>
         <th aria-label="Rec/Br" data-stat="rec_broken_tackles_per_rec" class=" sort_default_asc hide_non_quals center" data-tip="Receptions per broken tackle" >Rec/Br</th>
         <th aria-label="Drop" data-stat="rec_drops" class=" center" data-tip="Dropped passes" >Drop</th>
         <th aria-label="Drop%" data-stat="rec_drop_pct" class=" hide_non_quals center" data-tip="Dropped passes per target" >Drop%</th>
         <th aria-label="Int" data-stat="rec_target_int" class=" center" data-tip="Interceptions on passes where targeted" >Int</th>
         <th aria-label="Rat" data-stat="rec_pass_rating" class=" hide_non_quals center" data-tip="Passer rating on passes when targeted. 25 targets/16 game pace required for leaderboards." >Rat</th>
      </tr>
      <tr ><th scope="row" class="left " data-append-csv="StxxAm00" data-stat="player" ><a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="targets" >9</td><td class="right " data-stat="rec" >7</td><td class="right " data-stat="rec_yds" >112</td><td class="right " data-stat="rec_td" >1</td><td class="right " data-stat="rec_first_down" >6</td><td class="right " data-stat="rec_air_yds" >50</td><td class="right " data-stat="rec_air_yds_per_rec" >7.1</td><td class="right " data-stat="rec_yac" >62</td><td class="right " data-stat="rec_yac_per_rec" >8.9</td><td class="right " data-stat="rec_adot" >8.0</td><td class="right " data-stat="rec_broken_tackles" >1</td><td class="right " data-stat="rec_broken_tackles_per_rec" >7.0</td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >155.6</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LaPoSa01" data-stat="player" ><a href="/players/L/LaPoSa01.htm">Sam LaPorta</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="targets" >6</td><td class="right " data-stat="rec" >5</td><td class="right " data-stat="rec_yds" >56</td><td class="right " data-stat="rec_td" >3</td><td class="right " data-stat="rec_first_down" >5</td><td class="right " data-stat="rec_air_yds" >30</td><td class="right " data-stat="rec_air_yds_per_rec" >6.0</td><td class="right " data-stat="rec_yac" >26</td><td class="right " data-stat="rec_yac_per_rec" >5.2</td><td class="right " data-stat="rec_adot" >7.5</td><td class="right " data-stat="rec_broken_tackles" >1</td><td class="right " data-stat="rec_broken_tackles_per_rec" >5.0</td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >145.1</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WillJa11" data-stat="player" ><a href="/players/W/WillJa11.htm">Jameson Williams</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="targets" >7</td><td class="right " data-stat="rec" >4</td><td class="right " data-stat="rec_yds" >47</td><td class="right iz" data-stat="rec_td" >0</td><td class="right " data-stat="rec_first_down" >3</td><td class="right " data-stat="rec_air_yds" >32</td><td class="right " data-stat="rec_air_yds_per_rec" >8.0</td><td class="right " data-stat="rec_yac" >15</td><td class="right " data-stat="rec_yac_per_rec" >3.8</td><td class="right " data-stat="rec_adot" >16.1</td><td class="right " data-stat="rec_broken_tackles" >1</td><td class="right " data-stat="rec_broken_tackles_per_rec" >4.0</td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >77.7</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ReynJo00" data-stat="player" ><a href="/players/R/ReynJo00.htm">Josh Reynolds</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="targets" >3</td><td class="right " data-stat="rec" >2</td><td class="right " data-stat="rec_yds" >41</td><td class="right iz" data-stat="rec_td" >0</td><td class="right " data-stat="rec_first_down" >2</td><td class="right " data-stat="rec_air_yds" >35</td><td class="right " data-stat="rec_air_yds_per_rec" >17.5</td><td class="right " data-stat="rec_yac" >6</td><td class="right " data-stat="rec_yac_per_rec" >3.0</td><td class="right " data-stat="rec_adot" >13.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >109.7</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MontDa01" data-stat="player" ><a href="/players/M/MontDa01.htm">David Montgomery</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="targets" >3</td><td class="right " data-stat="rec" >2</td><td class="right " data-stat="rec_yds" >-3</td><td class="right iz" data-stat="rec_td" >0</td><td class="right iz" data-stat="rec_first_down" >0</td><td class="right " data-stat="rec_air_yds" >-10</td><td class="right " data-stat="rec_air_yds_per_rec" >-5.0</td><td class="right " data-stat="rec_yac" >7</td><td class="right " data-stat="rec_yac_per_rec" >3.5</td><td class="right " data-stat="rec_adot" >-2.3</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >70.1</td></tr>
<tr ><th scope="row" class="left " data-append-csv="GibbJa01" data-stat="player" ><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="targets" >2</td><td class="right " data-stat="rec" >2</td><td class="right " data-stat="rec_yds" >8</td><td class="right " data-stat="rec_td" >1</td><td class="right " data-stat="rec_first_down" >1</td><td class="right " data-stat="rec_air_yds" >3</td><td class="right " data-stat="rec_air_yds_per_rec" >1.5</td><td class="right " data-stat="rec_yac" >5</td><td class="right " data-stat="rec_yac_per_rec" >2.5</td><td class="right " data-stat="rec_adot" >1.5</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >122.9</td></tr>
<tr ><th scope="row" class="left " data-append-csv="RaymKa00" data-stat="player" ><a href="/players/R/RaymKa00.htm">Kalif Raymond</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="targets" >1</td><td class="right " data-stat="rec" >1</td><td class="right " data-stat="rec_yds" >12</td><td class="right iz" data-stat="rec_td" >0</td><td class="right " data-stat="rec_first_down" >1</td><td class="right " data-stat="rec_air_yds" >13</td><td class="right " data-stat="rec_air_yds_per_rec" >13.0</td><td class="right " data-stat="rec_yac" >-1</td><td class="right " data-stat="rec_yac_per_rec" >-1.0</td><td class="right " data-stat="rec_adot" >13.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >116.7</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PeopDo00" data-stat="player" ><a href="/players/P/PeopDo00.htm">Donovan Peoples-Jones</a></th><td class="left " data-stat="team" >DET</td><td class="right " data-stat="targets" >1</td><td class="right " data-stat="rec" >1</td><td class="right " data-stat="rec_yds" >5</td><td class="right iz" data-stat="rec_td" >0</td><td class="right iz" data-stat="rec_first_down" ></td><td class="right " data-stat="rec_air_yds" >4</td><td class="right " data-stat="rec_air_yds_per_rec" >4.0</td><td class="right " data-stat="rec_yac" >1</td><td class="right " data-stat="rec_yac_per_rec" >1.0</td><td class="right " data-stat="rec_adot" >4.0</td><td class="right iz" data-stat="rec_broken_tackles" >0</td><td class="right iz" data-stat="rec_broken_tackles_per_rec" ></td><td class="right iz" data-stat="rec_drops" >0</td><td class="right iz" data-stat="rec_drop_pct" >0.0</td><td class="right iz" data-stat="rec_target_int" >0</td><td class="right " data-stat="rec_pass_rating" >87.5</td></tr>

</table>


</div>
-->
                </div>
                <div id="all_defense_advanced" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_defense_advanced" id="defense_advanced_sh">
                        <span class="section_anchor" id="defense_advanced_link" data-label="Advanced Defense"></span>
                        <h2>Advanced Defense</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_defense_advanced">
    
    <table class="sortable stats_table" id="defense_advanced" data-cols-to-freeze=",1">
    <caption>Advanced Defense Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Interceptions" data-stat="def_int" scope="col" class=" poptip center" data-tip="Passes intercepted on defense" >Int</th>
         <th aria-label="Tgt" data-stat="def_targets" scope="col" class=" poptip center" data-tip="Times targeted by a pass as a defender" >Tgt</th>
         <th aria-label="Cmp" data-stat="def_cmp" scope="col" class=" poptip center" data-tip="Completed passes when targeted" >Cmp</th>
         <th aria-label="Cmp%" data-stat="def_cmp_perc" scope="col" class=" poptip hide_non_quals center" data-tip="Completion percentage allowed on targets. 25 targets/16 game pace required for leaderboards." >Cmp%</th>
         <th aria-label="Yds" data-stat="def_cmp_yds" scope="col" class=" poptip center" data-tip="Receiving yards allowed on completions" >Yds</th>
         <th aria-label="Yds/Cmp" data-stat="def_yds_per_cmp" scope="col" class=" poptip hide_non_quals center" data-tip="Receiving yards per reception allowed. 25 targets/16 game pace required for leaderboards." >Yds/Cmp</th>
         <th aria-label="Yds/Tgt" data-stat="def_yds_per_target" scope="col" class=" poptip hide_non_quals center" data-tip="Receiving yards per time targeted. 25 targets/16 game pace required for leaderboards." >Yds/Tgt</th>
         <th aria-label="TD" data-stat="def_cmp_td" scope="col" class=" poptip center" data-tip="Receiving TDs allowed" >TD</th>
         <th aria-label="Rat" data-stat="def_pass_rating" scope="col" class=" poptip hide_non_quals center" data-tip="Pass rating allowed when targeted. 25 targets/16 game pace required for leaderboards." >Rat</th>
         <th aria-label="DADOT" data-stat="def_tgt_yds_per_att" scope="col" class=" poptip hide_non_quals center" data-tip="Average depth of target when targeted as a defender, whether completed or not. 25 targets/16 game pace required for leaderboards." >DADOT</th>
         <th aria-label="Air" data-stat="def_air_yds" scope="col" class=" poptip center" data-tip="Total air yards on completions" >Air</th>
         <th aria-label="YAC" data-stat="def_yac" scope="col" class=" poptip center" data-tip="Yards after catch on completions" >YAC</th>
         <th aria-label="Bltz" data-stat="blitzes" scope="col" class=" poptip center" data-tip="Times brought on a blitz of the QB" >Bltz</th>
         <th aria-label="Hrry" data-stat="qb_hurry" scope="col" class=" poptip center" data-tip="QB hurries (QB threw the ball earlier than intended or chased out of the pocket)" >Hrry</th>
         <th aria-label="QBKD" data-stat="qb_knockdown" scope="col" class=" poptip center" data-tip="QB knockdowns (QB hit the ground after the throw)" >QBKD</th>
         <th aria-label="Sacks" data-stat="sacks" scope="col" class=" poptip center" data-tip="Sacks (official since 1982,<br />based on play-by-play, game film<br />and other research since 1960)" data-filter="1" data-name="Sacks" >Sk</th>
         <th aria-label="Prss" data-stat="pressures" scope="col" class=" poptip center" data-tip="QB pressures (hurries + knockdowns + all sack plays (half and full for players, just full sacks for teams))" >Prss</th>
         <th aria-label="Tackles Combined" data-stat="tackles_combined" scope="col" class=" poptip center" data-tip="Tackles<br>Combined solo + assisted tackles<br />Prior to 1994, all tackles are put into 'combined', though<br />they are unofficial and inconsistently recorded from team to team. For amusement only." >Comb</th>
         <th aria-label="MTkl" data-stat="tackles_missed" scope="col" class=" poptip center" data-tip="Missed tackles" >MTkl</th>
         <th aria-label="MTkl%" data-stat="tackles_missed_pct" scope="col" class=" poptip hide_non_quals center" data-tip="Missed tackle percentage, missed tackles divided by missed + combined tackles. 25 tackles/16 game pace required for leaderboards." >MTkl%</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="IrviBr00" data-stat="player" ><a href="/players/I/IrviBr00.htm">Bruce Irvin</a></th><td class="left iz" data-stat="team" ></td><td class="right iz" data-stat="def_int" ></td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right " data-stat="qb_hurry" >2</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" ></td><td class="right " data-stat="pressures" >2</td><td class="right iz" data-stat="tackles_combined" ></td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" ></td></tr>
<tr ><th scope="row" class="left " data-append-csv="MoreFa00" data-stat="player" ><a href="/players/M/MoreFa00.htm">Fabian Moreau</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >7</td><td class="right " data-stat="def_cmp" >6</td><td class="right " data-stat="def_cmp_perc" >85.7%</td><td class="right " data-stat="def_cmp_yds" >74</td><td class="right " data-stat="def_yds_per_cmp" >12.3</td><td class="right " data-stat="def_yds_per_target" >10.6</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >110.7</td><td class="right " data-stat="def_tgt_yds_per_att" >8.4</td><td class="right " data-stat="def_air_yds" >55</td><td class="right " data-stat="def_yac" >19</td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >8</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >11.1%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JeweJo00" data-stat="player" ><a href="/players/J/JeweJo00.htm">Josey Jewell</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >5</td><td class="right " data-stat="def_cmp" >5</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >45</td><td class="right " data-stat="def_yds_per_cmp" >9.0</td><td class="right " data-stat="def_yds_per_target" >9.0</td><td class="right " data-stat="def_cmp_td" >1</td><td class="right " data-stat="def_pass_rating" >143.7</td><td class="right " data-stat="def_tgt_yds_per_att" >2.2</td><td class="right " data-stat="def_air_yds" >11</td><td class="right " data-stat="def_yac" >34</td><td class="right " data-stat="blitzes" >3</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >9</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >10.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LockPJ00" data-stat="player" ><a href="/players/L/LockPJ00.htm">P.J. Locke</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >5</td><td class="right " data-stat="def_cmp" >4</td><td class="right " data-stat="def_cmp_perc" >80.0%</td><td class="right " data-stat="def_cmp_yds" >66</td><td class="right " data-stat="def_yds_per_cmp" >16.5</td><td class="right " data-stat="def_yds_per_target" >13.2</td><td class="right " data-stat="def_cmp_td" >2</td><td class="right " data-stat="def_pass_rating" >158.3</td><td class="right " data-stat="def_tgt_yds_per_att" >10.2</td><td class="right " data-stat="def_air_yds" >42</td><td class="right " data-stat="def_yac" >24</td><td class="right " data-stat="blitzes" >1</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >4</td><td class="right " data-stat="tackles_missed" >4</td><td class="right " data-stat="tackles_missed_pct" >50.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SingAl00" data-stat="player" ><a href="/players/S/SingAl00.htm">Alex Singleton</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >2</td><td class="right " data-stat="def_cmp" >2</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >41</td><td class="right " data-stat="def_yds_per_cmp" >20.5</td><td class="right " data-stat="def_yds_per_target" >20.5</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >118.7</td><td class="right " data-stat="def_tgt_yds_per_att" >10.5</td><td class="right " data-stat="def_air_yds" >21</td><td class="right " data-stat="def_yac" >20</td><td class="right " data-stat="blitzes" >9</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >1</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_missed" >4</td><td class="right " data-stat="tackles_missed_pct" >44.4%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SurtPa01" data-stat="player" ><a href="/players/S/SurtPa01.htm">Patrick Surtain II</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >4</td><td class="right " data-stat="def_cmp" >2</td><td class="right " data-stat="def_cmp_perc" >50.0%</td><td class="right " data-stat="def_cmp_yds" >23</td><td class="right " data-stat="def_yds_per_cmp" >11.5</td><td class="right " data-stat="def_yds_per_target" >5.8</td><td class="right " data-stat="def_cmp_td" >1</td><td class="right " data-stat="def_pass_rating" >107.3</td><td class="right " data-stat="def_tgt_yds_per_att" >17.3</td><td class="right " data-stat="def_air_yds" >19</td><td class="right " data-stat="def_yac" >4</td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_missed" >2</td><td class="right " data-stat="tackles_missed_pct" >40.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McMiJa00" data-stat="player" ><a href="/players/M/McMiJa00.htm">Ja'Quan McMillian</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >3</td><td class="right " data-stat="def_cmp" >2</td><td class="right " data-stat="def_cmp_perc" >66.7%</td><td class="right " data-stat="def_cmp_yds" >18</td><td class="right " data-stat="def_yds_per_cmp" >9.0</td><td class="right " data-stat="def_yds_per_target" >6.0</td><td class="right " data-stat="def_cmp_td" >1</td><td class="right " data-stat="def_pass_rating" >122.2</td><td class="right " data-stat="def_tgt_yds_per_att" >6.7</td><td class="right " data-stat="def_air_yds" >7</td><td class="right " data-stat="def_yac" >11</td><td class="right " data-stat="blitzes" >2</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >25.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="CoopJo02" data-stat="player" ><a href="/players/C/CoopJo02.htm">Jonathon Cooper</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >1</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >4</td><td class="right " data-stat="def_yds_per_cmp" >4.0</td><td class="right " data-stat="def_yds_per_target" >4.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >83.3</td><td class="right " data-stat="def_tgt_yds_per_att" >-3.0</td><td class="right " data-stat="def_air_yds" >-3</td><td class="right " data-stat="def_yac" >7</td><td class="right iz" data-stat="blitzes" >0</td><td class="right " data-stat="qb_hurry" >1</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right " data-stat="sacks" >1.0</td><td class="right " data-stat="pressures" >2</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_missed" >2</td><td class="right " data-stat="tackles_missed_pct" >28.6%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoneD.01" data-stat="player" ><a href="/players/J/JoneD.01.htm">D.J. Jones</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >1</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >-7</td><td class="right " data-stat="def_yds_per_cmp" >-7.0</td><td class="right " data-stat="def_yds_per_target" >-7.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >79.2</td><td class="right " data-stat="def_tgt_yds_per_att" >-7.0</td><td class="right " data-stat="def_air_yds" >-7</td><td class="right iz" data-stat="def_yac" >0</td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right " data-stat="sacks" >1.0</td><td class="right " data-stat="pressures" >1</td><td class="right " data-stat="tackles_combined" >4</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >20.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SimmJu00" data-stat="player" ><a href="/players/S/SimmJu00.htm">Justin Simmons</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >3</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >33.3%</td><td class="right " data-stat="def_cmp_yds" >14</td><td class="right " data-stat="def_yds_per_cmp" >14.0</td><td class="right " data-stat="def_yds_per_target" >4.7</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >49.3</td><td class="right " data-stat="def_tgt_yds_per_att" >19.3</td><td class="right " data-stat="def_air_yds" >12</td><td class="right " data-stat="def_yac" >2</td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_missed" >2</td><td class="right " data-stat="tackles_missed_pct" >28.6%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SandDr00" data-stat="player" ><a href="/players/S/SandDr00.htm">Drew Sanders</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >2</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >50.0%</td><td class="right " data-stat="def_cmp_yds" >29</td><td class="right " data-stat="def_yds_per_cmp" >29.0</td><td class="right " data-stat="def_yds_per_target" >14.5</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >95.8</td><td class="right " data-stat="def_tgt_yds_per_att" >5.5</td><td class="right " data-stat="def_air_yds" >8</td><td class="right " data-stat="def_yac" >21</td><td class="right " data-stat="blitzes" >2</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BrowBa01" data-stat="player" ><a href="/players/B/BrowBa01.htm">Baron Browning</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >1</td><td class="right " data-stat="tackles_combined" >2</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PurcMi00" data-stat="player" ><a href="/players/P/PurcMi00.htm">Mike Purcell</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >1</td><td class="right " data-stat="tackles_combined" >3</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HarrJo05" data-stat="player" ><a href="/players/H/HarrJo05.htm">Jonathan Harris</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >1</td><td class="right " data-stat="tackles_combined" >5</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AlleZa01" data-stat="player" ><a href="/players/A/AlleZa01.htm">Zach Allen</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >1</td><td class="right iz" data-stat="tackles_combined" >0</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" ></td></tr>
<tr ><th scope="row" class="left " data-append-csv="HennMa01" data-stat="player" ><a href="/players/H/HennMa01.htm">Matt Henningsen</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >33.3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="IncoTh00" data-stat="player" ><a href="/players/I/IncoTh00.htm">Thomas Incoom</a></th><td class="left " data-stat="team" >DEN</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >50.0%</td></tr>

      
      <tr class="thead">
         <th aria-label="Player" data-stat="player" class=" sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Tm" data-stat="team" class=" sort_default_asc show_partial_when_sorting left" >Tm</th>
         <th aria-label="Interceptions" data-stat="def_int" class=" center" data-tip="Passes intercepted on defense" >Int</th>
         <th aria-label="Tgt" data-stat="def_targets" class=" center" data-tip="Times targeted by a pass as a defender" >Tgt</th>
         <th aria-label="Cmp" data-stat="def_cmp" class=" center" data-tip="Completed passes when targeted" >Cmp</th>
         <th aria-label="Cmp%" data-stat="def_cmp_perc" class=" hide_non_quals center" data-tip="Completion percentage allowed on targets. 25 targets/16 game pace required for leaderboards." >Cmp%</th>
         <th aria-label="Yds" data-stat="def_cmp_yds" class=" center" data-tip="Receiving yards allowed on completions" >Yds</th>
         <th aria-label="Yds/Cmp" data-stat="def_yds_per_cmp" class=" hide_non_quals center" data-tip="Receiving yards per reception allowed. 25 targets/16 game pace required for leaderboards." >Yds/Cmp</th>
         <th aria-label="Yds/Tgt" data-stat="def_yds_per_target" class=" hide_non_quals center" data-tip="Receiving yards per time targeted. 25 targets/16 game pace required for leaderboards." >Yds/Tgt</th>
         <th aria-label="TD" data-stat="def_cmp_td" class=" center" data-tip="Receiving TDs allowed" >TD</th>
         <th aria-label="Rat" data-stat="def_pass_rating" class=" hide_non_quals center" data-tip="Pass rating allowed when targeted. 25 targets/16 game pace required for leaderboards." >Rat</th>
         <th aria-label="DADOT" data-stat="def_tgt_yds_per_att" class=" hide_non_quals center" data-tip="Average depth of target when targeted as a defender, whether completed or not. 25 targets/16 game pace required for leaderboards." >DADOT</th>
         <th aria-label="Air" data-stat="def_air_yds" class=" center" data-tip="Total air yards on completions" >Air</th>
         <th aria-label="YAC" data-stat="def_yac" class=" center" data-tip="Yards after catch on completions" >YAC</th>
         <th aria-label="Bltz" data-stat="blitzes" class=" center" data-tip="Times brought on a blitz of the QB" >Bltz</th>
         <th aria-label="Hrry" data-stat="qb_hurry" class=" center" data-tip="QB hurries (QB threw the ball earlier than intended or chased out of the pocket)" >Hrry</th>
         <th aria-label="QBKD" data-stat="qb_knockdown" class=" center" data-tip="QB knockdowns (QB hit the ground after the throw)" >QBKD</th>
         <th aria-label="Sacks" data-stat="sacks" class=" center" data-tip="Sacks (official since 1982,<br />based on play-by-play, game film<br />and other research since 1960)" data-filter="1" data-name="Sacks" >Sk</th>
         <th aria-label="Prss" data-stat="pressures" class=" center" data-tip="QB pressures (hurries + knockdowns + all sack plays (half and full for players, just full sacks for teams))" >Prss</th>
         <th aria-label="Tackles Combined" data-stat="tackles_combined" class=" center" data-tip="Tackles<br>Combined solo + assisted tackles<br />Prior to 1994, all tackles are put into 'combined', though<br />they are unofficial and inconsistently recorded from team to team. For amusement only." >Comb</th>
         <th aria-label="MTkl" data-stat="tackles_missed" class=" center" data-tip="Missed tackles" >MTkl</th>
         <th aria-label="MTkl%" data-stat="tackles_missed_pct" class=" hide_non_quals center" data-tip="Missed tackle percentage, missed tackles divided by missed + combined tackles. 25 tackles/16 game pace required for leaderboards." >MTkl%</th>
      </tr>
      <tr ><th scope="row" class="left " data-append-csv="MeliIf00" data-stat="player" ><a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >10</td><td class="right " data-stat="def_cmp" >5</td><td class="right " data-stat="def_cmp_perc" >50.0%</td><td class="right " data-stat="def_cmp_yds" >63</td><td class="right " data-stat="def_yds_per_cmp" >12.6</td><td class="right " data-stat="def_yds_per_target" >6.3</td><td class="right " data-stat="def_cmp_td" >1</td><td class="right " data-stat="def_pass_rating" >103.3</td><td class="right " data-stat="def_tgt_yds_per_att" >8.5</td><td class="right " data-stat="def_air_yds" >45</td><td class="right " data-stat="def_yac" >18</td><td class="right " data-stat="blitzes" >4</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right " data-stat="sacks" >1.0</td><td class="right " data-stat="pressures" >2</td><td class="right " data-stat="tackles_combined" >9</td><td class="right " data-stat="tackles_missed" >2</td><td class="right " data-stat="tackles_missed_pct" >18.2%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AnzaAl00" data-stat="player" ><a href="/players/A/AnzaAl00.htm">Alex Anzalone</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >3</td><td class="right " data-stat="def_cmp" >3</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >21</td><td class="right " data-stat="def_yds_per_cmp" >7.0</td><td class="right " data-stat="def_yds_per_target" >7.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >95.8</td><td class="right " data-stat="def_tgt_yds_per_att" >2.0</td><td class="right " data-stat="def_air_yds" >6</td><td class="right " data-stat="def_yac" >15</td><td class="right " data-stat="blitzes" >14</td><td class="right " data-stat="qb_hurry" >1</td><td class="right " data-stat="qb_knockdown" >2</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >3</td><td class="right " data-stat="tackles_combined" >12</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >7.7%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="DorsKh00" data-stat="player" ><a href="/players/D/DorsKh00.htm">Khalil Dorsey</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >4</td><td class="right " data-stat="def_cmp" >2</td><td class="right " data-stat="def_cmp_perc" >50.0%</td><td class="right " data-stat="def_cmp_yds" >13</td><td class="right " data-stat="def_yds_per_cmp" >6.5</td><td class="right " data-stat="def_yds_per_target" >3.3</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >57.3</td><td class="right " data-stat="def_tgt_yds_per_att" >6.3</td><td class="right " data-stat="def_air_yds" >7</td><td class="right " data-stat="def_yac" >6</td><td class="right " data-stat="blitzes" >1</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BarnDe02" data-stat="player" ><a href="/players/B/BarnDe02.htm">Derrick Barnes</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >3</td><td class="right " data-stat="def_cmp" >2</td><td class="right " data-stat="def_cmp_perc" >66.7%</td><td class="right " data-stat="def_cmp_yds" >22</td><td class="right " data-stat="def_yds_per_cmp" >11.0</td><td class="right " data-stat="def_yds_per_target" >7.3</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >88.2</td><td class="right " data-stat="def_tgt_yds_per_att" >0.7</td><td class="right " data-stat="def_air_yds" >6</td><td class="right " data-stat="def_yac" >16</td><td class="right " data-stat="blitzes" >3</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >25.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SuttCa00" data-stat="player" ><a href="/players/S/SuttCa00.htm">Cameron Sutton</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >3</td><td class="right " data-stat="def_cmp" >2</td><td class="right " data-stat="def_cmp_perc" >66.7%</td><td class="right " data-stat="def_cmp_yds" >27</td><td class="right " data-stat="def_yds_per_cmp" >13.5</td><td class="right " data-stat="def_yds_per_target" >9.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >95.1</td><td class="right " data-stat="def_tgt_yds_per_att" >7.3</td><td class="right " data-stat="def_air_yds" >13</td><td class="right " data-stat="def_yac" >14</td><td class="right " data-stat="blitzes" >2</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >3</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BranBr00" data-stat="player" ><a href="/players/B/BranBr00.htm">Brian Branch</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >5</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >20.0%</td><td class="right " data-stat="def_cmp_yds" >40</td><td class="right " data-stat="def_yds_per_cmp" >40.0</td><td class="right " data-stat="def_yds_per_target" >8.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >60.4</td><td class="right " data-stat="def_tgt_yds_per_att" >7.6</td><td class="right " data-stat="def_air_yds" >9</td><td class="right " data-stat="def_yac" >31</td><td class="right " data-stat="blitzes" >3</td><td class="right " data-stat="qb_hurry" >1</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >2</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >33.3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PascJo00" data-stat="player" ><a href="/players/P/PascJo00.htm">Josh Paschal</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >1</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >-5</td><td class="right " data-stat="def_yds_per_cmp" >-5.0</td><td class="right " data-stat="def_yds_per_target" >-5.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >79.2</td><td class="right " data-stat="def_tgt_yds_per_att" >-8.0</td><td class="right " data-stat="def_air_yds" >-8</td><td class="right " data-stat="def_yac" >3</td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right " data-stat="sacks" >1.0</td><td class="right " data-stat="pressures" >1</td><td class="right " data-stat="tackles_combined" >3</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoseKe03" data-stat="player" ><a href="/players/J/JoseKe03.htm">Kerby Joseph</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >1</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >18</td><td class="right " data-stat="def_yds_per_cmp" >18.0</td><td class="right " data-stat="def_yds_per_target" >18.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >118.7</td><td class="right " data-stat="def_tgt_yds_per_att" >16.0</td><td class="right " data-stat="def_air_yds" >16</td><td class="right " data-stat="def_yac" >2</td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >4</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="OnwuLe00" data-stat="player" ><a href="/players/O/OnwuLe00.htm">Levi Onwuzurike</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >1</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >24</td><td class="right " data-stat="def_yds_per_cmp" >24.0</td><td class="right " data-stat="def_yds_per_target" >24.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >118.7</td><td class="right " data-stat="def_tgt_yds_per_att" >-1.0</td><td class="right " data-stat="def_air_yds" >-1</td><td class="right " data-stat="def_yac" >25</td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ReevJa00" data-stat="player" ><a href="/players/R/ReevJa00.htm">Jalen Reeves-Maybin</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >1</td><td class="right " data-stat="def_cmp" >1</td><td class="right " data-stat="def_cmp_perc" >100.0%</td><td class="right " data-stat="def_cmp_yds" >14</td><td class="right " data-stat="def_yds_per_cmp" >14.0</td><td class="right " data-stat="def_yds_per_target" >14.0</td><td class="right iz" data-stat="def_cmp_td" >0</td><td class="right " data-stat="def_pass_rating" >118.7</td><td class="right " data-stat="def_tgt_yds_per_att" >6.0</td><td class="right " data-stat="def_air_yds" >6</td><td class="right " data-stat="def_yac" >8</td><td class="right " data-stat="blitzes" >1</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >33.3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HutcAi00" data-stat="player" ><a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right " data-stat="qb_hurry" >2</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >3</td><td class="right " data-stat="tackles_combined" >4</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="VildKi00" data-stat="player" ><a href="/players/V/VildKi00.htm">Kindle Vildor</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right " data-stat="def_targets" >2</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" >0.0%</td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" >0.0</td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right " data-stat="def_pass_rating" >39.6</td><td class="right " data-stat="def_tgt_yds_per_att" >25.0</td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right " data-stat="blitzes" >1</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right " data-stat="qb_knockdown" >1</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right " data-stat="pressures" >1</td><td class="right iz" data-stat="tackles_combined" >0</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" ></td></tr>
<tr ><th scope="row" class="left " data-append-csv="ComiJo00" data-stat="player" ><a href="/players/C/ComiJo00.htm">John Cominsky</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >16.7%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="RodrMa00" data-stat="player" ><a href="/players/R/RodrMa00.htm">Malcolm Rodriguez</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right " data-stat="blitzes" >1</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >1</td><td class="right iz" data-stat="tackles_missed" >0</td><td class="right iz" data-stat="tackles_missed_pct" >0.0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="CampJa04" data-stat="player" ><a href="/players/C/CampJa04.htm">Jack Campbell</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right " data-stat="blitzes" >1</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >5</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >16.7%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BuggIs00" data-stat="player" ><a href="/players/B/BuggIs00.htm">Isaiah Buggs</a></th><td class="left " data-stat="team" >DET</td><td class="right iz" data-stat="def_int" >0</td><td class="right iz" data-stat="def_targets" >0</td><td class="right iz" data-stat="def_cmp" >0</td><td class="right iz" data-stat="def_cmp_perc" ></td><td class="right iz" data-stat="def_cmp_yds" ></td><td class="right iz" data-stat="def_yds_per_cmp" ></td><td class="right iz" data-stat="def_yds_per_target" ></td><td class="right iz" data-stat="def_cmp_td" ></td><td class="right iz" data-stat="def_pass_rating" ></td><td class="right iz" data-stat="def_tgt_yds_per_att" ></td><td class="right iz" data-stat="def_air_yds" ></td><td class="right iz" data-stat="def_yac" ></td><td class="right iz" data-stat="blitzes" >0</td><td class="right iz" data-stat="qb_hurry" >0</td><td class="right iz" data-stat="qb_knockdown" >0</td><td class="right iz" data-stat="sacks" >0.0</td><td class="right iz" data-stat="pressures" >0</td><td class="right " data-stat="tackles_combined" >2</td><td class="right " data-stat="tackles_missed" >1</td><td class="right " data-stat="tackles_missed_pct" >33.3%</td></tr>

</table>


</div>
-->
                </div>
                <div class="content_grid">
                    <div>
                        <div id="all_home_starters" class="table_wrapper setup_commented commented">
                            <div class="section_heading assoc_home_starters" id="home_starters_sh">
                                <span class="section_anchor" id="home_starters_link" data-label="Lions Starters"></span>
                                <h2>Lions Starters</h2>
                                <div class="section_heading_text">
                                    <ul></ul>
                                </div>
                            </div>
                            <div class="placeholder"></div>
                            <!--

<div class="table_container" id="div_home_starters">
    
    <table class="suppress_all sortable stats_table" id="home_starters" data-cols-to-freeze=",1">
    <caption>Lions Starters Table</caption>
    

   <colgroup><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Pos" data-stat="pos" scope="col" class=" poptip sort_default_asc left" data-tip="Position" >Pos</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="GoffJa00" data-stat="player" ><a href="/players/G/GoffJa00.htm">Jared Goff</a></th><td class="left " data-stat="pos" >QB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MontDa01" data-stat="player" ><a href="/players/M/MontDa01.htm">David Montgomery</a></th><td class="left " data-stat="pos" >RB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WillJa11" data-stat="player" ><a href="/players/W/WillJa11.htm">Jameson Williams</a></th><td class="left " data-stat="pos" >WR</td></tr>
<tr ><th scope="row" class="left " data-append-csv="StxxAm00" data-stat="player" ><a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a></th><td class="left " data-stat="pos" >WR</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WrigBr01" data-stat="player" ><a href="/players/W/WrigBr01.htm">Brock Wright</a></th><td class="left " data-stat="pos" >TE</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LaPoSa01" data-stat="player" ><a href="/players/L/LaPoSa01.htm">Sam LaPorta</a></th><td class="left " data-stat="pos" >TE</td></tr>
<tr ><th scope="row" class="left " data-append-csv="GlasGr00" data-stat="player" ><a href="/players/G/GlasGr00.htm">Graham Glasgow</a></th><td class="left " data-stat="pos" >OL</td></tr>
<tr ><th scope="row" class="left " data-append-csv="DeckTa00" data-stat="player" ><a href="/players/D/DeckTa00.htm">Taylor Decker</a></th><td class="left " data-stat="pos" >T</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SewePe00" data-stat="player" ><a href="/players/S/SewePe00.htm">Penei Sewell</a></th><td class="left " data-stat="pos" >T</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JackJo03" data-stat="player" ><a href="/players/J/JackJo03.htm">Jonah Jackson</a></th><td class="left " data-stat="pos" >G</td></tr>
<tr ><th scope="row" class="left " data-append-csv="RagnFr00" data-stat="player" ><a href="/players/R/RagnFr00.htm">Frank Ragnow</a></th><td class="left " data-stat="pos" >C</td></tr>
<tr class="divider" ><th scope="row" class="left " data-append-csv="BuggIs00" data-stat="player" ><a href="/players/B/BuggIs00.htm">Isaiah Buggs</a></th><td class="left " data-stat="pos" >DL</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HutcAi00" data-stat="player" ><a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a></th><td class="left " data-stat="pos" >DL</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoneBe03" data-stat="player" ><a href="/players/J/JoneBe03.htm">Benito Jones</a></th><td class="left " data-stat="pos" >DL</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PascJo00" data-stat="player" ><a href="/players/P/PascJo00.htm">Josh Paschal</a></th><td class="left " data-stat="pos" >DL</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BarnDe02" data-stat="player" ><a href="/players/B/BarnDe02.htm">Derrick Barnes</a></th><td class="left " data-stat="pos" >LB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AnzaAl00" data-stat="player" ><a href="/players/A/AnzaAl00.htm">Alex Anzalone</a></th><td class="left " data-stat="pos" >LB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="DorsKh00" data-stat="player" ><a href="/players/D/DorsKh00.htm">Khalil Dorsey</a></th><td class="left " data-stat="pos" >CB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SuttCa00" data-stat="player" ><a href="/players/S/SuttCa00.htm">Cameron Sutton</a></th><td class="left " data-stat="pos" >CB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MeliIf00" data-stat="player" ><a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a></th><td class="left " data-stat="pos" >S</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoseKe03" data-stat="player" ><a href="/players/J/JoseKe03.htm">Kerby Joseph</a></th><td class="left " data-stat="pos" >S</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BranBr00" data-stat="player" ><a href="/players/B/BranBr00.htm">Brian Branch</a></th><td class="left " data-stat="pos" >DB</td></tr>

</table>


</div>
-->
                        </div>
                    </div>
                    <div>
                        <div id="all_vis_starters" class="table_wrapper setup_commented commented">
                            <div class="section_heading assoc_vis_starters" id="vis_starters_sh">
                                <span class="section_anchor" id="vis_starters_link" data-label="Broncos Starters"></span>
                                <h2>Broncos Starters</h2>
                                <div class="section_heading_text">
                                    <ul></ul>
                                </div>
                            </div>
                            <div class="placeholder"></div>
                            <!--

<div class="table_container" id="div_vis_starters">
    
    <table class="suppress_all sortable stats_table" id="vis_starters" data-cols-to-freeze=",1">
    <caption>Broncos Starters Table</caption>
    

   <colgroup><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Pos" data-stat="pos" scope="col" class=" poptip sort_default_asc left" data-tip="Position" >Pos</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="WilsRu00" data-stat="player" ><a href="/players/W/WilsRu00.htm">Russell Wilson</a></th><td class="left " data-stat="pos" >QB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McLaJa00" data-stat="player" ><a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a></th><td class="left " data-stat="pos" >RB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SuttCo00" data-stat="player" ><a href="/players/S/SuttCo00.htm">Courtland Sutton</a></th><td class="left " data-stat="pos" >WR</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HumpLi01" data-stat="player" ><a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a></th><td class="left " data-stat="pos" >WR</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JeudJe00" data-stat="player" ><a href="/players/J/JeudJe00.htm">Jerry Jeudy</a></th><td class="left " data-stat="pos" >WR</td></tr>
<tr ><th scope="row" class="left " data-append-csv="TrauAd00" data-stat="player" ><a href="/players/T/TrauAd00.htm">Adam Trautman</a></th><td class="left " data-stat="pos" >TE</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MeinQu02" data-stat="player" ><a href="/players/M/MeinQu02.htm">Quinn Meinerz</a></th><td class="left " data-stat="pos" >OL</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BollGa00" data-stat="player" ><a href="/players/B/BollGa00.htm">Garett Bolles</a></th><td class="left " data-stat="pos" >T</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McGlMi00" data-stat="player" ><a href="/players/M/McGlMi00.htm">Mike McGlinchey</a></th><td class="left " data-stat="pos" >T</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PoweBe00" data-stat="player" ><a href="/players/P/PoweBe00.htm">Ben Powers</a></th><td class="left " data-stat="pos" >G</td></tr>
<tr ><th scope="row" class="left " data-append-csv="CushLl00" data-stat="player" ><a href="/players/C/CushLl00.htm">Lloyd Cushenberry III</a></th><td class="left " data-stat="pos" >C</td></tr>
<tr class="divider" ><th scope="row" class="left " data-append-csv="PurcMi00" data-stat="player" ><a href="/players/P/PurcMi00.htm">Mike Purcell</a></th><td class="left " data-stat="pos" >DL</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AlleZa01" data-stat="player" ><a href="/players/A/AlleZa01.htm">Zach Allen</a></th><td class="left " data-stat="pos" >DE</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoneD.01" data-stat="player" ><a href="/players/J/JoneD.01.htm">D.J. Jones</a></th><td class="left " data-stat="pos" >DT</td></tr>
<tr ><th scope="row" class="left " data-append-csv="CoopJo02" data-stat="player" ><a href="/players/C/CoopJo02.htm">Jonathon Cooper</a></th><td class="left " data-stat="pos" >OLB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BrowBa01" data-stat="player" ><a href="/players/B/BrowBa01.htm">Baron Browning</a></th><td class="left " data-stat="pos" >OLB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JeweJo00" data-stat="player" ><a href="/players/J/JeweJo00.htm">Josey Jewell</a></th><td class="left " data-stat="pos" >LB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SingAl00" data-stat="player" ><a href="/players/S/SingAl00.htm">Alex Singleton</a></th><td class="left " data-stat="pos" >LB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MoreFa00" data-stat="player" ><a href="/players/M/MoreFa00.htm">Fabian Moreau</a></th><td class="left " data-stat="pos" >CB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SurtPa01" data-stat="player" ><a href="/players/S/SurtPa01.htm">Patrick Surtain II</a></th><td class="left " data-stat="pos" >CB</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LockPJ00" data-stat="player" ><a href="/players/L/LockPJ00.htm">P.J. Locke</a></th><td class="left " data-stat="pos" >S</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SimmJu00" data-stat="player" ><a href="/players/S/SimmJu00.htm">Justin Simmons</a></th><td class="left " data-stat="pos" >S</td></tr>

</table>


</div>
-->
                        </div>
                    </div>
                </div>
                <div class="content_grid">
                    <div>
                        <div id="all_home_snap_counts" class="table_wrapper setup_commented commented">
                            <div class="section_heading assoc_home_snap_counts" id="home_snap_counts_sh">
                                <span class="section_anchor" id="home_snap_counts_link" data-label="Lions Snap Counts"></span>
                                <h2>Lions Snap Counts</h2>
                                <div class="section_heading_text">
                                    <ul></ul>
                                </div>
                            </div>
                            <div class="placeholder"></div>
                            <!--

<div class="table_container" id="div_home_snap_counts">
    
    <table class="sortable stats_table" id="home_snap_counts" data-cols-to-freeze=",1">
    <caption>Lions Snap Counts Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col></colgroup>
   <thead>

      
      <tr class="over_header">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="offense_snaps" colspan="2" class=" over_header center" >Off.</th>
         <th aria-label="" data-stat="defense_snaps" colspan="2" class=" over_header center" >Def.</th>
         <th aria-label="" data-stat="special_teams_snaps" colspan="2" class=" over_header center" >ST</th>
      </tr>
            
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Pos" data-stat="pos" scope="col" class=" poptip sort_default_asc left" data-tip="Position" >Pos</th>
         <th aria-label="Num" data-stat="offense" scope="col" class=" poptip center" data-over-header="Off." >Num</th>
         <th aria-label="Pct" data-stat="off_pct" scope="col" class=" poptip center" data-tip="Percentage of available offensive snaps taken for games in which this player appeared." data-over-header="Off." >Pct</th>
         <th aria-label="Num" data-stat="defense" scope="col" class=" poptip center" data-over-header="Def." >Num</th>
         <th aria-label="Pct" data-stat="def_pct" scope="col" class=" poptip center" data-tip="Percentage of available defensive snaps taken for games in which this player appeared." data-over-header="Def." >Pct</th>
         <th aria-label="Num" data-stat="special_teams" scope="col" class=" poptip center" data-over-header="ST" >Num</th>
         <th aria-label="Pct" data-stat="st_pct" scope="col" class=" poptip center" data-tip="Percentage of available special teams snaps taken for games in which this player appeared." data-over-header="ST" >Pct</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="SewePe00" data-stat="player" ><a href="/players/S/SewePe00.htm">Penei Sewell</a></th><td class="left " data-stat="pos" >T</td><td class="right " data-stat="offense" >66</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="GlasGr00" data-stat="player" ><a href="/players/G/GlasGr00.htm">Graham Glasgow</a></th><td class="left " data-stat="pos" >G</td><td class="right " data-stat="offense" >66</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="RagnFr00" data-stat="player" ><a href="/players/R/RagnFr00.htm">Frank Ragnow</a></th><td class="left " data-stat="pos" >C</td><td class="right " data-stat="offense" >66</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="DeckTa00" data-stat="player" ><a href="/players/D/DeckTa00.htm">Taylor Decker</a></th><td class="left " data-stat="pos" >T</td><td class="right " data-stat="offense" >66</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JackJo03" data-stat="player" ><a href="/players/J/JackJo03.htm">Jonah Jackson</a></th><td class="left " data-stat="pos" >G</td><td class="right " data-stat="offense" >66</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="GoffJa00" data-stat="player" ><a href="/players/G/GoffJa00.htm">Jared Goff</a></th><td class="left " data-stat="pos" >QB</td><td class="right " data-stat="offense" >66</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LaPoSa01" data-stat="player" ><a href="/players/L/LaPoSa01.htm">Sam LaPorta</a></th><td class="left " data-stat="pos" >TE</td><td class="right " data-stat="offense" >63</td><td class="right " data-stat="off_pct" >95%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="StxxAm00" data-stat="player" ><a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >61</td><td class="right " data-stat="off_pct" >92%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >2</td><td class="right " data-stat="st_pct" >7%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WillJa11" data-stat="player" ><a href="/players/W/WillJa11.htm">Jameson Williams</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >45</td><td class="right " data-stat="off_pct" >68%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ReynJo00" data-stat="player" ><a href="/players/R/ReynJo00.htm">Josh Reynolds</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >38</td><td class="right " data-stat="off_pct" >58%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MontDa01" data-stat="player" ><a href="/players/M/MontDa01.htm">David Montgomery</a></th><td class="left " data-stat="pos" >RB</td><td class="right " data-stat="offense" >34</td><td class="right " data-stat="off_pct" >52%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="GibbJa01" data-stat="player" ><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a></th><td class="left " data-stat="pos" >RB</td><td class="right " data-stat="offense" >32</td><td class="right " data-stat="off_pct" >48%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="RaymKa00" data-stat="player" ><a href="/players/R/RaymKa00.htm">Kalif Raymond</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >20</td><td class="right " data-stat="off_pct" >30%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >7</td><td class="right " data-stat="st_pct" >24%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WrigBr01" data-stat="player" ><a href="/players/W/WrigBr01.htm">Brock Wright</a></th><td class="left " data-stat="pos" >TE</td><td class="right " data-stat="offense" >12</td><td class="right " data-stat="off_pct" >18%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >8</td><td class="right " data-stat="st_pct" >28%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PeopDo00" data-stat="player" ><a href="/players/P/PeopDo00.htm">Donovan Peoples-Jones</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >11</td><td class="right " data-stat="off_pct" >17%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SkipDa00" data-stat="player" ><a href="/players/S/SkipDa00.htm">Dan Skipper</a></th><td class="left " data-stat="pos" >T</td><td class="right " data-stat="offense" >8</td><td class="right " data-stat="off_pct" >12%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MitcJa00" data-stat="player" ><a href="/players/M/MitcJa00.htm">James Mitchell</a></th><td class="left " data-stat="pos" >TE</td><td class="right " data-stat="offense" >6</td><td class="right " data-stat="off_pct" >9%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >16</td><td class="right " data-stat="st_pct" >55%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AnzaAl00" data-stat="player" ><a href="/players/A/AnzaAl00.htm">Alex Anzalone</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >64</td><td class="right " data-stat="def_pct" >100%</td><td class="right " data-stat="special_teams" >1</td><td class="right " data-stat="st_pct" >3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoseKe03" data-stat="player" ><a href="/players/J/JoseKe03.htm">Kerby Joseph</a></th><td class="left " data-stat="pos" >FS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >62</td><td class="right " data-stat="def_pct" >97%</td><td class="right " data-stat="special_teams" >8</td><td class="right " data-stat="st_pct" >28%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MeliIf00" data-stat="player" ><a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >62</td><td class="right " data-stat="def_pct" >97%</td><td class="right " data-stat="special_teams" >7</td><td class="right " data-stat="st_pct" >24%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SuttCa00" data-stat="player" ><a href="/players/S/SuttCa00.htm">Cameron Sutton</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >62</td><td class="right " data-stat="def_pct" >97%</td><td class="right " data-stat="special_teams" >2</td><td class="right " data-stat="st_pct" >7%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HutcAi00" data-stat="player" ><a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a></th><td class="left " data-stat="pos" >DE</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >59</td><td class="right " data-stat="def_pct" >92%</td><td class="right " data-stat="special_teams" >1</td><td class="right " data-stat="st_pct" >3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BranBr00" data-stat="player" ><a href="/players/B/BranBr00.htm">Brian Branch</a></th><td class="left " data-stat="pos" >SS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >46</td><td class="right " data-stat="def_pct" >72%</td><td class="right " data-stat="special_teams" >5</td><td class="right " data-stat="st_pct" >17%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ComiJo00" data-stat="player" ><a href="/players/C/ComiJo00.htm">John Cominsky</a></th><td class="left " data-stat="pos" >DE</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >46</td><td class="right " data-stat="def_pct" >72%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="DorsKh00" data-stat="player" ><a href="/players/D/DorsKh00.htm">Khalil Dorsey</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >44</td><td class="right " data-stat="def_pct" >69%</td><td class="right " data-stat="special_teams" >8</td><td class="right " data-stat="st_pct" >28%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PascJo00" data-stat="player" ><a href="/players/P/PascJo00.htm">Josh Paschal</a></th><td class="left " data-stat="pos" >DE</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >43</td><td class="right " data-stat="def_pct" >67%</td><td class="right " data-stat="special_teams" >4</td><td class="right " data-stat="st_pct" >14%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BarnDe02" data-stat="player" ><a href="/players/B/BarnDe02.htm">Derrick Barnes</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >35</td><td class="right " data-stat="def_pct" >55%</td><td class="right " data-stat="special_teams" >7</td><td class="right " data-stat="st_pct" >24%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="CampJa04" data-stat="player" ><a href="/players/C/CampJa04.htm">Jack Campbell</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >33</td><td class="right " data-stat="def_pct" >52%</td><td class="right " data-stat="special_teams" >14</td><td class="right " data-stat="st_pct" >48%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoneBe03" data-stat="player" ><a href="/players/J/JoneBe03.htm">Benito Jones</a></th><td class="left " data-stat="pos" >DT</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >30</td><td class="right " data-stat="def_pct" >47%</td><td class="right " data-stat="special_teams" >9</td><td class="right " data-stat="st_pct" >31%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BuggIs00" data-stat="player" ><a href="/players/B/BuggIs00.htm">Isaiah Buggs</a></th><td class="left " data-stat="pos" >DT</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >23</td><td class="right " data-stat="def_pct" >36%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="OkwaRo01" data-stat="player" ><a href="/players/O/OkwaRo01.htm">Romeo Okwara</a></th><td class="left " data-stat="pos" >DE</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >18</td><td class="right " data-stat="def_pct" >28%</td><td class="right " data-stat="special_teams" >7</td><td class="right " data-stat="st_pct" >24%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="VildKi00" data-stat="player" ><a href="/players/V/VildKi00.htm">Kindle Vildor</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >18</td><td class="right " data-stat="def_pct" >28%</td><td class="right " data-stat="special_teams" >5</td><td class="right " data-stat="st_pct" >17%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="OnwuLe00" data-stat="player" ><a href="/players/O/OnwuLe00.htm">Levi Onwuzurike</a></th><td class="left " data-stat="pos" >DE</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >14</td><td class="right " data-stat="def_pct" >22%</td><td class="right " data-stat="special_teams" >1</td><td class="right " data-stat="st_pct" >3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="IrviBr00" data-stat="player" ><a href="/players/I/IrviBr00.htm">Bruce Irvin</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >13</td><td class="right " data-stat="def_pct" >20%</td><td class="right " data-stat="special_teams" >1</td><td class="right " data-stat="st_pct" >3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MartBr00" data-stat="player" ><a href="/players/M/MartBr00.htm">Brodric Martin</a></th><td class="left " data-stat="pos" >DT</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >11</td><td class="right " data-stat="def_pct" >17%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ReevJa00" data-stat="player" ><a href="/players/R/ReevJa00.htm">Jalen Reeves-Maybin</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >10</td><td class="right " data-stat="def_pct" >16%</td><td class="right " data-stat="special_teams" >22</td><td class="right " data-stat="st_pct" >76%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="RodrMa00" data-stat="player" ><a href="/players/R/RodrMa00.htm">Malcolm Rodriguez</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >5</td><td class="right " data-stat="def_pct" >8%</td><td class="right " data-stat="special_teams" >22</td><td class="right " data-stat="st_pct" >76%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PittAn01" data-stat="player" ><a href="/players/P/PittAn01.htm">Anthony Pittman</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >4</td><td class="right " data-stat="def_pct" >6%</td><td class="right " data-stat="special_teams" >20</td><td class="right " data-stat="st_pct" >69%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HarrWi02" data-stat="player" ><a href="/players/H/HarrWi02.htm">Will Harris</a></th><td class="left " data-stat="pos" >SS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >2</td><td class="right " data-stat="def_pct" >3%</td><td class="right " data-stat="special_teams" >22</td><td class="right " data-stat="st_pct" >76%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ReynCr00" data-stat="player" ><a href="/players/R/ReynCr00.htm">Craig Reynolds</a></th><td class="left " data-stat="pos" >RB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >17</td><td class="right " data-stat="st_pct" >59%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="FoxxJa01" data-stat="player" ><a href="/players/F/FoxxJa01.htm">Jack Fox</a></th><td class="left " data-stat="pos" >P</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >17</td><td class="right " data-stat="st_pct" >59%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WalkTr01" data-stat="player" ><a href="/players/W/WalkTr01.htm">Tracy Walker</a></th><td class="left " data-stat="pos" >FS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >15</td><td class="right " data-stat="st_pct" >52%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JacoJe00" data-stat="player" ><a href="/players/J/JacoJe00.htm">Jerry Jacobs</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >13</td><td class="right " data-stat="st_pct" >45%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McQuJa00" data-stat="player" ><a href="/players/M/McQuJa00.htm">Jake McQuaide</a></th><td class="left " data-stat="pos" >LS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >10</td><td class="right " data-stat="st_pct" >34%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SorsCo00" data-stat="player" ><a href="/players/S/SorsCo00.htm">Colby Sorsdal</a></th><td class="left " data-stat="pos" >G</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BadgMi00" data-stat="player" ><a href="/players/B/BadgMi00.htm">Michael Badgley</a></th><td class="left " data-stat="pos" >K</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AwosKa00" data-stat="player" ><a href="/players/A/AwosKa00.htm">Kayode Awosika</a></th><td class="left " data-stat="pos" >T</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>

</table>


</div>
-->
                        </div>
                    </div>
                    <div>
                        <div id="all_vis_snap_counts" class="table_wrapper setup_commented commented">
                            <div class="section_heading assoc_vis_snap_counts" id="vis_snap_counts_sh">
                                <span class="section_anchor" id="vis_snap_counts_link" data-label="Broncos Snap Counts"></span>
                                <h2>Broncos Snap Counts</h2>
                                <div class="section_heading_text">
                                    <ul></ul>
                                </div>
                            </div>
                            <div class="placeholder"></div>
                            <!--

<div class="table_container" id="div_vis_snap_counts">
    
    <table class="sortable stats_table" id="vis_snap_counts" data-cols-to-freeze=",1">
    <caption>Broncos Snap Counts Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col></colgroup>
   <thead>

      
      <tr class="over_header">
         <th aria-label="" data-stat="" colspan="2" class=" over_header center" ></th>
         <th aria-label="" data-stat="offense_snaps" colspan="2" class=" over_header center" >Off.</th>
         <th aria-label="" data-stat="defense_snaps" colspan="2" class=" over_header center" >Def.</th>
         <th aria-label="" data-stat="special_teams_snaps" colspan="2" class=" over_header center" >ST</th>
      </tr>
            
      <tr>
         <th aria-label="Player" data-stat="player" scope="col" class=" poptip sort_default_asc show_partial_when_sorting left" >Player</th>
         <th aria-label="Pos" data-stat="pos" scope="col" class=" poptip sort_default_asc left" data-tip="Position" >Pos</th>
         <th aria-label="Num" data-stat="offense" scope="col" class=" poptip center" data-over-header="Off." >Num</th>
         <th aria-label="Pct" data-stat="off_pct" scope="col" class=" poptip center" data-tip="Percentage of available offensive snaps taken for games in which this player appeared." data-over-header="Off." >Pct</th>
         <th aria-label="Num" data-stat="defense" scope="col" class=" poptip center" data-over-header="Def." >Num</th>
         <th aria-label="Pct" data-stat="def_pct" scope="col" class=" poptip center" data-tip="Percentage of available defensive snaps taken for games in which this player appeared." data-over-header="Def." >Pct</th>
         <th aria-label="Num" data-stat="special_teams" scope="col" class=" poptip center" data-over-header="ST" >Num</th>
         <th aria-label="Pct" data-stat="st_pct" scope="col" class=" poptip center" data-tip="Percentage of available special teams snaps taken for games in which this player appeared." data-over-header="ST" >Pct</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="left " data-append-csv="BollGa00" data-stat="player" ><a href="/players/B/BollGa00.htm">Garett Bolles</a></th><td class="left " data-stat="pos" >T</td><td class="right " data-stat="offense" >64</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PoweBe00" data-stat="player" ><a href="/players/P/PoweBe00.htm">Ben Powers</a></th><td class="left " data-stat="pos" >G</td><td class="right " data-stat="offense" >64</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MeinQu02" data-stat="player" ><a href="/players/M/MeinQu02.htm">Quinn Meinerz</a></th><td class="left " data-stat="pos" >G</td><td class="right " data-stat="offense" >64</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="CushLl00" data-stat="player" ><a href="/players/C/CushLl00.htm">Lloyd Cushenberry III</a></th><td class="left " data-stat="pos" >C</td><td class="right " data-stat="offense" >64</td><td class="right " data-stat="off_pct" >100%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McGlMi00" data-stat="player" ><a href="/players/M/McGlMi00.htm">Mike McGlinchey</a></th><td class="left " data-stat="pos" >T</td><td class="right " data-stat="offense" >61</td><td class="right " data-stat="off_pct" >95%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WilsRu00" data-stat="player" ><a href="/players/W/WilsRu00.htm">Russell Wilson</a></th><td class="left " data-stat="pos" >QB</td><td class="right " data-stat="offense" >60</td><td class="right " data-stat="off_pct" >94%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SuttCo00" data-stat="player" ><a href="/players/S/SuttCo00.htm">Courtland Sutton</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >60</td><td class="right " data-stat="off_pct" >94%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JeudJe00" data-stat="player" ><a href="/players/J/JeudJe00.htm">Jerry Jeudy</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >40</td><td class="right " data-stat="off_pct" >63%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HumpLi01" data-stat="player" ><a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >37</td><td class="right " data-stat="off_pct" >58%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WillJa10" data-stat="player" ><a href="/players/W/WillJa10.htm">Javonte Williams</a></th><td class="left " data-stat="pos" >RB</td><td class="right " data-stat="offense" >31</td><td class="right " data-stat="off_pct" >48%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="TrauAd00" data-stat="player" ><a href="/players/T/TrauAd00.htm">Adam Trautman</a></th><td class="left " data-stat="pos" >TE</td><td class="right " data-stat="offense" >30</td><td class="right " data-stat="off_pct" >47%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >7</td><td class="right " data-stat="st_pct" >24%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="KrulLu00" data-stat="player" ><a href="/players/K/KrulLu00.htm">Lucas Krull</a></th><td class="left " data-stat="pos" >TE</td><td class="right " data-stat="offense" >29</td><td class="right " data-stat="off_pct" >45%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >7</td><td class="right " data-stat="st_pct" >24%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MimsMa00" data-stat="player" ><a href="/players/M/MimsMa00.htm">Marvin Mims</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >27</td><td class="right " data-stat="off_pct" >42%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >11</td><td class="right " data-stat="st_pct" >38%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PeriSa00" data-stat="player" ><a href="/players/P/PeriSa00.htm">Samaje Perine</a></th><td class="left " data-stat="pos" >RB</td><td class="right " data-stat="offense" >25</td><td class="right " data-stat="off_pct" >39%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="ManhCh00" data-stat="player" ><a href="/players/M/ManhCh00.htm">Chris Manhertz</a></th><td class="left " data-stat="pos" >TE</td><td class="right " data-stat="offense" >16</td><td class="right " data-stat="off_pct" >25%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >9</td><td class="right " data-stat="st_pct" >31%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BurtMi00" data-stat="player" ><a href="/players/B/BurtMi00.htm">Michael Burton</a></th><td class="left " data-stat="pos" >FB</td><td class="right " data-stat="offense" >9</td><td class="right " data-stat="off_pct" >14%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >17</td><td class="right " data-stat="st_pct" >59%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McLaJa00" data-stat="player" ><a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a></th><td class="left " data-stat="pos" >RB</td><td class="right " data-stat="offense" >8</td><td class="right " data-stat="off_pct" >13%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >4</td><td class="right " data-stat="st_pct" >14%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BailQu00" data-stat="player" ><a href="/players/B/BailQu00.htm">Quinn Bailey</a></th><td class="left " data-stat="pos" >G</td><td class="right " data-stat="offense" >4</td><td class="right " data-stat="off_pct" >6%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="StidJa00" data-stat="player" ><a href="/players/S/StidJa00.htm">Jarrett Stidham</a></th><td class="left " data-stat="pos" >QB</td><td class="right " data-stat="offense" >4</td><td class="right " data-stat="off_pct" >6%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JohnBr23" data-stat="player" ><a href="/players/J/JohnBr23.htm">Brandon Johnson</a></th><td class="left " data-stat="pos" >WR</td><td class="right " data-stat="offense" >4</td><td class="right " data-stat="off_pct" >6%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="FlemCa00" data-stat="player" ><a href="/players/F/FlemCa00.htm">Cameron Fleming</a></th><td class="left " data-stat="pos" >T</td><td class="right " data-stat="offense" >3</td><td class="right " data-stat="off_pct" >5%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SurtPa01" data-stat="player" ><a href="/players/S/SurtPa01.htm">Patrick Surtain II</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >66</td><td class="right " data-stat="def_pct" >100%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SimmJu00" data-stat="player" ><a href="/players/S/SimmJu00.htm">Justin Simmons</a></th><td class="left " data-stat="pos" >FS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >66</td><td class="right " data-stat="def_pct" >100%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SingAl00" data-stat="player" ><a href="/players/S/SingAl00.htm">Alex Singleton</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >66</td><td class="right " data-stat="def_pct" >100%</td><td class="right " data-stat="special_teams" >1</td><td class="right " data-stat="st_pct" >3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MoreFa00" data-stat="player" ><a href="/players/M/MoreFa00.htm">Fabian Moreau</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >66</td><td class="right " data-stat="def_pct" >100%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="BrowBa01" data-stat="player" ><a href="/players/B/BrowBa01.htm">Baron Browning</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >60</td><td class="right " data-stat="def_pct" >91%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="CoopJo02" data-stat="player" ><a href="/players/C/CoopJo02.htm">Jonathon Cooper</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >56</td><td class="right " data-stat="def_pct" >85%</td><td class="right " data-stat="special_teams" >8</td><td class="right " data-stat="st_pct" >28%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LockPJ00" data-stat="player" ><a href="/players/L/LockPJ00.htm">P.J. Locke</a></th><td class="left " data-stat="pos" >FS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >56</td><td class="right " data-stat="def_pct" >85%</td><td class="right " data-stat="special_teams" >5</td><td class="right " data-stat="st_pct" >17%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="AlleZa01" data-stat="player" ><a href="/players/A/AlleZa01.htm">Zach Allen</a></th><td class="left " data-stat="pos" >DE</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >48</td><td class="right " data-stat="def_pct" >73%</td><td class="right " data-stat="special_teams" >9</td><td class="right " data-stat="st_pct" >31%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JeweJo00" data-stat="player" ><a href="/players/J/JeweJo00.htm">Josey Jewell</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >47</td><td class="right " data-stat="def_pct" >71%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="McMiJa00" data-stat="player" ><a href="/players/M/McMiJa00.htm">Ja'Quan McMillian</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >46</td><td class="right " data-stat="def_pct" >70%</td><td class="right " data-stat="special_teams" >1</td><td class="right " data-stat="st_pct" >3%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="PurcMi00" data-stat="player" ><a href="/players/P/PurcMi00.htm">Mike Purcell</a></th><td class="left " data-stat="pos" >NT</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >38</td><td class="right " data-stat="def_pct" >58%</td><td class="right " data-stat="special_teams" >9</td><td class="right " data-stat="st_pct" >31%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="JoneD.01" data-stat="player" ><a href="/players/J/JoneD.01.htm">D.J. Jones</a></th><td class="left " data-stat="pos" >NT</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >35</td><td class="right " data-stat="def_pct" >53%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HarrJo05" data-stat="player" ><a href="/players/H/HarrJo05.htm">Jonathan Harris</a></th><td class="left " data-stat="pos" >DE</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >28</td><td class="right " data-stat="def_pct" >42%</td><td class="right " data-stat="special_teams" >6</td><td class="right " data-stat="st_pct" >21%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="HennMa01" data-stat="player" ><a href="/players/H/HennMa01.htm">Matt Henningsen</a></th><td class="left " data-stat="pos" >DE</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >17</td><td class="right " data-stat="def_pct" >26%</td><td class="right " data-stat="special_teams" >13</td><td class="right " data-stat="st_pct" >45%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SandDr00" data-stat="player" ><a href="/players/S/SandDr00.htm">Drew Sanders</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >11</td><td class="right " data-stat="def_pct" >17%</td><td class="right " data-stat="special_teams" >20</td><td class="right " data-stat="st_pct" >69%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LancTy00" data-stat="player" ><a href="/players/L/LancTy00.htm">Tyler Lancaster</a></th><td class="left " data-stat="pos" >NT</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >11</td><td class="right " data-stat="def_pct" >17%</td><td class="right iz" data-stat="special_teams" >0</td><td class="right iz" data-stat="st_pct" >0%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="IncoTh00" data-stat="player" ><a href="/players/I/IncoTh00.htm">Thomas Incoom</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >7</td><td class="right " data-stat="def_pct" >11%</td><td class="right " data-stat="special_teams" >8</td><td class="right " data-stat="st_pct" >28%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="TurnDe02" data-stat="player" ><a href="/players/T/TurnDe02.htm">Delarrin Turner-Yell</a></th><td class="left " data-stat="pos" >FS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >1</td><td class="right " data-stat="def_pct" >2%</td><td class="right " data-stat="special_teams" >25</td><td class="right " data-stat="st_pct" >86%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MossRi00" data-stat="player" ><a href="/players/M/MossRi00.htm">Riley Moss</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right " data-stat="defense" >1</td><td class="right " data-stat="def_pct" >2%</td><td class="right " data-stat="special_teams" >20</td><td class="right " data-stat="st_pct" >69%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="StrnJu00" data-stat="player" ><a href="/players/S/StrnJu00.htm">Justin Strnad</a></th><td class="left " data-stat="pos" >LB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >26</td><td class="right " data-stat="st_pct" >90%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="SmitTr04" data-stat="player" ><a href="/players/S/SmitTr04.htm">Tremon Smith</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >25</td><td class="right " data-stat="st_pct" >86%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WashDw00" data-stat="player" ><a href="/players/W/WashDw00.htm">Dwayne Washington</a></th><td class="left " data-stat="pos" >RB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >20</td><td class="right " data-stat="st_pct" >69%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="FrabMi00" data-stat="player" ><a href="/players/F/FrabMi00.htm">Mitchell Fraboni</a></th><td class="left " data-stat="pos" >LS</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >8</td><td class="right " data-stat="st_pct" >28%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="DixoRi00" data-stat="player" ><a href="/players/D/DixoRi00.htm">Riley Dixon</a></th><td class="left " data-stat="pos" >P</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >8</td><td class="right " data-stat="st_pct" >28%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="LutzWi00" data-stat="player" ><a href="/players/L/LutzWi00.htm">Wil Lutz</a></th><td class="left " data-stat="pos" >K</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >7</td><td class="right " data-stat="st_pct" >24%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="MathDa00" data-stat="player" ><a href="/players/M/MathDa00.htm">Damarri Mathis</a></th><td class="left " data-stat="pos" >CB</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >5</td><td class="right " data-stat="st_pct" >17%</td></tr>
<tr ><th scope="row" class="left " data-append-csv="WattLu00" data-stat="player" ><a href="/players/W/WattLu00.htm">Luke Wattenberg</a></th><td class="left " data-stat="pos" >C</td><td class="right iz" data-stat="offense" >0</td><td class="right iz" data-stat="off_pct" >0%</td><td class="right iz" data-stat="defense" >0</td><td class="right iz" data-stat="def_pct" >0%</td><td class="right " data-stat="special_teams" >3</td><td class="right " data-stat="st_pct" >10%</td></tr>

</table>


</div>
-->
                        </div>
                    </div>
                </div>
                <div class="content_grid">
                    <div>
                        <div id="all_home_drives" class="table_wrapper setup_commented commented">
                            <div class="section_heading assoc_home_drives" id="home_drives_sh">
                                <span class="section_anchor" id="home_drives_link" data-label="Lions Drives"></span>
                                <h2>Lions Drives</h2>
                                <div class="section_heading_text">
                                    <ul></ul>
                                </div>
                            </div>
                            <div class="placeholder"></div>
                            <!--

<div class="table_container" id="div_home_drives">
    
    <table class="sortable stats_table" id="home_drives" data-cols-to-freeze=",1">
    <caption>Lions Drives Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="#" data-stat="drive_num" scope="col" class=" poptip center" >#</th>
         <th aria-label="Quarter" data-stat="quarter" scope="col" class=" poptip center" >Quarter</th>
         <th aria-label="Time" data-stat="time_start" scope="col" class=" poptip center" >Time</th>
         <th aria-label="LOS" data-stat="start_at" scope="col" class=" poptip center" >LOS</th>
         <th aria-label="Plays" data-stat="play_count_tip" scope="col" class=" poptip center" data-tip="Number of plays in drive.<br />P - Pass, R - Rush, Y - Penalty" >Plays</th>
         <th aria-label="Length" data-stat="time_total" scope="col" class=" poptip center" >Length</th>
         <th aria-label="Net Yards (Just Plays)" data-stat="net_yds" scope="col" class=" poptip center" >Net Yds</th>
         <th aria-label="Result" data-stat="end_event" scope="col" class=" poptip center" >Result</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="right " data-stat="drive_num" >1</th><td class="center " data-stat="quarter" >1</td><td class="right " data-stat="time_start" csk="900" >15:00</td><td class="right " data-stat="start_at" >DET 25</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="5 Pass, 0 Rush, 0 Penalty">5</span></td><td class="right " data-stat="time_total" csk="122" >2:02</td><td class="right " data-stat="net_yds" >25</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >2</th><td class="center " data-stat="quarter" >1</td><td class="right " data-stat="time_start" csk="698" >11:38</td><td class="right " data-stat="start_at" >DEN 37</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="2 Pass, 1 Rush, 0 Penalty">3</span></td><td class="right " data-stat="time_total" csk="125" >2:05</td><td class="right " data-stat="net_yds" >-2</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >3</th><td class="center " data-stat="quarter" >1</td><td class="right " data-stat="time_start" csk="511" >8:31</td><td class="right " data-stat="start_at" >DET 27</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="4 Pass, 2 Rush, 1 Penalty">6</span></td><td class="right " data-stat="time_total" csk="207" >3:27</td><td class="right " data-stat="net_yds" >24</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >4</th><td class="center " data-stat="quarter" >1</td><td class="right " data-stat="time_start" csk="98" >1:38</td><td class="right " data-stat="start_at" >DET 20</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="5 Pass, 3 Rush, 0 Penalty">8</span></td><td class="right " data-stat="time_total" csk="247" >4:07</td><td class="right " data-stat="net_yds" >80</td><td class="center " data-stat="end_event" >Touchdown</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >5</th><td class="center " data-stat="quarter" >2</td><td class="right " data-stat="time_start" csk="658" >10:58</td><td class="right " data-stat="start_at" >DET 39</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="5 Pass, 1 Rush, 0 Penalty">6</span></td><td class="right " data-stat="time_total" csk="163" >2:43</td><td class="right " data-stat="net_yds" >61</td><td class="center " data-stat="end_event" >Touchdown</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >6</th><td class="center " data-stat="quarter" >2</td><td class="right " data-stat="time_start" csk="261" >4:21</td><td class="right " data-stat="start_at" >DET 19</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="6 Pass, 5 Rush, 0 Penalty">11</span></td><td class="right " data-stat="time_total" csk="242" >4:02</td><td class="right " data-stat="net_yds" >81</td><td class="center " data-stat="end_event" >Touchdown</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >7</th><td class="center " data-stat="quarter" >3</td><td class="right " data-stat="time_start" csk="634" >10:34</td><td class="right " data-stat="start_at" >DET 25</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="4 Pass, 4 Rush, 0 Penalty">8</span></td><td class="right " data-stat="time_total" csk="213" >3:33</td><td class="right " data-stat="net_yds" >75</td><td class="center " data-stat="end_event" >Touchdown</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >8</th><td class="center " data-stat="quarter" >3</td><td class="right " data-stat="time_start" csk="43" >0:43</td><td class="right " data-stat="start_at" >DET 25</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="1 Pass, 5 Rush, 1 Penalty">6</span></td><td class="right " data-stat="time_total" csk="211" >3:31</td><td class="right " data-stat="net_yds" >75</td><td class="center " data-stat="end_event" >Touchdown</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >9</th><td class="center " data-stat="quarter" >4</td><td class="right " data-stat="time_start" csk="659" >10:59</td><td class="right " data-stat="start_at" >DET 23</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="2 Pass, 1 Rush, 0 Penalty">3</span></td><td class="right " data-stat="time_total" csk="101" >1:41</td><td class="right " data-stat="net_yds" >-9</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >10</th><td class="center " data-stat="quarter" >4</td><td class="right " data-stat="time_start" csk="388" >6:28</td><td class="right " data-stat="start_at" >DEN 44</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="2 Pass, 6 Rush, 0 Penalty">8</span></td><td class="right " data-stat="time_total" csk="247" >4:07</td><td class="right " data-stat="net_yds" >44</td><td class="center " data-stat="end_event" >Touchdown</td></tr>

</table>


</div>
-->
                        </div>
                    </div>
                    <div>
                        <div id="all_vis_drives" class="table_wrapper setup_commented commented">
                            <div class="section_heading assoc_vis_drives" id="vis_drives_sh">
                                <span class="section_anchor" id="vis_drives_link" data-label="Broncos Drives"></span>
                                <h2>Broncos Drives</h2>
                                <div class="section_heading_text">
                                    <ul></ul>
                                </div>
                            </div>
                            <div class="placeholder"></div>
                            <!--

<div class="table_container" id="div_vis_drives">
    
    <table class="sortable stats_table" id="vis_drives" data-cols-to-freeze=",1">
    <caption>Broncos Drives Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="#" data-stat="drive_num" scope="col" class=" poptip center" >#</th>
         <th aria-label="Quarter" data-stat="quarter" scope="col" class=" poptip center" >Quarter</th>
         <th aria-label="Time" data-stat="time_start" scope="col" class=" poptip center" >Time</th>
         <th aria-label="LOS" data-stat="start_at" scope="col" class=" poptip center" >LOS</th>
         <th aria-label="Plays" data-stat="play_count_tip" scope="col" class=" poptip center" data-tip="Number of plays in drive.<br />P - Pass, R - Rush, Y - Penalty" >Plays</th>
         <th aria-label="Length" data-stat="time_total" scope="col" class=" poptip center" >Length</th>
         <th aria-label="Net Yards (Just Plays)" data-stat="net_yds" scope="col" class=" poptip center" >Net Yds</th>
         <th aria-label="Result" data-stat="end_event" scope="col" class=" poptip center" >Result</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="right " data-stat="drive_num" >1</th><td class="center " data-stat="quarter" >1</td><td class="right " data-stat="time_start" csk="778" >12:58</td><td class="right " data-stat="start_at" >DEN 29</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="3 Pass, 1 Rush, 0 Penalty">4</span></td><td class="right " data-stat="time_total" csk="80" >1:20</td><td class="right " data-stat="net_yds" >41</td><td class="center " data-stat="end_event" >Fumble</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >2</th><td class="center " data-stat="quarter" >1</td><td class="right " data-stat="time_start" csk="573" >9:33</td><td class="right " data-stat="start_at" >DEN 20</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="2 Pass, 1 Rush, 0 Penalty">3</span></td><td class="right " data-stat="time_total" csk="62" >1:02</td><td class="right " data-stat="net_yds" >1</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >3</th><td class="center " data-stat="quarter" >1</td><td class="right " data-stat="time_start" csk="304" >5:04</td><td class="right " data-stat="start_at" >DEN 16</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="2 Pass, 4 Rush, 1 Penalty">6</span></td><td class="right " data-stat="time_total" csk="206" >3:26</td><td class="right " data-stat="net_yds" >30</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >4</th><td class="center " data-stat="quarter" >2</td><td class="right " data-stat="time_start" csk="751" >12:31</td><td class="right " data-stat="start_at" >DEN 25</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="2 Pass, 1 Rush, 0 Penalty">3</span></td><td class="right " data-stat="time_total" csk="93" >1:33</td><td class="right " data-stat="net_yds" >-12</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >5</th><td class="center " data-stat="quarter" >2</td><td class="right " data-stat="time_start" csk="495" >8:15</td><td class="right " data-stat="start_at" >DEN 21</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="3 Pass, 4 Rush, 0 Penalty">7</span></td><td class="right " data-stat="time_total" csk="234" >3:54</td><td class="right " data-stat="net_yds" >11</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >6</th><td class="center " data-stat="quarter" >2</td><td class="right " data-stat="time_start" csk="19" >0:19</td><td class="right " data-stat="start_at" >DEN 25</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="0 Pass, 1 Rush, 0 Penalty">1</span></td><td class="right " data-stat="time_total" csk="19" >0:19</td><td class="right " data-stat="net_yds" >-1</td><td class="center " data-stat="end_event" >End of Half</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >7</th><td class="center " data-stat="quarter" >3</td><td class="right " data-stat="time_start" csk="900" >15:00</td><td class="right " data-stat="start_at" >DEN 25</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="6 Pass, 4 Rush, 1 Penalty">10</span></td><td class="right " data-stat="time_total" csk="266" >4:26</td><td class="right " data-stat="net_yds" >75</td><td class="center " data-stat="end_event" >Touchdown</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >8</th><td class="center " data-stat="quarter" >3</td><td class="right " data-stat="time_start" csk="421" >7:01</td><td class="right " data-stat="start_at" >DEN 25</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="7 Pass, 4 Rush, 1 Penalty">12</span></td><td class="right " data-stat="time_total" csk="378" >6:18</td><td class="right " data-stat="net_yds" >70</td><td class="center " data-stat="end_event" >Field Goal</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >9</th><td class="center " data-stat="quarter" >4</td><td class="right " data-stat="time_start" csk="732" >12:12</td><td class="right " data-stat="start_at" >DEN 25</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="4 Pass, 1 Rush, 0 Penalty">5</span></td><td class="right " data-stat="time_total" csk="73" >1:13</td><td class="right " data-stat="net_yds" >19</td><td class="center " data-stat="end_event" >Punt</td></tr>
<tr class="bold" ><th scope="row" class="right " data-stat="drive_num" >10</th><td class="center " data-stat="quarter" >4</td><td class="right " data-stat="time_start" csk="558" >9:18</td><td class="right " data-stat="start_at" >DEN 38</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="5 Pass, 3 Rush, 0 Penalty">8</span></td><td class="right " data-stat="time_total" csk="170" >2:50</td><td class="right " data-stat="net_yds" >62</td><td class="center " data-stat="end_event" >Touchdown</td></tr>
<tr ><th scope="row" class="right " data-stat="drive_num" >11</th><td class="center " data-stat="quarter" >4</td><td class="right " data-stat="time_start" csk="141" >2:21</td><td class="right " data-stat="start_at" >DEN 21</td><td class="right " data-stat="play_count_tip" ><span class="tooltip" tip="0 Pass, 4 Rush, 0 Penalty">4</span></td><td class="right " data-stat="time_total" csk="141" >2:21</td><td class="right " data-stat="net_yds" >26</td><td class="center " data-stat="end_event" >End of Game</td></tr>

</table>


</div>
-->
                        </div>
                    </div>
                </div>
                <!-- CTA_FLAG -->
                <div class="callout light new_stathead_player_highlight stathead_event">
                    <div class="callout_logos">
                        <a href="
  
https://stathead.com/sport/football/?&utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_03_bnnr_boxes_stathead&utm_content=img_logo" class="sh-cta-button" target="_blank" rel="noopener">
                            <img src="https://cdn.ssref.net/req/202004233/logos/stathead-pfr-white.svg" onerror="this.src='https://cdn.ssref.net/req/202004233/logos/pfr-logo-white.png'; this.onerror = null;" alt="Stathead Logo">
                        </a>
                        <div id="powered_by">POWERED BY</div>
                        <a href="
  
https://stathead.com/sport/football/?&utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_03_bnnr_boxes_stathead&utm_content=img_logo" class="sh-cta-button" target="_blank" rel="noopener">
                            <img src="https://cdn.ssref.net/req/202004233/logos/pfr-logo-white.svg" onerror="this.src='https://cdn.ssref.net/req/202004233/logos/pfr-logo-white.png'; this.onerror = null;" alt=".com Logo">
                        </a>
                    </div>
                    <div class="new_stathead_player_highlight_content">
                        <div>
                            <b>Looking for something amazing? Uncover the story that stats can tell with Stathead.</b>
                        </div>
                        <div class="cta">Search through thousands of plays from pro football history using our Event Finder tool.</div>
                        <div>
                            <a href="
  
https://stathead.com/sport/football/?&utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_03_bnnr_boxes_stathead&utm_content=bttn_cta" class="button " target="_blank" rel="noopener">Try it & get your first month FREE</a>
                        </div>
                    </div>
                </div>
                <div id="all_pbp" class="table_wrapper setup_commented commented">
                    <div class="section_heading assoc_pbp" id="pbp_sh">
                        <span class="section_anchor" id="pbp_link" data-label="Full Play-By-Play"></span>
                        <h2>Full Play-By-Play</h2>
                        <div class="section_heading_text">
                            <ul></ul>
                        </div>
                    </div>
                    <div class="placeholder"></div>
                    <!--

<div class="table_container" id="div_pbp">
    
    <table class="sortable stats_table" id="pbp" data-cols-to-freeze="1,2">
    <caption>Full Play-By-Play Table</caption>
    

   <colgroup><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="Quarter" data-stat="quarter" scope="col" class=" poptip center" >Quarter</th>
         <th aria-label="Time" data-stat="qtr_time_remain" scope="col" class=" poptip center" data-tip="Time remaining in this quarter" >Time</th>
         <th aria-label="Down" data-stat="down" scope="col" class=" poptip center" >Down</th>
         <th aria-label="ToGo" data-stat="yds_to_go" scope="col" class=" poptip center" >ToGo</th>
         <th aria-label="Location" data-stat="location" scope="col" class=" poptip left" data-tip="Play location" >Location</th>
         <th aria-label="DEN" data-stat="pbp_score_aw" scope="col" class=" poptip left" data-tip="Away Points" >DEN</th>
         <th aria-label="DET" data-stat="pbp_score_hm" scope="col" class=" poptip left" data-tip="Home Points" >DET</th>
         <th aria-label="Detail" data-stat="detail" scope="col" class=" poptip left" data-tip="Play description" >Detail</th>
         <th aria-label="EPB" data-stat="exp_pts_before" scope="col" class=" poptip left" data-tip="Expected points before this play, based on down, distance, and field position" >EPB</th>
         <th aria-label="EPA" data-stat="exp_pts_after" scope="col" class=" poptip left" data-tip="Expected points after this play (or actual scoring results of the play if it was a score)" >EPA</th>
      </tr>
      </thead>
<tbody><tr class="thead onecell" ><td class="right center" data-stat="onecell" colspan="10" >1st Quarter</td></tr>
<tr ><th scope="row" class="center iz" data-stat="quarter" ></th><td class="center iz" data-stat="qtr_time_remain" ></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left iz" data-stat="location" ></td><td class="right iz" data-stat="pbp_score_aw" ></td><td class="right iz" data-stat="pbp_score_hm" ></td><td class="left " data-stat="detail" >Lions won the coin toss, Lions to receive the opening kickoff.</td><td class="right iz" data-stat="exp_pts_before" ></td><td class="right iz" data-stat="exp_pts_after" ></td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_1.000">15:00</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="65" >DEN 35</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_1.000"></a><a href="/players/L/LutzWi00.htm">Wil Lutz</a> kicks off 66 yards, returned by <a href="/players/R/ReynCr00.htm">Craig Reynolds</a> for 26 yards (tackle by <a href="/players/B/BurtMi00.htm">Michael Burton</a>)</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.610</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_2.000">14:56</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="25" >DET 25</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_2.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete short right</td><td class="right " data-stat="exp_pts_before" >0.610</td><td class="right " data-stat="exp_pts_after" >0.060</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_3.000">14:46</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="25" >DET 25</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_3.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a> for 21 yards (tackle by <a href="/players/S/SingAl00.htm">Alex Singleton</a>)</td><td class="right " data-stat="exp_pts_before" >0.060</td><td class="right " data-stat="exp_pts_after" >1.990</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_4.000">14:01</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="46" >DET 46</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_4.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete deep left intended for <a href="/players/W/WillJa11.htm">Jameson Williams</a> (defended by <a href="/players/S/SimmJu00.htm">Justin Simmons</a>)</td><td class="right " data-stat="exp_pts_before" >1.990</td><td class="right " data-stat="exp_pts_after" >1.450</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_5.000">13:52</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="46" >DET 46</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_5.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/M/MontDa01.htm">David Montgomery</a> for 4 yards (tackle by <a href="/players/C/CoopJo02.htm">Jonathon Cooper</a>)</td><td class="right " data-stat="exp_pts_before" >1.450</td><td class="right " data-stat="exp_pts_after" >1.290</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_6.000">13:10</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >6</td><td class="left " data-stat="location" csk="50" >DET 50</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_6.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete short right intended for <a href="/players/M/MontDa01.htm">David Montgomery</a></td><td class="right " data-stat="exp_pts_before" >1.290</td><td class="right " data-stat="exp_pts_after" >-0.060</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_7.000">13:06</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >6</td><td class="left " data-stat="location" csk="50" >DET 50</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_7.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> punts 21 yards out of bounds</td><td class="right " data-stat="exp_pts_before" >-0.060</td><td class="right " data-stat="exp_pts_after" >-0.870</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_9.000">12:58</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="71" >DEN 29</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_9.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short middle to <a href="/players/J/JeudJe00.htm">Jerry Jeudy</a> for 40 yards (tackle by <a href="/players/B/BranBr00.htm">Brian Branch</a>)</td><td class="right " data-stat="exp_pts_before" >0.870</td><td class="right " data-stat="exp_pts_after" >3.510</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_10.000">12:27</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="31" >DET 31</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_10.000"></a><a href="/players/M/MimsMa00.htm">Marvin Mims</a> right end for 11 yards (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >3.510</td><td class="right " data-stat="exp_pts_after" >4.240</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_11.000">11:53</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="20" >DET 20</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_11.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short left intended for <a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a> (defended by <a href="/players/D/DorsKh00.htm">Khalil Dorsey</a>)</td><td class="right " data-stat="exp_pts_before" >4.240</td><td class="right " data-stat="exp_pts_after" >3.690</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_12.000">11:52</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="20" >DET 20</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_12.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> sacked by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a> for -10 yards. <a href="/players/W/WilsRu00.htm">Russell Wilson</a> fumbles (forced by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>), recovered by <a href="/players/B/BuggIs00.htm">Isaiah Buggs</a> at DET-30 and returned for 33 yards (tackle by <a href="/players/M/MeinQu02.htm">Quinn Meinerz</a>)</td><td class="right " data-stat="exp_pts_before" >3.690</td><td class="right " data-stat="exp_pts_after" >-3.120</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_13.000">11:38</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="63" >DEN 37</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_13.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/W/WillJa11.htm">Jameson Williams</a> for 1 yard (tackle by <a href="/players/J/JeweJo00.htm">Josey Jewell</a>)</td><td class="right " data-stat="exp_pts_before" >3.120</td><td class="right " data-stat="exp_pts_after" >2.710</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_14.000">11:03</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="64" >DEN 36</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_14.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> left tackle for 4 yards (tackle by <a href="/players/H/HarrJo05.htm">Jonathan Harris</a>)</td><td class="right " data-stat="exp_pts_before" >2.710</td><td class="right " data-stat="exp_pts_after" >2.540</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_15.000">10:30</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >5</td><td class="left " data-stat="location" csk="68" >DEN 32</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_15.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> sacked by <a href="/players/J/JoneD.01.htm">D.J. Jones</a> for -7 yards</td><td class="right " data-stat="exp_pts_before" >2.540</td><td class="right " data-stat="exp_pts_after" >0.660</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_16.000">9:43</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >12</td><td class="left " data-stat="location" csk="61" >DEN 39</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_16.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> punts 39 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >0.660</td><td class="right " data-stat="exp_pts_after" >-0.280</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_18.000">9:33</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="80" >DEN 20</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_18.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> up the middle for 1 yard (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >0.280</td><td class="right " data-stat="exp_pts_after" >-0.130</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_19.000">8:55</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="79" >DEN 21</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_19.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete deep right intended for <a href="/players/M/MimsMa00.htm">Marvin Mims</a> (defended by <a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a>)</td><td class="right " data-stat="exp_pts_before" >-0.130</td><td class="right " data-stat="exp_pts_after" >-0.820</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_20.000">8:50</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="79" >DEN 21</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_20.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short left intended for <a href="/players/J/JeudJe00.htm">Jerry Jeudy</a></td><td class="right " data-stat="exp_pts_before" >-0.820</td><td class="right " data-stat="exp_pts_after" >-1.960</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_21.000">8:40</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="79" >DEN 21</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_21.000"></a><a href="/players/D/DixoRi00.htm">Riley Dixon</a> punts 52 yards, returned by <a href="/players/R/RaymKa00.htm">Kalif Raymond</a> for no gain (tackle by <a href="/players/M/MossRi00.htm">Riley Moss</a>)</td><td class="right " data-stat="exp_pts_before" >-1.960</td><td class="right " data-stat="exp_pts_after" >-0.740</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_23.000">8:31</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="27" >DET 27</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_23.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> up the middle for 8 yards (tackle by <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >0.740</td><td class="right " data-stat="exp_pts_after" >1.280</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_24.000">7:51</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >2</td><td class="left " data-stat="location" csk="35" >DET 35</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_24.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> right end for 10 yards (tackle by <a href="/players/M/McMiJa00.htm">Ja'Quan McMillian</a>). Penalty on <a href="/players/G/GlasGr00.htm">Graham Glasgow</a>: Offensive Holding, 10 yards (accepted) (no play)</td><td class="right " data-stat="exp_pts_before" >1.280</td><td class="right " data-stat="exp_pts_after" >-0.070</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_25.000">7:42</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >12</td><td class="left " data-stat="location" csk="25" >DET 25</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_25.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short middle to <a href="/players/W/WillJa11.htm">Jameson Williams</a> for 14 yards (tackle by <a href="/players/S/SimmJu00.htm">Justin Simmons</a>)</td><td class="right " data-stat="exp_pts_before" >-0.070</td><td class="right " data-stat="exp_pts_after" >1.530</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_26.000">7:02</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="39" >DET 39</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_26.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/R/RaymKa00.htm">Kalif Raymond</a> for 12 yards</td><td class="right " data-stat="exp_pts_before" >1.530</td><td class="right " data-stat="exp_pts_after" >2.320</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_27.000">6:36</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="51" >DEN 49</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_27.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> up the middle for 1 yard (tackle by <a href="/players/C/CoopJo02.htm">Jonathon Cooper</a> and <a href="/players/I/IncoTh00.htm">Thomas Incoom</a>)</td><td class="right " data-stat="exp_pts_before" >2.320</td><td class="right " data-stat="exp_pts_after" >1.920</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_28.000">6:00</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="52" >DEN 48</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_28.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> for -1 yards (tackle by <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >1.920</td><td class="right " data-stat="exp_pts_after" >1.090</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_29.000">5:16</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="51" >DEN 49</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_29.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete deep left intended for <a href="/players/W/WillJa11.htm">Jameson Williams</a></td><td class="right " data-stat="exp_pts_before" >1.090</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_30.000">5:11</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="51" >DEN 49</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_30.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> punts 33 yards, fair catch by <a href="/players/M/MimsMa00.htm">Marvin Mims</a> at DEN-16</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.140</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_32.000">5:04</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="84" >DEN 16</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_32.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> up the middle for 2 yards (tackle by <a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a>)</td><td class="right " data-stat="exp_pts_before" >-0.140</td><td class="right " data-stat="exp_pts_after" >-0.350</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_33.000">4:23</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >8</td><td class="left " data-stat="location" csk="82" >DEN 18</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_33.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> up the middle for 4 yards (tackle by <a href="/players/C/ComiJo00.htm">John Cominsky</a> and <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>)</td><td class="right " data-stat="exp_pts_before" >-0.350</td><td class="right " data-stat="exp_pts_after" >-0.620</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_34.000">3:40</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >5</td><td class="left " data-stat="location" csk="78" >DEN 22</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_34.000"></a>Penalty on <a href="/players/M/McGlMi00.htm">Mike McGlinchey</a>: False Start, 5 yards (accepted) (no play)</td><td class="right " data-stat="exp_pts_before" >-0.620</td><td class="right " data-stat="exp_pts_after" >-1.250</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_35.000">3:22</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="83" >DEN 17</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_35.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete deep left to <a href="/players/S/SuttCo00.htm">Courtland Sutton</a> for 23 yards (tackle by <a href="/players/D/DorsKh00.htm">Khalil Dorsey</a> and <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>)</td><td class="right " data-stat="exp_pts_before" >-1.250</td><td class="right " data-stat="exp_pts_after" >1.600</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_36.000">2:53</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="60" >DEN 40</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_36.000"></a><a href="/players/P/PeriSa00.htm">Samaje Perine</a> left tackle for 6 yards (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a> and <a href="/players/C/CampJa04.htm">Jack Campbell</a>)</td><td class="right " data-stat="exp_pts_before" >1.600</td><td class="right " data-stat="exp_pts_after" >1.860</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_37.000">2:17</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >4</td><td class="left " data-stat="location" csk="54" >DEN 46</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_37.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> left tackle for no gain (tackle by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a> and <a href="/players/B/BranBr00.htm">Brian Branch</a>)</td><td class="right " data-stat="exp_pts_before" >1.860</td><td class="right " data-stat="exp_pts_after" >1.160</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_38.000">1:52</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >4</td><td class="left " data-stat="location" csk="54" >DEN 46</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_38.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short right intended for <a href="/players/T/TrauAd00.htm">Adam Trautman</a> (defended by <a href="/players/B/BranBr00.htm">Brian Branch</a>)</td><td class="right " data-stat="exp_pts_before" >1.160</td><td class="right " data-stat="exp_pts_after" >-0.320</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_39.000">1:47</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >4</td><td class="left " data-stat="location" csk="54" >DEN 46</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_39.000"></a><a href="/players/D/DixoRi00.htm">Riley Dixon</a> punts 54 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >-0.320</td><td class="right " data-stat="exp_pts_after" >-0.280</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_41.000">1:38</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="20" >DET 20</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_41.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> left tackle for 6 yards (tackle by <a href="/players/S/SingAl00.htm">Alex Singleton</a> and <a href="/players/L/LockPJ00.htm">P.J. Locke</a>)</td><td class="right " data-stat="exp_pts_before" >0.280</td><td class="right " data-stat="exp_pts_after" >0.540</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_42.000">1:05</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >4</td><td class="left " data-stat="location" csk="26" >DET 26</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_42.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> left end for 5 yards (tackle by <a href="/players/H/HennMa01.htm">Matt Henningsen</a>)</td><td class="right " data-stat="exp_pts_before" >0.540</td><td class="right " data-stat="exp_pts_after" >1.000</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >1</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_43.000">0:29</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="31" >DET 31</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_43.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short middle to <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a> for 17 yards (tackle by <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >1.000</td><td class="right " data-stat="exp_pts_after" >2.130</td></tr>

      
      <tr class="thead">
         <th aria-label="Quarter" data-stat="quarter" class=" center" >Quarter</th>
         <th aria-label="Time" data-stat="qtr_time_remain" class=" center" data-tip="Time remaining in this quarter" >Time</th>
         <th aria-label="Down" data-stat="down" class=" center" >Down</th>
         <th aria-label="ToGo" data-stat="yds_to_go" class=" center" >ToGo</th>
         <th aria-label="Location" data-stat="location" class=" left" data-tip="Play location" >Location</th>
         <th aria-label="DEN" data-stat="pbp_score_aw" class=" left" data-tip="Away Points" >DEN</th>
         <th aria-label="DET" data-stat="pbp_score_hm" class=" left" data-tip="Home Points" >DET</th>
         <th aria-label="Detail" data-stat="detail" class=" left" data-tip="Play description" >Detail</th>
         <th aria-label="EPB" data-stat="exp_pts_before" class=" left" data-tip="Expected points before this play, based on down, distance, and field position" >EPB</th>
         <th aria-label="EPA" data-stat="exp_pts_after" class=" left" data-tip="Expected points after this play (or actual scoring results of the play if it was a score)" >EPA</th>
      </tr>
      <tr class="thead onecell" ><td class="right center" data-stat="onecell" colspan="10" >2nd Quarter</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_45.000">15:00</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="48" >DET 48</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_45.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> up the middle for no gain (tackle by <a href="/players/M/McMiJa00.htm">Ja'Quan McMillian</a>)</td><td class="right " data-stat="exp_pts_before" >2.130</td><td class="right " data-stat="exp_pts_after" >1.580</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_46.000">14:28</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="48" >DET 48</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_46.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short right to <a href="/players/P/PeopDo00.htm">Donovan Peoples-Jones</a> for 5 yards (tackle by <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >1.580</td><td class="right " data-stat="exp_pts_after" >1.550</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_47.000">13:52</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >5</td><td class="left " data-stat="location" csk="53" >DEN 47</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_47.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a> for 7 yards (tackle by <a href="/players/J/JeweJo00.htm">Josey Jewell</a>)</td><td class="right " data-stat="exp_pts_before" >1.550</td><td class="right " data-stat="exp_pts_after" >2.920</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_48.000">13:18</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="60" >DEN 40</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right iz" data-stat="pbp_score_hm" >0</td><td class="left " data-stat="detail" ><a name="pbp_48.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete deep right to <a href="/players/R/ReynJo00.htm">Josh Reynolds</a> for 21 yards (tackle by <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >2.920</td><td class="right " data-stat="exp_pts_after" >4.310</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_49.000">12:41</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="81" >DEN 19</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >6</td><td class="left " data-stat="detail" ><a name="pbp_49.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a> for 19 yards, touchdown</td><td class="right " data-stat="exp_pts_before" >4.310</td><td class="right " data-stat="exp_pts_after" >7.000</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_50.000">12:31</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="85" >DEN 15</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_50.000"></a><a href="/players/B/BadgMi00.htm">Michael Badgley</a> kicks extra point good</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_52.000">12:31</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="35" >DET 35</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_52.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> kicks off 65 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.610</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_53.000">12:31</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="75" >DEN 25</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_53.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short middle intended for <a href="/players/J/JeudJe00.htm">Jerry Jeudy</a></td><td class="right " data-stat="exp_pts_before" >0.610</td><td class="right " data-stat="exp_pts_after" >0.060</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_54.000">12:26</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="75" >DEN 25</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_54.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> up the middle for -3 yards (tackle by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a> and <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >0.060</td><td class="right " data-stat="exp_pts_after" >-1.020</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_55.000">11:42</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >13</td><td class="left " data-stat="location" csk="78" >DEN 22</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_55.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> sacked by <a href="/players/P/PascJo00.htm">Josh Paschal</a> for -9 yards</td><td class="right " data-stat="exp_pts_before" >-1.020</td><td class="right " data-stat="exp_pts_after" >-2.490</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_56.000">11:10</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >22</td><td class="left " data-stat="location" csk="87" >DEN 13</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_56.000"></a><a href="/players/D/DixoRi00.htm">Riley Dixon</a> punts 56 yards, returned by <a href="/players/R/RaymKa00.htm">Kalif Raymond</a> for 8 yards (tackle by <a href="/players/S/SmitTr04.htm">Tremon Smith</a>)</td><td class="right " data-stat="exp_pts_before" >-2.490</td><td class="right " data-stat="exp_pts_after" >-1.530</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_58.000">10:58</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="39" >DET 39</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_58.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete deep right to <a href="/players/R/ReynJo00.htm">Josh Reynolds</a> for 20 yards (tackle by <a href="/players/S/SurtPa01.htm">Patrick Surtain</a>)</td><td class="right " data-stat="exp_pts_before" >1.530</td><td class="right " data-stat="exp_pts_after" >2.850</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_59.000">10:19</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="59" >DEN 41</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_59.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> left end for 21 yards (tackle by <a href="/players/J/JeweJo00.htm">Josey Jewell</a>)</td><td class="right " data-stat="exp_pts_before" >2.850</td><td class="right " data-stat="exp_pts_after" >4.240</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_60.000">9:38</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="80" >DEN 20</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_60.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short right to <a href="/players/M/MontDa01.htm">David Montgomery</a> for -7 yards (tackle by <a href="/players/J/JoneD.01.htm">D.J. Jones</a>)</td><td class="right " data-stat="exp_pts_before" >4.240</td><td class="right " data-stat="exp_pts_after" >2.750</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_61.000">9:02</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >17</td><td class="left " data-stat="location" csk="73" >DEN 27</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_61.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/W/WillJa11.htm">Jameson Williams</a> for 18 yards (tackle by <a href="/players/L/LockPJ00.htm">P.J. Locke</a>)</td><td class="right " data-stat="exp_pts_before" >2.750</td><td class="right " data-stat="exp_pts_after" >5.140</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_62.000">8:25</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="91" >DEN 9</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >7</td><td class="left " data-stat="detail" ><a name="pbp_62.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete short middle intended for <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a> (defended by <a href="/players/L/LockPJ00.htm">P.J. Locke</a>)</td><td class="right " data-stat="exp_pts_before" >5.140</td><td class="right " data-stat="exp_pts_after" >4.380</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_63.000">8:20</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="91" >DEN 9</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >13</td><td class="left " data-stat="detail" ><a name="pbp_63.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short middle to <a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> for 9 yards, touchdown</td><td class="right " data-stat="exp_pts_before" >4.380</td><td class="right " data-stat="exp_pts_after" >7.000</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_64.000">8:15</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="85" >DEN 15</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_64.000"></a><a href="/players/B/BadgMi00.htm">Michael Badgley</a> kicks extra point good</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_66.000">8:15</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="35" >DET 35</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_66.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> kicks off 64 yards, returned by <a href="/players/M/MimsMa00.htm">Marvin Mims</a> for 20 yards (tackle by <a href="/players/R/ReevJa00.htm">Jalen Reeves-Maybin</a>)</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.340</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_67.000">8:10</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="79" >DEN 21</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_67.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short right to <a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a> for 8 yards (tackle by <a href="/players/S/SuttCa00.htm">Cameron Sutton</a> and <a href="/players/C/CampJa04.htm">Jack Campbell</a>)</td><td class="right " data-stat="exp_pts_before" >0.340</td><td class="right " data-stat="exp_pts_after" >0.880</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_69.000">7:44</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >2</td><td class="left " data-stat="location" csk="71" >DEN 29</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_69.000"></a><a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a> left tackle for 1 yard (tackle by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>)</td><td class="right " data-stat="exp_pts_before" >0.880</td><td class="right " data-stat="exp_pts_after" >0.300</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_70.000">7:10</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >1</td><td class="left " data-stat="location" csk="70" >DEN 30</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_70.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> up the middle for no gain (tackle by <a href="/players/C/CampJa04.htm">Jack Campbell</a>)</td><td class="right " data-stat="exp_pts_before" >0.300</td><td class="right " data-stat="exp_pts_after" >-1.370</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_71.000">6:28</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >1</td><td class="left " data-stat="location" csk="70" >DEN 30</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_71.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> up the middle for 2 yards (tackle by <a href="/players/C/ComiJo00.htm">John Cominsky</a>)</td><td class="right " data-stat="exp_pts_before" >-1.370</td><td class="right " data-stat="exp_pts_after" >1.070</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_72.000">5:57</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="68" >DEN 32</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_72.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> up the middle for 2 yards (tackle by <a href="/players/C/ComiJo00.htm">John Cominsky</a> and <a href="/players/J/JoseKe03.htm">Kerby Joseph</a>)</td><td class="right " data-stat="exp_pts_before" >1.070</td><td class="right " data-stat="exp_pts_after" >0.800</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_73.000">5:20</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >8</td><td class="left " data-stat="location" csk="66" >DEN 34</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_73.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short left to <a href="/players/W/WillJa10.htm">Javonte Williams</a> for -2 yards (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >0.800</td><td class="right " data-stat="exp_pts_after" >-0.160</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_74.000">4:35</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="68" >DEN 32</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_74.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete deep left intended for <a href="/players/J/JeudJe00.htm">Jerry Jeudy</a></td><td class="right " data-stat="exp_pts_before" >-0.160</td><td class="right " data-stat="exp_pts_after" >-1.240</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_75.000">4:28</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="68" >DEN 32</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_75.000"></a><a href="/players/D/DixoRi00.htm">Riley Dixon</a> punts 49 yards, fair catch by <a href="/players/R/RaymKa00.htm">Kalif Raymond</a> at DET-19</td><td class="right " data-stat="exp_pts_before" >-1.240</td><td class="right " data-stat="exp_pts_after" >-0.150</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_76.000">4:21</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="19" >DET 19</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_76.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> up the middle for 2 yards (tackle by <a href="/players/B/BrowBa01.htm">Baron Browning</a> and <a href="/players/J/JeweJo00.htm">Josey Jewell</a>)</td><td class="right " data-stat="exp_pts_before" >0.150</td><td class="right " data-stat="exp_pts_after" >-0.060</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_77.000">3:42</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >8</td><td class="left " data-stat="location" csk="21" >DET 21</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_77.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short middle to <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a> for 8 yards (tackle by <a href="/players/J/JeweJo00.htm">Josey Jewell</a> and <a href="/players/S/SimmJu00.htm">Justin Simmons</a>)</td><td class="right " data-stat="exp_pts_before" >-0.060</td><td class="right " data-stat="exp_pts_after" >0.870</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_78.000">3:05</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="29" >DET 29</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_78.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete short left intended for <a href="/players/R/ReynJo00.htm">Josh Reynolds</a> (defended by <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >0.870</td><td class="right " data-stat="exp_pts_after" >0.330</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_79.000">3:01</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="29" >DET 29</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_79.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short middle to <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a> for 29 yards (tackle by <a href="/players/S/SimmJu00.htm">Justin Simmons</a>)</td><td class="right " data-stat="exp_pts_before" >0.330</td><td class="right " data-stat="exp_pts_after" >2.790</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_80.000">2:34</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="58" >DEN 42</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_80.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> up the middle for 8 yards (tackle by <a href="/players/B/BrowBa01.htm">Baron Browning</a>)</td><td class="right " data-stat="exp_pts_before" >2.790</td><td class="right " data-stat="exp_pts_after" >3.320</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_81.000">2:17</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left iz" data-stat="location" csk="0" ></td><td class="right iz" data-stat="pbp_score_aw" ></td><td class="right iz" data-stat="pbp_score_hm" ></td><td class="left " data-stat="detail" ><a name="pbp_81.000"></a>Timeout #1 by Denver Broncos</td><td class="right iz" data-stat="exp_pts_before" ></td><td class="right iz" data-stat="exp_pts_after" ></td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_82.000">2:17</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >2</td><td class="left " data-stat="location" csk="66" >DEN 34</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_82.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> up the middle for 1 yard (tackle by <a href="/players/H/HarrJo05.htm">Jonathan Harris</a> and <a href="/players/P/PurcMi00.htm">Mike Purcell</a>)</td><td class="right " data-stat="exp_pts_before" >3.320</td><td class="right " data-stat="exp_pts_after" >2.740</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_84.000">2:00</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >1</td><td class="left " data-stat="location" csk="67" >DEN 33</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_84.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> up the middle for 4 yards (tackle by <a href="/players/S/SimmJu00.htm">Justin Simmons</a>)</td><td class="right " data-stat="exp_pts_before" >2.740</td><td class="right " data-stat="exp_pts_after" >3.640</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_85.000">1:30</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="71" >DEN 29</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_85.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> right tackle for 11 yards (tackle by <a href="/players/S/SurtPa01.htm">Patrick Surtain</a>)</td><td class="right " data-stat="exp_pts_before" >3.640</td><td class="right " data-stat="exp_pts_after" >4.370</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_86.000">0:55</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="82" >DEN 18</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_86.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a> for 3 yards (tackle by <a href="/players/M/McMiJa00.htm">Ja'Quan McMillian</a>)</td><td class="right " data-stat="exp_pts_before" >4.370</td><td class="right " data-stat="exp_pts_after" >4.250</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_87.000">0:28</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left iz" data-stat="location" csk="0" ></td><td class="right iz" data-stat="pbp_score_aw" ></td><td class="right iz" data-stat="pbp_score_hm" ></td><td class="left " data-stat="detail" ><a name="pbp_87.000"></a>Timeout #1 by Detroit Lions</td><td class="right iz" data-stat="exp_pts_before" ></td><td class="right iz" data-stat="exp_pts_after" ></td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_88.000">0:28</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >7</td><td class="left " data-stat="location" csk="85" >DEN 15</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >14</td><td class="left " data-stat="detail" ><a name="pbp_88.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete short left intended for <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a></td><td class="right " data-stat="exp_pts_before" >4.250</td><td class="right " data-stat="exp_pts_after" >3.460</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_89.000">0:24</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >7</td><td class="left " data-stat="location" csk="85" >DEN 15</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >20</td><td class="left " data-stat="detail" ><a name="pbp_89.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short right to <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a> for 15 yards, touchdown</td><td class="right " data-stat="exp_pts_before" >3.460</td><td class="right " data-stat="exp_pts_after" >7.000</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_90.000">0:19</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="85" >DEN 15</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_90.000"></a><a href="/players/B/BadgMi00.htm">Michael Badgley</a> kicks extra point good</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_92.000">0:19</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="35" >DET 35</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_92.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> kicks off 65 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.610</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >2</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_93.000">0:19</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="75" >DEN 25</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_93.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> kneels for -1 yards</td><td class="right " data-stat="exp_pts_before" >0.610</td><td class="right " data-stat="exp_pts_after" >-0.070</td></tr>

      
      <tr class="thead">
         <th aria-label="Quarter" data-stat="quarter" class=" center" >Quarter</th>
         <th aria-label="Time" data-stat="qtr_time_remain" class=" center" data-tip="Time remaining in this quarter" >Time</th>
         <th aria-label="Down" data-stat="down" class=" center" >Down</th>
         <th aria-label="ToGo" data-stat="yds_to_go" class=" center" >ToGo</th>
         <th aria-label="Location" data-stat="location" class=" left" data-tip="Play location" >Location</th>
         <th aria-label="DEN" data-stat="pbp_score_aw" class=" left" data-tip="Away Points" >DEN</th>
         <th aria-label="DET" data-stat="pbp_score_hm" class=" left" data-tip="Home Points" >DET</th>
         <th aria-label="Detail" data-stat="detail" class=" left" data-tip="Play description" >Detail</th>
         <th aria-label="EPB" data-stat="exp_pts_before" class=" left" data-tip="Expected points before this play, based on down, distance, and field position" >EPB</th>
         <th aria-label="EPA" data-stat="exp_pts_after" class=" left" data-tip="Expected points after this play (or actual scoring results of the play if it was a score)" >EPA</th>
      </tr>
      <tr class="thead onecell" ><td class="right center" data-stat="onecell" colspan="10" >3rd Quarter</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_95.000">15:00</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="35" >DET 35</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_95.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> kicks off 65 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.610</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_96.000">15:00</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="75" >DEN 25</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_96.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> up the middle for 3 yards (tackle by <a href="/players/C/CampJa04.htm">Jack Campbell</a> and <a href="/players/C/ComiJo00.htm">John Cominsky</a>)</td><td class="right " data-stat="exp_pts_before" >0.610</td><td class="right " data-stat="exp_pts_after" >0.470</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_97.000">14:25</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >7</td><td class="left " data-stat="location" csk="72" >DEN 28</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_97.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short left to <a href="/players/W/WillJa10.htm">Javonte Williams</a> for -5 yards (tackle by <a href="/players/P/PascJo00.htm">Josh Paschal</a>)</td><td class="right " data-stat="exp_pts_before" >0.470</td><td class="right " data-stat="exp_pts_after" >-0.890</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_98.000">13:39</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >12</td><td class="left " data-stat="location" csk="77" >DEN 23</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_98.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete deep middle intended for <a href="/players/M/MimsMa00.htm">Marvin Mims</a>. Penalty on <a href="/players/D/DorsKh00.htm">Khalil Dorsey</a>: Illegal Contact, 5 yards (declined) . Penalty on <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>: Defensive Pass Interference, 44 yards (accepted) (no play)</td><td class="right " data-stat="exp_pts_before" >-0.890</td><td class="right " data-stat="exp_pts_after" >3.380</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_99.000">13:32</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="33" >DET 33</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_99.000"></a><a href="/players/P/PeriSa00.htm">Samaje Perine</a> up the middle for 2 yards (tackle by <a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a>)</td><td class="right " data-stat="exp_pts_before" >3.380</td><td class="right " data-stat="exp_pts_after" >3.110</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_100.000">12:53</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >8</td><td class="left " data-stat="location" csk="31" >DET 31</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_100.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short middle to <a href="/players/S/SuttCo00.htm">Courtland Sutton</a> for 14 yards (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >3.110</td><td class="right " data-stat="exp_pts_after" >4.440</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_101.000">12:20</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="17" >DET 17</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_101.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> right tackle for 6 yards (tackle by <a href="/players/C/CampJa04.htm">Jack Campbell</a> and <a href="/players/J/JoneBe03.htm">Benito Jones</a>)</td><td class="right " data-stat="exp_pts_before" >4.440</td><td class="right " data-stat="exp_pts_after" >4.890</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_102.000">11:42</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >4</td><td class="left " data-stat="location" csk="11" >DET 11</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_102.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short right intended for <a href="/players/T/TrauAd00.htm">Adam Trautman</a></td><td class="right " data-stat="exp_pts_before" >4.890</td><td class="right " data-stat="exp_pts_after" >4.100</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_103.000">11:40</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >4</td><td class="left " data-stat="location" csk="11" >DET 11</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_103.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short right to <a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a> for 5 yards (tackle by <a href="/players/D/DorsKh00.htm">Khalil Dorsey</a>)</td><td class="right " data-stat="exp_pts_before" >4.100</td><td class="right " data-stat="exp_pts_after" >5.830</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_104.000">11:20</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >6</td><td class="left " data-stat="location" csk="6" >DET 6</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_104.000"></a><a href="/players/P/PeriSa00.htm">Samaje Perine</a> right tackle for 3 yards (tackle by <a href="/players/M/MartBr00.htm">Brodric Martin</a> and <a href="/players/P/PascJo00.htm">Josh Paschal</a>)</td><td class="right " data-stat="exp_pts_before" >5.830</td><td class="right " data-stat="exp_pts_after" >5.530</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_105.000">10:46</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >3</td><td class="left " data-stat="location" csk="3" >DET 3</td><td class="right iz" data-stat="pbp_score_aw" >0</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_105.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short right intended for <a href="/players/J/JohnBr23.htm">Brandon Johnson</a> (defended by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>)</td><td class="right " data-stat="exp_pts_before" >5.530</td><td class="right " data-stat="exp_pts_after" >4.720</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_106.000">10:41</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >3</td><td class="left " data-stat="location" csk="3" >DET 3</td><td class="right " data-stat="pbp_score_aw" >6</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_106.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short left to <a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a> for 3 yards, touchdown <i>Replay Assistant challenged the pass completion ruling, and the original play was overturned.</i></td><td class="right " data-stat="exp_pts_before" >4.720</td><td class="right " data-stat="exp_pts_after" >7.000</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_107.000">10:34</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="15" >DET 15</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_107.000"></a><a href="/players/L/LutzWi00.htm">Wil Lutz</a> kicks extra point good</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_108.000">10:34</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="65" >DEN 35</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_108.000"></a><a href="/players/L/LutzWi00.htm">Wil Lutz</a> kicks off 65 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.610</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_109.000">10:34</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="25" >DET 25</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_109.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short middle to <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a> for 26 yards (tackle by <a href="/players/L/LockPJ00.htm">P.J. Locke</a> and <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >0.610</td><td class="right " data-stat="exp_pts_after" >2.320</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_110.000">9:55</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="51" >DEN 49</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_110.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete deep left intended for <a href="/players/W/WillJa11.htm">Jameson Williams</a></td><td class="right " data-stat="exp_pts_before" >2.320</td><td class="right " data-stat="exp_pts_after" >1.780</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_111.000">9:51</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="51" >DEN 49</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_111.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> right tackle for 1 yard (tackle by <a href="/players/J/JoneD.01.htm">D.J. Jones</a>)</td><td class="right " data-stat="exp_pts_before" >1.780</td><td class="right " data-stat="exp_pts_after" >1.220</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_112.000">9:13</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="52" >DEN 48</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_112.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> right end for 10 yards (tackle by <a href="/players/L/LockPJ00.htm">P.J. Locke</a>)</td><td class="right " data-stat="exp_pts_before" >1.220</td><td class="right " data-stat="exp_pts_after" >3.050</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_113.000">8:39</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="62" >DEN 38</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_113.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> up the middle for 34 yards (tackle by <a href="/players/H/HarrJo05.htm">Jonathan Harris</a>)</td><td class="right " data-stat="exp_pts_before" >3.050</td><td class="right " data-stat="exp_pts_after" >6.280</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_114.000">7:50</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >4</td><td class="left " data-stat="location" csk="96" >DEN 4</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_114.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> right tackle for 1 yard (tackle by <a href="/players/C/CoopJo02.htm">Jonathon Cooper</a> and <a href="/players/H/HennMa01.htm">Matt Henningsen</a>)</td><td class="right " data-stat="exp_pts_before" >6.280</td><td class="right " data-stat="exp_pts_after" >5.530</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_115.000">7:07</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >3</td><td class="left " data-stat="location" csk="97" >DEN 3</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >21</td><td class="left " data-stat="detail" ><a name="pbp_115.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete short left</td><td class="right " data-stat="exp_pts_before" >5.530</td><td class="right " data-stat="exp_pts_after" >4.720</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_116.000">7:03</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >3</td><td class="left " data-stat="location" csk="97" >DEN 3</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >27</td><td class="left " data-stat="detail" ><a name="pbp_116.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short right to <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a> for 3 yards, touchdown</td><td class="right " data-stat="exp_pts_before" >4.720</td><td class="right " data-stat="exp_pts_after" >7.000</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_117.000">7:01</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="85" >DEN 15</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_117.000"></a><a href="/players/B/BadgMi00.htm">Michael Badgley</a> kicks extra point good</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_119.000">7:01</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="35" >DET 35</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_119.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> kicks off 65 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.610</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_120.000">7:01</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="75" >DEN 25</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_120.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short left to <a href="/players/S/SuttCo00.htm">Courtland Sutton</a> for 8 yards (tackle by <a href="/players/S/SuttCa00.htm">Cameron Sutton</a>)</td><td class="right " data-stat="exp_pts_before" >0.610</td><td class="right " data-stat="exp_pts_after" >1.140</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_121.000">6:15</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >2</td><td class="left " data-stat="location" csk="67" >DEN 33</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_121.000"></a><a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a> left end for 1 yard (tackle by <a href="/players/O/OnwuLe00.htm">Levi Onwuzurike</a>)</td><td class="right " data-stat="exp_pts_before" >1.140</td><td class="right " data-stat="exp_pts_after" >0.560</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_122.000">5:49</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >1</td><td class="left " data-stat="location" csk="66" >DEN 34</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_122.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> up the middle for 2 yards (tackle by <a href="/players/B/BarnDe02.htm">Derrick Barnes</a>)</td><td class="right " data-stat="exp_pts_before" >0.560</td><td class="right " data-stat="exp_pts_after" >1.330</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_123.000">5:05</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="64" >DEN 36</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_123.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short right to <a href="/players/T/TrauAd00.htm">Adam Trautman</a> for 24 yards (tackle by <a href="/players/J/JoseKe03.htm">Kerby Joseph</a>)</td><td class="right " data-stat="exp_pts_before" >1.330</td><td class="right " data-stat="exp_pts_after" >2.920</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_124.000">4:19</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="40" >DET 40</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_124.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete deep middle intended for <a href="/players/K/KrulLu00.htm">Lucas Krull</a> (defended by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>)</td><td class="right " data-stat="exp_pts_before" >2.920</td><td class="right " data-stat="exp_pts_after" >2.370</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_125.000">4:12</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left iz" data-stat="location" csk="0" ></td><td class="right iz" data-stat="pbp_score_aw" ></td><td class="right iz" data-stat="pbp_score_hm" ></td><td class="left " data-stat="detail" ><a name="pbp_125.000"></a>Timeout #1 by Denver Broncos</td><td class="right iz" data-stat="exp_pts_before" ></td><td class="right iz" data-stat="exp_pts_after" ></td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_126.000">4:12</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="40" >DET 40</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_126.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> up the middle for no gain (tackle by <a href="/players/B/BuggIs00.htm">Isaiah Buggs</a> and <a href="/players/C/ComiJo00.htm">John Cominsky</a>)</td><td class="right " data-stat="exp_pts_before" >2.370</td><td class="right " data-stat="exp_pts_after" >1.680</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_127.000">3:32</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="40" >DET 40</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_127.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short left to <a href="/players/J/JeudJe00.htm">Jerry Jeudy</a> for 19 yards (tackle by <a href="/players/S/SuttCa00.htm">Cameron Sutton</a>)</td><td class="right " data-stat="exp_pts_before" >1.680</td><td class="right " data-stat="exp_pts_after" >4.170</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_128.000">2:47</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="21" >DET 21</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_128.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short middle to <a href="/players/S/SuttCo00.htm">Courtland Sutton</a> for 12 yards (tackle by <a href="/players/R/RodrMa00.htm">Malcolm Rodriguez</a>)</td><td class="right " data-stat="exp_pts_before" >4.170</td><td class="right " data-stat="exp_pts_after" >5.140</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_129.000">2:18</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="9" >DET 9</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_129.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short left intended for <a href="/players/S/SuttCo00.htm">Courtland Sutton</a> (defended by <a href="/players/S/SuttCa00.htm">Cameron Sutton</a>)</td><td class="right " data-stat="exp_pts_before" >5.140</td><td class="right " data-stat="exp_pts_after" >4.380</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_130.000">2:15</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="9" >DET 9</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_130.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short right to <a href="/players/M/McLaJa00.htm">Jaleel McLaughlin</a> for 8 yards (tackle by <a href="/players/R/ReevJa00.htm">Jalen Reeves-Maybin</a> and <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >4.380</td><td class="right " data-stat="exp_pts_after" >5.170</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_131.000">1:31</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >1</td><td class="left " data-stat="location" csk="1" >DET 1</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_131.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> left end for no gain (tackle by <a href="/players/B/BarnDe02.htm">Derrick Barnes</a> and <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >5.170</td><td class="right " data-stat="exp_pts_after" >3.550</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_132.000">0:51</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >1</td><td class="left " data-stat="location" csk="1" >DET 1</td><td class="right " data-stat="pbp_score_aw" >7</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_132.000"></a><a href="/players/B/BurtMi00.htm">Michael Burton</a> up the middle for no gain, touchdown. Penalty on <a href="/players/M/MeinQu02.htm">Quinn Meinerz</a>: Offensive Offside, 4 yards (accepted) (no play)</td><td class="right " data-stat="exp_pts_before" >3.550</td><td class="right " data-stat="exp_pts_after" >3.010</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_133.000">0:46</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >5</td><td class="left " data-stat="location" csk="5" >DET 5</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_133.000"></a><a href="/players/L/LutzWi00.htm">Wil Lutz</a> 23 yard field goal good</td><td class="right " data-stat="exp_pts_before" >3.010</td><td class="right " data-stat="exp_pts_after" >3.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_135.000">0:43</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="65" >DEN 35</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_135.000"></a><a href="/players/L/LutzWi00.htm">Wil Lutz</a> kicks off 65 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.610</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >3</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_136.000">0:43</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="25" >DET 25</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_136.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> right end for 7 yards (tackle by <a href="/players/H/HarrJo05.htm">Jonathan Harris</a>)</td><td class="right " data-stat="exp_pts_before" >0.610</td><td class="right " data-stat="exp_pts_after" >1.010</td></tr>

      
      <tr class="thead">
         <th aria-label="Quarter" data-stat="quarter" class=" center" >Quarter</th>
         <th aria-label="Time" data-stat="qtr_time_remain" class=" center" data-tip="Time remaining in this quarter" >Time</th>
         <th aria-label="Down" data-stat="down" class=" center" >Down</th>
         <th aria-label="ToGo" data-stat="yds_to_go" class=" center" >ToGo</th>
         <th aria-label="Location" data-stat="location" class=" left" data-tip="Play location" >Location</th>
         <th aria-label="DEN" data-stat="pbp_score_aw" class=" left" data-tip="Away Points" >DEN</th>
         <th aria-label="DET" data-stat="pbp_score_hm" class=" left" data-tip="Home Points" >DET</th>
         <th aria-label="Detail" data-stat="detail" class=" left" data-tip="Play description" >Detail</th>
         <th aria-label="EPB" data-stat="exp_pts_before" class=" left" data-tip="Expected points before this play, based on down, distance, and field position" >EPB</th>
         <th aria-label="EPA" data-stat="exp_pts_after" class=" left" data-tip="Expected points after this play (or actual scoring results of the play if it was a score)" >EPA</th>
      </tr>
      <tr class="thead onecell" ><td class="right center" data-stat="onecell" colspan="10" >4th Quarter</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_138.000">15:00</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >3</td><td class="left " data-stat="location" csk="32" >DET 32</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_138.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short right to <a href="/players/W/WillJa11.htm">Jameson Williams</a> for 14 yards (tackle by <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >1.010</td><td class="right " data-stat="exp_pts_after" >1.990</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_139.000">14:18</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="46" >DET 46</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_139.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> left tackle for 4 yards (tackle by <a href="/players/S/SingAl00.htm">Alex Singleton</a>)</td><td class="right " data-stat="exp_pts_before" >1.990</td><td class="right " data-stat="exp_pts_after" >1.990</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_140.000">13:39</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >6</td><td class="left " data-stat="location" csk="50" >DEN 50</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_140.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> up the middle for 9 yards (tackle by <a href="/players/J/JeweJo00.htm">Josey Jewell</a> and <a href="/players/S/SingAl00.htm">Alex Singleton</a>)</td><td class="right " data-stat="exp_pts_before" >1.990</td><td class="right " data-stat="exp_pts_after" >2.850</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_141.000">13:04</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="59" >DEN 41</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_141.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete deep left intended for <a href="/players/R/ReynJo00.htm">Josh Reynolds</a>. Penalty on <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>: Defensive Pass Interference, 16 yards (accepted) (no play)</td><td class="right " data-stat="exp_pts_before" >2.850</td><td class="right " data-stat="exp_pts_after" >3.910</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_142.000">12:58</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="75" >DEN 25</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >28</td><td class="left " data-stat="detail" ><a name="pbp_142.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> left tackle for 13 yards (tackle by <a href="/players/J/JeweJo00.htm">Josey Jewell</a> and <a href="/players/S/SingAl00.htm">Alex Singleton</a>)</td><td class="right " data-stat="exp_pts_before" >3.910</td><td class="right " data-stat="exp_pts_after" >4.780</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_143.000">12:17</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="88" >DEN 12</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >34</td><td class="left " data-stat="detail" ><a name="pbp_143.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> left end for 12 yards, touchdown</td><td class="right " data-stat="exp_pts_before" >4.780</td><td class="right " data-stat="exp_pts_after" >7.000</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_144.000">12:12</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="85" >DEN 15</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_144.000"></a><a href="/players/B/BadgMi00.htm">Michael Badgley</a> kicks extra point good</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_146.000">12:12</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="35" >DET 35</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_146.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> kicks off 65 yards, touchback.</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.610</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_147.000">12:12</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="75" >DEN 25</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_147.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> scrambles right end for 1 yard (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >0.610</td><td class="right " data-stat="exp_pts_after" >0.200</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_148.000">11:42</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >9</td><td class="left " data-stat="location" csk="74" >DEN 26</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_148.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete deep middle to <a href="/players/K/KrulLu00.htm">Lucas Krull</a> for 18 yards (tackle by <a href="/players/J/JoseKe03.htm">Kerby Joseph</a>)</td><td class="right " data-stat="exp_pts_before" >0.200</td><td class="right " data-stat="exp_pts_after" >1.860</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_149.000">11:18</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="56" >DEN 44</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_149.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short right intended for <a href="/players/K/KrulLu00.htm">Lucas Krull</a> (defended by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >1.860</td><td class="right " data-stat="exp_pts_after" >1.320</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_150.000">11:15</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="56" >DEN 44</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_150.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete deep right intended for <a href="/players/J/JeudJe00.htm">Jerry Jeudy</a></td><td class="right " data-stat="exp_pts_before" >1.320</td><td class="right " data-stat="exp_pts_after" >0.630</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_151.000">11:10</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="56" >DEN 44</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_151.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete deep left intended for <a href="/players/M/MimsMa00.htm">Marvin Mims</a> (defended by <a href="/players/V/VildKi00.htm">Kindle Vildor</a>)</td><td class="right " data-stat="exp_pts_before" >0.630</td><td class="right " data-stat="exp_pts_after" >-0.460</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_152.000">11:05</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="56" >DEN 44</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_152.000"></a><a href="/players/D/DixoRi00.htm">Riley Dixon</a> punts 48 yards, fair catch by <a href="/players/R/RaymKa00.htm">Kalif Raymond</a> at DET-8. Penalty on <a href="/players/S/SmitTr04.htm">Tremon Smith</a>: Unnecessary Roughness / Offense, 15 yards (accepted) </td><td class="right " data-stat="exp_pts_before" >-0.460</td><td class="right " data-stat="exp_pts_after" >-0.480</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_154.000">10:59</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="23" >DET 23</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_154.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass incomplete short right intended for <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a></td><td class="right " data-stat="exp_pts_before" >0.480</td><td class="right " data-stat="exp_pts_after" >-0.070</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_155.000">10:54</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="23" >DET 23</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_155.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> right end for -1 yards (tackle by <a href="/players/S/SimmJu00.htm">Justin Simmons</a>)</td><td class="right " data-stat="exp_pts_before" >-0.070</td><td class="right " data-stat="exp_pts_after" >-0.890</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_156.000">10:08</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >11</td><td class="left " data-stat="location" csk="22" >DET 22</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_156.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> sacked by <a href="/players/C/CoopJo02.htm">Jonathon Cooper</a> for -8 yards</td><td class="right " data-stat="exp_pts_before" >-0.890</td><td class="right " data-stat="exp_pts_after" >-2.470</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_157.000">9:29</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >19</td><td class="left " data-stat="location" csk="14" >DET 14</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_157.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> punts 48 yards downed by <a href="/players/R/RodrMa00.htm">Malcolm Rodriguez</a></td><td class="right " data-stat="exp_pts_before" >-2.470</td><td class="right " data-stat="exp_pts_after" >-1.470</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_159.000">9:18</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="62" >DEN 38</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_159.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short middle to <a href="/players/P/PeriSa00.htm">Samaje Perine</a> for 11 yards (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >1.470</td><td class="right " data-stat="exp_pts_after" >2.190</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_160.000">8:46</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="51" >DEN 49</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_160.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short middle to <a href="/players/J/JeudJe00.htm">Jerry Jeudy</a> for 15 yards (tackle by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>)</td><td class="right " data-stat="exp_pts_before" >2.190</td><td class="right " data-stat="exp_pts_after" >3.180</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_161.000">8:12</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="36" >DET 36</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_161.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short middle to <a href="/players/S/SuttCo00.htm">Courtland Sutton</a> for 14 yards (tackle by <a href="/players/B/BarnDe02.htm">Derrick Barnes</a>)</td><td class="right " data-stat="exp_pts_before" >3.180</td><td class="right " data-stat="exp_pts_after" >4.110</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_162.000">7:48</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="22" >DET 22</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_162.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass incomplete short left intended for <a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a></td><td class="right " data-stat="exp_pts_before" >4.110</td><td class="right " data-stat="exp_pts_after" >3.560</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_163.000">7:45</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="22" >DET 22</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_163.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> pass complete short right to <a href="/players/H/HumpLi01.htm">Lil'Jordan Humphrey</a> for 8 yards (tackle by <a href="/players/D/DorsKh00.htm">Khalil Dorsey</a>)</td><td class="right " data-stat="exp_pts_before" >3.560</td><td class="right " data-stat="exp_pts_after" >4.150</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_164.000">7:21</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >2</td><td class="left " data-stat="location" csk="14" >DET 14</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_164.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> right tackle for 1 yard (tackle by <a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a>)</td><td class="right " data-stat="exp_pts_before" >4.150</td><td class="right " data-stat="exp_pts_after" >2.720</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_165.000">6:51</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >1</td><td class="left " data-stat="location" csk="13" >DET 13</td><td class="right " data-stat="pbp_score_aw" >10</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_165.000"></a><a href="/players/P/PeriSa00.htm">Samaje Perine</a> up the middle for 12 yards (tackle by <a href="/players/J/JoseKe03.htm">Kerby Joseph</a>)</td><td class="right " data-stat="exp_pts_before" >2.720</td><td class="right " data-stat="exp_pts_after" >6.970</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_166.000">6:31</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >1</td><td class="left " data-stat="location" csk="1" >DET 1</td><td class="right " data-stat="pbp_score_aw" >16</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_166.000"></a><a href="/players/W/WilsRu00.htm">Russell Wilson</a> up the middle for 1 yard, touchdown</td><td class="right " data-stat="exp_pts_before" >6.970</td><td class="right " data-stat="exp_pts_after" >7.000</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_167.000">6:28</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="15" >DET 15</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_167.000"></a><a href="/players/L/LutzWi00.htm">Wil Lutz</a> kicks extra point good</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_169.000">6:28</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="65" >DEN 35</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_169.000"></a><a href="/players/L/LutzWi00.htm">Wil Lutz</a> kicks onside 9 yards, returned by <a href="/players/R/RodrMa00.htm">Malcolm Rodriguez</a> for no gain</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >2.650</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_170.000">6:27</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="56" >DEN 44</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_170.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> left tackle for 2 yards (tackle by <a href="/players/J/JeweJo00.htm">Josey Jewell</a> and <a href="/players/J/JoneD.01.htm">D.J. Jones</a>)</td><td class="right " data-stat="exp_pts_before" >2.650</td><td class="right " data-stat="exp_pts_after" >2.380</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_171.000">5:42</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >8</td><td class="left " data-stat="location" csk="58" >DEN 42</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_171.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short left to <a href="/players/S/StxxAm00.htm">Amon-Ra St. Brown</a> for 10 yards (tackle by <a href="/players/J/JeweJo00.htm">Josey Jewell</a>)</td><td class="right " data-stat="exp_pts_before" >2.380</td><td class="right " data-stat="exp_pts_after" >3.450</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_172.000">5:00</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="68" >DEN 32</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_172.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> right tackle for 5 yards (tackle by <a href="/players/C/CoopJo02.htm">Jonathon Cooper</a>)</td><td class="right " data-stat="exp_pts_before" >3.450</td><td class="right " data-stat="exp_pts_after" >3.580</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_173.000">4:55</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left iz" data-stat="location" csk="0" ></td><td class="right iz" data-stat="pbp_score_aw" ></td><td class="right iz" data-stat="pbp_score_hm" ></td><td class="left " data-stat="detail" ><a name="pbp_173.000"></a>Timeout #2 by Denver Broncos</td><td class="right iz" data-stat="exp_pts_before" ></td><td class="right iz" data-stat="exp_pts_after" ></td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_174.000">4:55</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >5</td><td class="left " data-stat="location" csk="73" >DEN 27</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_174.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> left end for 9 yards (tackle by <a href="/players/M/MoreFa00.htm">Fabian Moreau</a>)</td><td class="right " data-stat="exp_pts_before" >3.580</td><td class="right " data-stat="exp_pts_after" >4.370</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_175.000">4:42</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left iz" data-stat="location" csk="0" ></td><td class="right iz" data-stat="pbp_score_aw" ></td><td class="right iz" data-stat="pbp_score_hm" ></td><td class="left " data-stat="detail" ><a name="pbp_175.000"></a>Timeout #3 by Denver Broncos</td><td class="right iz" data-stat="exp_pts_before" ></td><td class="right iz" data-stat="exp_pts_after" ></td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_176.000">4:42</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="82" >DEN 18</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_176.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> up the middle for 2 yards (tackle by <a href="/players/P/PurcMi00.htm">Mike Purcell</a> and <a href="/players/H/HarrJo05.htm">Jonathan Harris</a>)</td><td class="right " data-stat="exp_pts_before" >4.370</td><td class="right " data-stat="exp_pts_after" >4.090</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_177.000">3:58</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >8</td><td class="left " data-stat="location" csk="84" >DEN 16</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_177.000"></a><a href="/players/M/MontDa01.htm">David Montgomery</a> left tackle for 2 yards (tackle by <a href="/players/P/PurcMi00.htm">Mike Purcell</a> and <a href="/players/M/McMiJa00.htm">Ja'Quan McMillian</a>)</td><td class="right " data-stat="exp_pts_before" >4.090</td><td class="right " data-stat="exp_pts_after" >3.630</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_178.000">3:13</a></td><td class="center " data-stat="down" >3</td><td class="center " data-stat="yds_to_go" >6</td><td class="left " data-stat="location" csk="86" >DEN 14</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >35</td><td class="left " data-stat="detail" ><a name="pbp_178.000"></a><a href="/players/G/GibbJa01.htm">Jahmyr Gibbs</a> left tackle for 4 yards (tackle by <a href="/players/S/SurtPa01.htm">Patrick Surtain</a> and <a href="/players/S/SandDr00.htm">Drew Sanders</a>)</td><td class="right " data-stat="exp_pts_before" >3.630</td><td class="right " data-stat="exp_pts_after" >2.890</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_179.000">2:26</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left iz" data-stat="location" csk="0" ></td><td class="right iz" data-stat="pbp_score_aw" ></td><td class="right iz" data-stat="pbp_score_hm" ></td><td class="left " data-stat="detail" ><a name="pbp_179.000"></a>Timeout #1 by Detroit Lions</td><td class="right iz" data-stat="exp_pts_before" ></td><td class="right iz" data-stat="exp_pts_after" ></td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_180.000">2:26</a></td><td class="center " data-stat="down" >4</td><td class="center " data-stat="yds_to_go" >2</td><td class="left " data-stat="location" csk="90" >DEN 10</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >41</td><td class="left " data-stat="detail" ><a name="pbp_180.000"></a><a href="/players/G/GoffJa00.htm">Jared Goff</a> pass complete short middle to <a href="/players/L/LaPoSa01.htm">Sam LaPorta</a> for 10 yards, touchdown</td><td class="right " data-stat="exp_pts_before" >2.890</td><td class="right " data-stat="exp_pts_after" >7.000</td></tr>
<tr class=" score" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_181.000">2:21</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="85" >DEN 15</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >42</td><td class="left " data-stat="detail" ><a name="pbp_181.000"></a><a href="/players/B/BadgMi00.htm">Michael Badgley</a> kicks extra point good</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.000</td></tr>
<tr class="divider" ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_182.000">2:21</a></td><td class="center iz" data-stat="down" ></td><td class="center iz" data-stat="yds_to_go" ></td><td class="left " data-stat="location" csk="35" >DET 35</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >42</td><td class="left " data-stat="detail" ><a name="pbp_182.000"></a><a href="/players/F/FoxxJa01.htm">Jack Fox</a> kicks off 59 yards, returned by <a href="/players/M/MimsMa00.htm">Marvin Mims</a> for 15 yards (tackle by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>)</td><td class="right " data-stat="exp_pts_before" >0.000</td><td class="right " data-stat="exp_pts_after" >0.340</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_183.000">2:15</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="79" >DEN 21</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >42</td><td class="left " data-stat="detail" ><a name="pbp_183.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> right tackle for 4 yards (tackle by <a href="/players/B/BuggIs00.htm">Isaiah Buggs</a> and <a href="/players/H/HutcAi00.htm">Aidan Hutchinson</a>)</td><td class="right " data-stat="exp_pts_before" >0.340</td><td class="right " data-stat="exp_pts_after" >0.340</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_185.000">2:00</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >6</td><td class="left " data-stat="location" csk="75" >DEN 25</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >42</td><td class="left " data-stat="detail" ><a name="pbp_185.000"></a><a href="/players/W/WillJa10.htm">Javonte Williams</a> left tackle for 8 yards (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a>)</td><td class="right " data-stat="exp_pts_before" >0.340</td><td class="right " data-stat="exp_pts_after" >1.140</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_186.000">1:25</a></td><td class="center " data-stat="down" >1</td><td class="center " data-stat="yds_to_go" >10</td><td class="left " data-stat="location" csk="67" >DEN 33</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >42</td><td class="left " data-stat="detail" ><a name="pbp_186.000"></a><a href="/players/P/PeriSa00.htm">Samaje Perine</a> up the middle for 5 yards (tackle by <a href="/players/M/MeliIf00.htm">Ifeatu Melifonwu</a>)</td><td class="right " data-stat="exp_pts_before" >1.140</td><td class="right " data-stat="exp_pts_after" >1.270</td></tr>
<tr ><th scope="row" class="center " data-stat="quarter" >4</th><td class="center " data-stat="qtr_time_remain" ><a href="#pbp_187.000">0:46</a></td><td class="center " data-stat="down" >2</td><td class="center " data-stat="yds_to_go" >5</td><td class="left " data-stat="location" csk="62" >DEN 38</td><td class="right " data-stat="pbp_score_aw" >17</td><td class="right " data-stat="pbp_score_hm" >42</td><td class="left " data-stat="detail" ><a name="pbp_187.000"></a><a href="/players/P/PeriSa00.htm">Samaje Perine</a> right end for 9 yards (tackle by <a href="/players/A/AnzaAl00.htm">Alex Anzalone</a> and <a href="/players/M/MartBr00.htm">Brodric Martin</a>)</td><td class="right " data-stat="exp_pts_before" >1.270</td><td class="right " data-stat="exp_pts_after" >2.060</td></tr>
<tr class="thead onecell" ><td class="right center" data-stat="onecell" colspan="10" >End of Regulation</td></tr>

</table>


</div>
-->
                </div>
                <!-- global.nonempty_tables_num: 17, table_count: 17 -->
                <!-- no Local/Partials/NoteBottom.tt2 -->
                <div id="bottom_nav" class="section_wrapper">
                    <div class="section_heading">
                        <span data-no-inpage="1" class="section_anchor" id="inner_nav_bottom_link" data-label="Schedules & Boxscores"></span>
                        <h2>Schedules & Boxscores</h2>
                    </div>
                    <div class="section_content" id="bottom_nav_container">
                        <p>
                            <a href="/boxscores/">NFL Scores & Boxes</a>
                        </p>
                        <p>
                            <a href="#">Schedules & Boxscores</a>
                        </p>
                        <ul class="">
                            <li>
                                <a href="/years/2023/">2023 NFL Scores & Schedule</a>
                            </li>
                            <li>
                                <a href="/teams/det/2023.htm">Detroit Lions Schedule</a>
                            </li>
                            <li>
                                <a href="/teams/den/2023.htm">Denver Broncos Schedule</a>
                            </li>
                        </ul>
                    </div>
                </div>
                <!-- fs_footer -->
                <div class="adblock">
                    <!-- div#fs_fs_footer  -->
                    <div align="center" id="div-gpt-ad-728x90-Footer" data-freestar-ad="__300x250 __970x90">
                        <script data-cfasync="false" type='text/javascript'>
                            if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {} else {
                                console.log('push ad:div-gpt-ad-728x90-Footer');
                                freestar.queue.push(function() {
                                    googletag.display('div-gpt-ad-728x90-Footer');
                                });
                            }
                        </script>
                    </div>
                    <!-- /div.#fs_fs_footer -->
                </div>
            </div>
            <!-- div#content -->
            <div id="footer" role="contentinfo">
                <div id="footer_header">
                    <ul class="bullets-inline">
                        <li class="user logged_in">
                            Welcome <span class="username"></span>
                            &nbsp;&#183;&nbsp;<a href="https://stathead.com/profile/?utm_source=pfr&amp;utm_medium=sr_xsite&amp;utm_campaign=2023_01_srnav_account">Your Account</a>
                        </li>
                        <li class="user logged_in">
                            <a class="logout" onclick="sr_auth_logout_page_elements();if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/profile/?do=logout">Logout</a>
                        </li>
                        <li class="user not_logged_in">
                            <a class="login" onclick="if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/users/login.cgi?token=1">Ad-Free Login</a>
                        </li>
                        <li class="user not_logged_in">
                            <a href="https://stathead.com/users/signup.cgi">Create Account</a>
                        </li>
                    </ul>
                    <div class="breadcrumbs">
                        You are here: 
                        <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                            <a itemprop="item" href="/">
                                <span itemprop="name">PFR Home Page</span>
                            </a>
                            <meta itemprop="position" content="1"/>
                        </span>
                        &gt;
                        <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                            <a itemprop="item" href="/boxscores/">
                                <span itemprop="name">Boxscores</span>
                            </a>
                            <meta itemprop="position" content="2"/>
                        </span>
                        &gt;<strong>Denver Broncos at Detroit Lions - December 16th, 2023</strong>
                    </div>
                </div>
                <!-- div#footer_header -->
                <div id="footer_general">
                    <div id="site_menu" role="navigation" aria-label="complete site index">
                        <div class="section_heading assoc_site_menu" id="site_menu_sh">
                            <span class="section_anchor" id="site_menu_link" data-label="Full Site Menu" data-no-inpage="1"></span>
                            <h2>Full Site Menu</h2>
                            <div class="section_heading_text">
                                <ul>
                                    <li>
                                        <a data-scroll href="#header">Return to Top</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <ul>
                            <li>
                                <a href="/players">Players</a>
                                <div>
                                    In the News: <a title="Brock Purdy" href="/players/P/PurdBr00.htm">Brock Purdy</a>
                                    , <a title="Christian McCaffrey" href="/players/M/McCaCh01.htm">Christian McCaffrey</a>
                                    , <a title="Baker Mayfield" href="/players/M/MayfBa00.htm">Baker Mayfield</a>
                                    , <a title="Justin Fields" href="/players/F/FielJu00.htm">Justin Fields</a>
                                    , <a title="Kyler Murray" href="/players/M/MurrKy00.htm">Kyler Murray</a>
                                    , <a title="Patrick Mahomes" href="/players/M/MahoPa00.htm">Patrick Mahomes</a>
                                    <a href="/players/">...</a>
                                </div>
                                <div>
                                    Popular: <a title="Tom Brady" href="/players/B/BradTo00.htm">Tom Brady</a>
                                    , <a title="Cam Newton" href="/players/N/NewtCa00.htm">Cam Newton</a>
                                    , <a title="Aaron Donald" href="/players/D/DonaAa00.htm">Aaron Donald</a>
                                    , <a title="Russell Wilson" href="/players/W/WilsRu00.htm">Russell Wilson</a>
                                    , <a title="Aaron Rodgers" href="/players/R/RodgAa00.htm">Aaron Rodgers</a>
                                    , <a title="Odell Beckham" href="/players/B/BeckOd00.htm">Odell Beckham Jr.</a>
                                    , <a title="J.J. Watt" href="/players/W/WattJ.00.htm">J.J. Watt</a>
                                    , <a title="Peyton Manning" href="/players/M/MannPe00.htm">Peyton Manning</a>
                                    , <a title="Patrick Mahomes" href="/players/M/MahoPa00.htm">Patrick Mahomes</a>
                                    , <a title="Julio Jones" href="/players/J/JoneJu02.htm">Julio Jones</a>
                                    , <a title="Antonio Brown" href="/players/B/BrowAn04.htm">Antonio Brown</a>
                                    , <a title="Ben Roethlisberger" href="/players/R/RoetBe00.htm">Ben Roethlisberger</a>
                                    , <a title="Drew Brees" href="/players/B/BreeDr00.htm">Drew Brees</a>
                                    , <a title="Todd Gurley" href="/players/G/GurlTo01.htm">Todd Gurley</a>
                                    <a href="/players/">...</a>
                                </div>
                                <div>
                                    <a href="/hof/">Hall of Famers</a>
                                    , <a href="/probowl/">Pro Bowlers</a>
                                    , <a href="/awards/ap-nfl-mvp-award.htm">MVPs</a>
                                    , <a href="/friv/linkify.cgi">Player Linker Tool</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/teams/">Teams</a>
                                <div>
                                    AFC East: <a href="/teams/mia/2023.htm">Dolphins</a>
                                    , <a href="/teams/buf/2023.htm">Bills</a>
                                    , <a href="/teams/nyj/2023.htm">Jets</a>
                                    , <a href="/teams/nwe/2023.htm">Patriots</a>
                                </div>
                                <div>
                                    AFC North: <a href="/teams/rav/2023.htm">Ravens</a>
                                    , <a href="/teams/cle/2023.htm">Browns</a>
                                    , <a href="/teams/cin/2023.htm">Bengals</a>
                                    , <a href="/teams/pit/2023.htm">Steelers</a>
                                </div>
                                <div>
                                    AFC South: <a href="/teams/htx/2023.htm">Texans</a>
                                    , <a href="/teams/jax/2023.htm">Jaguars</a>
                                    , <a href="/teams/clt/2023.htm">Colts</a>
                                    , <a href="/teams/oti/2023.htm">Titans</a>
                                </div>
                                <div>
                                    AFC West: <a href="/teams/kan/2023.htm">Chiefs</a>
                                    , <a href="/teams/den/2023.htm">Broncos</a>
                                    , <a href="/teams/rai/2023.htm">Raiders</a>
                                    , <a href="/teams/sdg/2023.htm">Chargers</a>
                                </div>
                                <div>
                                    NFC East: <a href="/teams/dal/2023.htm">Cowboys</a>
                                    , <a href="/teams/phi/2023.htm">Eagles</a>
                                    , <a href="/teams/nyg/2023.htm">Giants</a>
                                    , <a href="/teams/was/2023.htm">Commanders</a>
                                </div>
                                <div>
                                    NFC North: <a href="/teams/det/2023.htm">Lions</a>
                                    , <a href="/teams/min/2023.htm">Vikings</a>
                                    , <a href="/teams/gnb/2023.htm">Packers</a>
                                    , <a href="/teams/chi/2023.htm">Bears</a>
                                </div>
                                <div>
                                    NFC South: <a href="/teams/tam/2023.htm">Buccaneers</a>
                                    , <a href="/teams/nor/2023.htm">Saints</a>
                                    , <a href="/teams/atl/2023.htm">Falcons</a>
                                    , <a href="/teams/car/2023.htm">Panthers</a>
                                </div>
                                <div>
                                    NFC West: <a href="/teams/sfo/2023.htm">49ers</a>
                                    , <a href="/teams/ram/2023.htm">Rams</a>
                                    , <a href="/teams/sea/2023.htm">Seahawks</a>
                                    , <a href="/teams/crd/2023.htm">Cardinals</a>
                                </div>
                            </li>
                            <li>
                                <a href="/years/">Seasons</a>
                                <div>
                                    <a href="/years/2023/">Current Season</a>
                                    , <a href="/years/2023/games.htm">Current Season Schedule</a>
                                    , <a href="/years/2023/leaders.htm">Current Leaders</a>
                                </div>
                                <div>
                                    <a href="/years/2022/">2022</a>
                                    , <a href="/years/2021/">2021</a>
                                    , <a href="/years/2020/">2020</a>
                                    , <a href="/years/2019/">2019</a>
                                    , <a href="/years/2018/">2018</a>
                                    , <a href="/years/">...</a>
                                </div>
                            </li>
                            <li>
                                <a href="/leaders/">NFL Leaders</a>
                                <div>
                                    <a href="/leaders/pass_yds_career.htm">Career Passing Yards</a>
                                    , <a href="/leaders/rush_td_single_season.htm">Single Season Rush TD</a>
                                    , <a href="/leaders/sacks_single_game.htm">Single Game Sacks</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/boxscores/">NFL Scores</a>
                                <div>
                                    <a href="/boxscores/game-scores.htm">All-time Scores</a>
                                    , <a href="/boxscores/game_scores_find.cgi">Find a Score</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/draft/">NFL Draft</a>
                                <div>
                                    <a href="/years/2023/draft.htm">2023 Draft</a>
                                    , <a href="/draft/">Draft History</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a target='_blank' rel='noopener' href="https://stathead.com/football/?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Stathead</a>
                                <div>
                                    <strong>Player Finders</strong>
                                    : 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player-season-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Season Finder</a>
                                    , 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player-game-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Game Finder</a>
                                    , 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player-streak-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Streak Finder</a>
                                    ,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player-span-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Span Finder</a>
                                    ,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player_split_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Split Finder</a>
                                </div>
                                <div>
                                    <strong>Team Finders</strong>
                                    : 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/team-season-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Season Finder</a>
                                    , 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/team-game-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Game Finder</a>
                                    , 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/team-streak-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Streak Finder</a>
                                    ,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/team-span-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Span Finder</a>
                                    ,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/split_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Split Finder</a>
                                </div>
                                <div>
                                    <strong>Other Finders</strong>
                                    : 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/versus-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Versus Finder</a>
                                    ,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/ptd_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Touchdown Finder</a>
                                    ,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/fg_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Field Goal Finder</a>
                                    ,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/play_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Game Play Finder</a>
                                    ,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/drive_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Drive Finder</a>
                                </div>
                            </li>
                            <li>
                                <a href="/super-bowl/">Super Bowl Winners</a>
                                <div>
                                    <a href="/super-bowl/leaders.htm">Super Bowl Leaders</a>
                                    , <a href="/super-bowl/standings.htm">Super Bowl Standings</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/schools/">Schools</a>
                                <div>
                                    <a href="/schools/">All Player Colleges</a>
                                    , <a href="/schools/high_schools.cgi">High Schools</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/coaches/">NFL Coaches</a>
                                <div>
                                    Active Coaches: <a href="/coaches/BeliBi0.htm">Bill Belichick</a>
                                    , <a href="/coaches/ReidAn0.htm">Andy Reid</a>
                                    , <a href="/coaches/TomlMi0.htm">Mike Tomlin</a>
                                    , <a href="/coaches/CarrPe0.htm">Pete Carroll</a>
                                    ...
                                </div>
                                <div>
                                    Historical Coaches: <a href="/coaches/ShulDo0.htm">Don Shula</a>
                                    , <a href="/coaches/HalaGe0.htm">George Halas</a>
                                    , <a href="/coaches/LandTo0.htm">Tom Landry</a>
                                    , <a href="/coaches/LambCu0.htm">Curly Lambeau</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/executives/">Executives</a>
                                <div>
                                    <a href="/executives/AdamBu0.htm">Bud Adams</a>
                                    , <a href="/executives/PiolSc0.htm">Scott Pioli</a>
                                    , <a href="/executives/HalaGe0.htm">George Halas</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/officials/">NFL Officials</a>
                                <div>
                                    <a href="/officials/HochEd0r.htm">Ed Hochuli</a>
                                    , <a href="/officials/SterTo0r.htm">Tony Steratore</a>
                                    , <a href="/officials/McAuTe0r.htm">Terry McAulay</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/fantasy/">Fantasy Football Stats</a>
                                <div>
                                    <a href="/fantasy/QB-fantasy-matchups.htm">Current Fantasy Matchups</a>
                                    , <a href="/years/2023/fantasy-points-against-QB.htm">Fantasy Points Allowed</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/stadiums/">Stadiums</a>
                                <div>
                                    <a href="/stadiums/GNB00.htm">Lambeau Field</a>
                                    , <a href="/stadiums/NOR00.htm">Superdome</a>
                                    , <a href="/stadiums/SFO00.htm">Candlestick Park</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/awards/">NFL Awards</a>
                                <div>
                                    <a href="/hof/">Pro Football Hall of Fame</a>
                                    , <a href="/awards/ap-nfl-mvp-award.htm">AP NFL MVP</a>
                                    , <a href="/probowl/">Pro Bowl</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/friv/">Frivolities</a>
                                <div>
                                    <a href="/friv/players-who-played-for-multiple-teams-franchises.fcgi">Players who played for multiple teams</a>
                                    , <a href="/linker">Player Linker Tool</a>
                                    , <a href="/friv/birthdays.cgi">Birthdays</a>
                                    , <a href="/players/uniform.cgi">Uniform Numbers</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="/about/">About</a>
                                <div>
                                    <a href="/about/glossary.htm">Glossary</a>
                                    , <a href="/about/minimums.htm">Stat Minimums</a>
                                    , <a href="/about/nfl-football-faqs.html">Frequently Asked Questions about the NFL and Football</a>
                                    ...
                                </div>
                            </li>
                            <li>
                                <a href="https://www.immaculategrid.com/football/?utm_campaign=2023_07_lnk_home_footer_ig&utm_source=pfr&utm_medium=sr_xsite">Immaculate Grid</a>
                                <div>Put your football knowledge to the test with our daily football trivia game. Can you complete the grid?</div>
                            <li>
                            <li>
                                <a href="
	</ul>

			
   		        

      <ul>
       <li></li>      
       <li><a href=" https://www.pro-football-reference.com/pfr-blog /">Pro-Football-Reference.com Blog and Articles</a></li>

	        </div><!-- div#site_menu -->
		<div>
			<div id=" social " class=" icon_group noload ">
	
<div class=" section_heading assoc_ " id=" _sh ">
  <span class=" section_anchor " id=" _link " data-label=" We 're Social...for Statheads" data-no-inpage="1"></span><h2>We' re Social...for Statheads </h2>		
</div>
                                    <a href="tel://888-512-8907" data-tip="Call us on Telephone" data-label="Telephone" aria-label="Telephone" class="poptip">
                                        <svg class="icon phone">
                                            <use xlink:href="#ic-phone"></use>
                                        </svg>
                                    </a>
                                    <a href="//www.sports-reference.com/blog/" data-tip="The Sports Reference Blog" data-label="Our Blog" aria-label="Our Blog" class="poptip">
                                        <svg class="icon wordpress">
                                            <use xlink:href="#ic-wordpress"></use>
                                        </svg>
                                    </a>
                                    <a href="https://www.sports-reference.com/blog/feed/" data-tip="Our Blog's RSS Feed" data-label="RSS Feed" aria-label="RSS Feed" class="poptip">
                                        <svg class="icon rss">
                                            <use xlink:href="#ic-rss"></use>
                                        </svg>
                                    </a>
                                    <a href="https://www.facebook.com/Pro.Football.Reference" data-tip="Pro-Football-Reference.com at Facebook" data-label="Facebook" aria-label="Facebook" class="poptip">
                                        <svg class="icon facebook">
                                            <use xlink:href="#ic-facebook"></use>
                                        </svg>
                                    </a>
                                    <a href="https://twitter.com/pfref" data-tip="Pro-Football-Reference.com at Twitter" data-label="Twitter" aria-label="Twitter" class="poptip">
                                        <svg class="icon twitter">
                                            <use xlink:href="#ic-twitter"></use>
                                        </svg>
                                    </a>
                                    <a href="https://instagram.com/profootballreference" data-tip="Pro-Football-Reference.com at Instagram" data-label="Instagram" aria-label="Instagram" class="poptip">
                                        <svg class="icon instagram">
                                            <use xlink:href="#ic-instagram"></use>
                                        </svg>
                                    </a>
                                    <a href="https://www.tiktok.com/@profootballreference" data-tip="Pro-Football-Reference.com at TikTok" data-label="TikTok" aria-label="TikTok" class="poptip">
                                        <svg class="icon tiktok">
                                            <use xlink:href="#ic-tiktok"></use>
                                        </svg>
                                    </a>
                                    <a href="https://reddit.com/r/SportsReference" data-tip="Reddit/r/SportsReference" data-label="Reddit/r/SR" aria-label="Reddit/r/SR" class="poptip">
                                        <svg class="icon reddit">
                                            <use xlink:href="#ic-reddit"></use>
                                        </svg>
                                    </a>
                                    <a href="https://www.youtube.com/user/sportsreference" data-tip="YouTube/SportsReference" data-label="YouTube" aria-label="YouTube" class="poptip">
                                        <svg class="icon youtube">
                                            <use xlink:href="#ic-youtube"></use>
                                        </svg>
                                    </a>
                                    <a href="https://www.linkedin.com/company/sports-reference-llc" data-tip="Follow SR on LinkedIn" data-label="LinkedIn" aria-label="LinkedIn" class="poptip">
                                        <svg class="icon linkedin">
                                            <use xlink:href="#ic-linkedin"></use>
                                        </svg>
                                    </a>
                                    <a href="https://www.paypal.me/sportsref" data-tip="Send us money via PayPal" data-label="PayPal" aria-label="PayPal" class="poptip">
                                        <svg class="icon paypal">
                                            <use xlink:href="#ic-paypal"></use>
                                        </svg>
                                    </a>
                                    <p>
                                        Every <a href="https://www.sports-reference.com/blog/sports-reference-social-media/">Sports Reference Social Media Account</a>
                                    </p>
                                    <p>
                                        <strong>Site Last Updated:</strong>
                                        Saturday, December 23,  6:36AM

                                    </p>
                                    <p>
                                        <a href="https://www.sports-reference.com/feedback/" class="button" style="display: block">Question, Comment, Feedback, or Correction?</a>
                                    </p>
                                    <p>
                                        <a style="display: block" href="https://www.pro-football-reference.com/email" class="button">Subscribe to our Free Email Newsletter</a>
                                    </p>
                                    <p>
                                        <a style="background-color:#7e3e89; color: #fff;" href="https://stathead.com/sport/football/?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footerbttn_stathead" class="button alt">
                                            Subscribe to Stathead Football: Get your first month FREE<br>
                                            <em>Your All-Access Ticket to the Pro Football Reference Database</em>
                                        </a>
                                    </p>
                                    <p>
                                        <a href="https://www.sports-reference.com/blog/ways-sports-reference-can-help-your-website/?utm_medium=sr&utm_source=pfr&utm_campaign=site-footer-ways-help">Do you have a sports website? Or write about sports? We have tools and resources that can help you use sports data.  Find out more.</a>
                                    </p>
                    </div>
                    <!-- div#social -->
                    <div id="tips_tricks">
                        <div class="section_heading assoc_tips" id="tips_sh">
                            <span class="section_anchor" id="tips_link" data-label="FAQs, Tip &amp; Tricks" data-no-inpage="1"></span>
                            <h2>FAQs, Tip &amp;Tricks</h2>
                        </div>
                        <ul>
                            <li>
                                Learn about the <a href="https://www.pro-football-reference.com/blog/index37a8.html">Approximate Value Formula</a>
                            </li>
                            <li>
                                Details on the Pro Football Reference <a href="https://www.pro-football-reference.com/about/win_prob.htm">Win Probability</a>
                            </li>
                            <li>
                                <a href="//www.sports-reference.com/blog/category/tips-and-tricks/">Tips and Tricks from our Blog.</a>
                            </li>
                            <li>
                                <a href="/linker/">Do you have a blog? Join our linker program.</a>
                            </li>
                            <li>
                                <a href="https://www.sports-reference.com/blog/category/stathead-tutorial-series/">Watch our How-To Videos to Become a Stathead</a>
                            </li>
                            <li>
                                <a href="//stathead.com/?ref=pfr">Subscribe to Stathead and get access to more data than you can imagine</a>
                            </li>
                        </ul>
                    </div>
                    <!-- div#tips_tricks -->
                    <div id="credits">
                        <p>
                            All logos are the trademark &amp;property of their owners and not Sports Reference LLC.  We present them here for purely educational purposes.
				<a href="https://www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">Our reasoning for presenting offensive logos.</a>
                        </p>
                        <p>
                            Logos were compiled by the amazing <a href="http://sportslogos.net/">SportsLogos.net.</a>
                        </p>
                        <div class="notice">
                            <p>
                                Data Provided By
	
                                <a href="https://www.sportradar.com/" rel="nofollow">
                                    <img alt="SportRadar" border=0 width=275 src="https://cdn.ssref.net/req/202311303/images/klecko/sportradar.png" style="background-color:#666; padding:.5em; border-radius:.25em">
                                </a>
                            </p>
                        </div>
                        <p>
                            Copyright &copy;2000-2023 <a href="//www.sports-reference.com/">Sports Reference LLC</a>
                            . All rights reserved.
                        </p>
                        <p>The SPORTS REFERENCE and STATHEAD trademarks are owned exclusively by Sports Reference LLC. Use without license or authorization is expressly prohibited.

                        <p>
                            Please see our <a href="https://www.pro-football-reference.com/about/sources.htm">Contributors and Sources page</a>
                            for data source details.
                        </p>
                    </div>
                    <!-- div#credits -->
                </div>
            </div>
            <ul id="site_dirs" class="notranslate bullets-inline">
                <li>
                    <a href="https://www.sports-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">
                        <svg height="15px" width="20px">
                            <use xlink:href="#ic-sr-pennant"></use>
                        </svg>
                        Sports &nbsp;Reference &#8239;&reg;
                    </a>
                </li>
                <li>
                    <a href="https://www.baseball-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Baseball</a>
                </li>
                <li class="current">
                    <a href="https://www.pro-football-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Football</a>
                    <a href="https://www.sports-reference.com/cfb/">(college)</a>
                </li>
                <li>
                    <a href="https://www.basketball-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Basketball</a>
                    <a href="https://www.sports-reference.com/cbb/">(college)</a>
                </li>
                <li>
                    <a href="https://www.hockey-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Hockey</a>
                </li>
                <li>
                    <a href="https://fbref.com/pt/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Futebol</a>
                </li>
                <li>
                    <a href="https://www.sports-reference.com/blog/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Blog</a>
                </li>
                <li>
                    <a href="https://stathead.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Stathead &#8239;&reg;</a>
                </li>
                <li>
                    <a href="https://www.immaculategrid.com/football/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Immaculate Grid</a>
                </li>
            </ul>
            <div id="about">
                <a href="//www.sports-reference.com/about.html">About</a>
                &bull;<a href="//www.sports-reference.com/termsofuse.html">Conditions &amp;Terms of Service</a>
                &bull;<a href="//www.sports-reference.com/advertise.html">Advertise With Us</a>
                &bull;<a href="//www.sports-reference.com/jobs.html">Jobs at SR</a>
                <br>
                <br>
                Sports Reference Purpose: We will be the trusted source of information and tools that inspire and empower users to enjoy, understand, and share the sports they love.
  <br>
                <br>
                <a href="//www.sports-reference.com/privacy.html">Privacy Policy</a>
                &bull;<a href="//www.sports-reference.com/gambling-revenue-policy.html">Gambling Revenue Policy</a>
                &bull;<a href="//www.sports-reference.com/accessibility-policy.html">Accessibility Policy</a>
                &bull;<a href="//www.sports-reference.com/data_use.html">Use of Data</a>
            </div>
            <!-- div#about -->
        </div>
        <!-- div#footer -->
</div>
<!-- div#wrap -->
<!-- yes sticky url:  https://www.pro-football-reference.com/boxscores/202312160det.htm -->
<div id="fs-select-footer"></div>
<!-- rails -->
<div class="adblock rails  left">
    <!-- div#fs_fs_rails_left  -->
    <div align="center" id="div-gpt-ad-160x600-1" data-freestar-ad="">
        <script data-cfasync="false" type='text/javascript'>
            if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {} else {
                console.log('push ad:div-gpt-ad-160x600-1');
                freestar.queue.push(function() {
                    googletag.display('div-gpt-ad-160x600-1');
                });
            }
        </script>
    </div>
    <!-- /div.#fs_fs_rails_left -->
</div>
<div class="adblock rails right">
    <!-- div#fs_fs_rails_right  -->
    <div align="center" id="div-gpt-ad-160x600-2" data-freestar-ad="">
        <script data-cfasync="false" type='text/javascript'>
            if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {} else {
                console.log('push ad:div-gpt-ad-160x600-2');
                freestar.queue.push(function() {
                    googletag.display('div-gpt-ad-160x600-2');
                });
            }
        </script>
    </div>
    <!-- /div.#fs_fs_rails_right -->
</div>
<!-- sr_gender is used in Templates/Assets/GoogleAnalytics.tt2 -->
<script>
    var sr_gender = "";
</script>
<!-- Google Analytics -->
<!-- Google Analytics UA,  UA-1890630-3 -->
<!-- Google Analytics GA4, G-EMBDG7RM0K -->
<!-- Google Tag Manager -->
<script>
    (function(w, d, s, l, i) {
        w[l] = w[l] || [];
        w[l].push({
            'gtm.start': new Date().getTime(),
            event: 'gtm.js'
        });
        var f = d.getElementsByTagName(s)[0]
          , j = d.createElement(s)
          , dl = l != 'dataLayer' ? '&l=' + l : '';
        j.async = true;
        j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
        f.parentNode.insertBefore(j, f);
    }
    )(window, document, 'script', 'dataLayer', 'GTM-MC36NL2');
</script>
<!-- End Google Tag Manager -->
<!-- Google Tag Manager (noscript) -->
<noscript>
    <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MC36NL2" height="0" width="0" style="display:none;visibility:hidden"></iframe>
</noscript>
<!-- End Google Tag Manager (noscript) -->
<script>
    var sr_cookie = vjs_readCookie('stathead_user') || '';
    var sr_cookie_split = sr_cookie.split("::");
    var sr_session_key = (sr_cookie_split.length > 1) ? sr_cookie_split[2] : '';
    var sr_ad_free_key = "3";
    var sr_site_id = "pfr";
    var sr_is_subscriber = (sr_ad_free_key && sr_session_key.vjs_isMatch(new RegExp(sr_ad_free_key + "$"))) || sr_session_key.vjs_isMatch(/1$/) || (sr_site_id === 'stathead' && sr_session_key.vjs_isMatch(/[0-7]$/));
    var sr_is_user = sr_cookie !== null && sr_cookie !== '';
    var sr_seen_modal = vjs_readCookie('modal_ad') !== null;
    var sr_device = 'unk';
    if (Modernizr.phone) {
        sr_device = 'phone';
    } else if (Modernizr.tablet) {
        sr_device = 'tablet';
    } else if (Modernizr.laptop) {
        sr_device = 'laptop';
    } else if (Modernizr.desktop) {
        sr_device = 'desktop';
    }
    var sr_stathead_site = vjs_readCookie('stathead_site') || '';
    var sr_stathead_type = vjs_readCookie('stathead_type') || '';
    window.dataLayer = window.dataLayer || [];
    function gtag() {
        dataLayer.push(arguments);
    }
    gtag('js', new Date());
    /* GA4: individual site code config, do not send a page view (double counts) */
    gtag('config', 'G-EMBDG7RM0K', {
        'is_sub': sr_is_subscriber,
        'is_user': sr_is_user,
        'page_gender': typeof (sr_gender) === 'string' ? sr_gender : null,
        'stathead_type': sr_stathead_type,
        'stathead_site': sr_stathead_site,
        'viewport_width': Modernizr.viewport_width,
        send_page_view: false
    });
    /* GA4: all sr sites together */
    /* I believe linker works as a parameter here, although there didn\'t seem to be a simple "true" value to set besides this one --NW https://developers.google.com/analytics/devguides/collection/gtagjs/cross-domain Add configs for both sets of code. */
    gtag('config', 'G-80FRT7VJ60', {
        'linker': {
            'domains': ['stathead.com']
        },
        'is_sub': sr_is_subscriber,
        'is_user': sr_is_user,
        'page_gender': typeof (sr_gender) === 'string' ? sr_gender : null,
        'stathead_type': sr_stathead_type,
        'stathead_site': sr_stathead_site,
        'viewport_width': Modernizr.viewport_width
    });
</script>
<!-- End Google Analytics -->
<!-- Start of HubSpot Embed Code -->
<script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/20503178.js"></script>
<!-- End of HubSpot Embed Code -->
</body>
<!-- SR -->
</html>
"""
