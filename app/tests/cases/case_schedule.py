# flake8: noqa
# pylint: skip-file

SCHEDULE_PAGE = """
<!DOCTYPE html>
<html data-version="klecko-" data-root="/home/pfr/build" lang="en" class="no-js" >
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0" />
    <link rel="dns-prefetch" href="https://cdn.ssref.net/req/202311303" />
<!-- Quantcast Choice. Consent Manager Tag v2.0 (for TCF 2.0) -->
<script type="text/javascript" async=true>
    (function() {
	var host = window.location.hostname;
	var element = document.createElement('script');
	var firstScript = document.getElementsByTagName('script')[0];
	var url = 'https://cmp.quantcast.com'
	    .concat('/choice/', 'XwNYEpNeFfhfr', '/', host, 
		    '/choice.js?tag_version=V2');
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
		    if (
			args.length > 3 &&
			    args[2] === 2 &&
			    typeof args[3] === 'boolean'
		    ) {
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
		    if(args[0] === 'init' && typeof args[3] === 'object') {
			args[3] = Object.assign(args[3], { tag_version: 'V2' });
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
		    window.__tcfapi(
			payload.command,
			payload.version,
			function(retValue, success) {
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
			},
			payload.parameter
		    );
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
	};

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
    })();
</script>
<!-- End Quantcast Choice. Consent Manager Tag v2.0 (for TCF 2.0) -->


    <title>2023 NFL Weekly League Schedule | Pro-Football-Reference.com</title>



    <meta name="Description" content="Check out the 2023 NFL Weekly League Schedule including AFC and NFC results and standings on Pro-football-reference.com">
    <link rel="canonical" href="https://www.pro-football-reference.com/years/2023/games.htm" />


<!-- include:start  ="/inc/klecko_header_full_pfr.html_f" -->
<!-- yes:cookie regular load the cached css -->
<script>function gup(n) {n = n.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]'); var r = new RegExp('[\\?&]'+n+'=([^&#]*)'); var re = r.exec(location.search);   return re === null?'':decodeURIComponent(re[1].replace(/\+/g,' '));}; document.srdev = gup('srdev')</script>
<script>if (!document.srdev && (location.hostname === 'sup.fb.srdevel.com')) { document.srdev = 'aw'; }/* sf: hardcode this in for sup.fb.srdevel.com for testing purposes. */</script>
<link rel="preconnect" href="https://cdn.ssref.net" crossorigin>
<link rel="preconnect" href="https://www.google-analytics.com"  crossorigin>
<link rel="preconnect" href="https://www.googletagservices.com" crossorigin>
<link rel="preload"    href="https://cdn.ssref.net/req/202311303/js/pfr/sr-min.js" as="script" crossorigin>
<link rel="preload"    href="https://cdn.ssref.net/req/202311303/icons/sr_icons-min.svg?pfr" as="fetch" crossorigin>
<link rel="preload"    href="https://www.pro-football-reference.com/short/inc/main_nav_menu.json" as="fetch" crossorigin>
<link rel="preload"    href="https://cdn.ssref.net/req/201604190/images/chosen-sprite.png" as="image" crossorigin>
<link rel="preload"    href="https://cdn.ssref.net/req/202311303/css/pfr/sr-min.css" as="style"    crossorigin>

<!-- CSS start -->
<link rel="stylesheet" href="https://cdn.ssref.net/req/202311303/css/pfr/sr-min.css" type="text/css"
      onload="if (document.srdev) { this.href = 'https://cdn.ssref.net/nocdn/dev/'.concat(document.srdev.substr(0,2),'/css/pfr/sr.css'); }" />
<!-- CSS END -->

<!-- JS START -->
<script class="allowed">var sr_is_production = true;
function vjs_getUrlParameter(e){e=e.replace(/[\[]/,"\\[").replace(/[\]]/,"\\]");e=new RegExp("[\\?&]"+e+"=([^&#]*)").exec(location.search);return null===e?"":decodeURIComponent(e[1].replace(/\+/g," "))}document.lang="","/es/"===window.location.pathname.substr(0,4)?document.lang="es":"/pt/"===window.location.pathname.substr(0,4)?document.lang="pt":"/fr/"===window.location.pathname.substr(0,4)?document.lang="fr":"/it/"===window.location.pathname.substr(0,4)?document.lang="it":"/de/"===window.location.pathname.substr(0,4)?document.lang="de":(window.location.pathname.substr(0,4),document.lang="en"),vjs_getUrlParameter("lang")&&(document.lang=vjs_getUrlParameter("lang")),document.srdev=null,vjs_getUrlParameter("srdev")?document.srdev=vjs_getUrlParameter("srdev"):"sup"===window.location.host.substr(0,3)&&(document.srdev="aw");var el,log_performance=!0,is_new_jscss_version=!1,sr_detect_operaMini=-1<navigator.userAgent.indexOf("Opera Mini"),sr_detect_firefox=(sr_detect_operaMini&&((el=document.querySelector("html")).className=el.className.concat(" operamini")),-1<navigator.userAgent.indexOf("Firefox")),sr_detect_firefoxMobile=(sr_detect_firefox&&((el=document.querySelector("html")).className=el.className.concat(" firefox")),-1<navigator.userAgent.indexOf("Firefox")&&(-1<navigator.userAgent.indexOf("Mobile")||-1<navigator.userAgent.indexOf("Tablet"))),sr_detect_ie=(sr_detect_firefoxMobile&&((el=document.querySelector("html")).className=el.className.concat(" firefox-mobile")),function(){var e=window.navigator.userAgent;if(0<e.indexOf("Trident/7.0"))return 11;if(0<e.indexOf("Trident/6.0"))return 10;if(0<e.indexOf("Trident/5.0"))return 9;for(var t=3,n=document.createElement("div"),r=n.getElementsByTagName("i");n.innerHTML="\x3c!--[if gt IE "+ ++t+"]><i></i><![endif]--\x3e",r[0];);return 4<t&&t}()),sr_detect_edge=!sr_detect_ie&&!!window.StyleMedia,sr_detect_safari=/Safari/.test(navigator.userAgent)&&/Apple Computer/.test(navigator.vendor),className="no-js",patt=((el=document.querySelector("html")).classList?el.classList.remove(className):el.className=el.className.replace(new RegExp("(^|\\b)"+className.split(" ").join("|")+"(\\b|$)","gi")," "),el.className=el.className.concat(" js"),!function(s,d,S){function E(e,t){return typeof e===t}function T(e){return"function"!=typeof d.createElement?d.createElement(e):m?d.createElementNS.call(d,"http://www.w3.org/2000/svg",e):d.createElement.apply(d,arguments)}function R(e,t,n,r){var o,i,s,a,l="modernizr",c=T("div");(a=d.body)||((a=T(m?"svg":"body")).fake=!0);if(parseInt(n,10))for(;n--;)(i=T("div")).id=r?r[n]:l+(n+1),c.appendChild(i);return(o=T("style")).type="text/css",o.id="s"+l,(a.fake?a:c).appendChild(o),a.appendChild(c),o.styleSheet?o.styleSheet.cssText=e:o.appendChild(d.createTextNode(e)),c.id=l,a.fake&&(a.style.background="",a.style.overflow="hidden",s=u.style.overflow,u.style.overflow="hidden",u.appendChild(a)),o=t(c,e),a.fake?(a.parentNode.removeChild(a),u.style.overflow=s,u.offsetHeight):c.parentNode.removeChild(c),!!o}function U(e){return e.replace(/([a-z])-([a-z])/g,function(e,t,n){return t+n.toUpperCase()}).replace(/^-/,"")}function D(e){return e.replace(/([A-Z])/g,function(e,t){return"-"+t.toLowerCase()}).replace(/^ms-/,"-ms-")}function q(e,t){var n=e.length;if("CSS"in s&&"supports"in s.CSS){for(;n--;)if(s.CSS.supports(D(e[n]),t))return!0;return!1}if("CSSSupportsRule"in s){for(var r=[];n--;)r.push("("+D(e[n])+":"+t+")");return R("@supports ("+(r=r.join(" or "))+") { #modernizr { position: absolute; } }",function(e){return"absolute"==(e=e,t=null,n="position","getComputedStyle"in s?(r=getComputedStyle.call(s,e,t),o=s.console,null!==r?n&&(r=r.getPropertyValue(n)):o&&o[o.error?"error":"log"].call(o,"getComputedStyle returning null, its possible modernizr test results are inaccurate")):r=!t&&e.currentStyle&&e.currentStyle[n],r);var t,n,r,o})}return S}function r(e,t,n,r,o){var i,s,a=e.charAt(0).toUpperCase()+e.slice(1),l=(e+" "+re.join(a+" ")+a).split(" ");if(E(t,"string")||void 0===t){var c=l,d=t,u=r,m=o;function f(){p&&(delete L.style,delete L.modElem)}if(m=void 0!==m&&m,void 0!==u){l=q(c,u);if(void 0!==l)return l}for(var p,h,g,v,_,w=["modernizr","tspan","samp"];!L.style&&w.length;)p=!0,L.modElem=T(w.shift()),L.style=L.modElem.style;for(g=c.length,h=0;h<g;h++)if(v=c[h],_=L.style[v],~(""+v).indexOf("-")&&(v=U(v)),L.style[v]!==S){if(m||void 0===u)return f(),"pfx"!=d||v;try{L.style[v]=u}catch(e){}if(L.style[v]!=_)return f(),"pfx"!=d||v}f()}else{var y=(e+" "+P.join(a+" ")+a).split(" "),b=t,x=n;for(s in y)if(y[s]in b)if(!1===x)return y[s];else{i=b[y[s]];if(E(i,"function")){var M=i;var z=x||b;return function(){return M.apply(z,arguments)};return}else return i}}return!1}function F(e,t,n){return r(e,S,S,t,n)}var $=[],o=[],e={_version:"3.6.0",_config:{classPrefix:"",enableClasses:!0,enableJSClass:!0,usePrefixes:!0},_q:[],on:function(e,t){var n=this;setTimeout(function(){t(n[e])},0)},addTest:function(e,t,n){o.push({name:e,fn:t,options:n})},addAsyncTest:function(e){o.push({name:null,fn:e})}},n=function(){},a=(n.prototype=e,(n=new n).addTest("cookies",function(){try{d.cookie="cookietest=1";var e=-1!=d.cookie.indexOf("cookietest=");return d.cookie="cookietest=1; expires=Thu, 01-Jan-1970 00:00:01 GMT",e}catch(e){return!1}}),n.addTest("localstorage",function(){var e="modernizr";try{return localStorage.setItem(e,e),localStorage.removeItem(e),!0}catch(e){return!1}}),n.addTest("sessionstorage",function(){var e="modernizr";try{return sessionStorage.setItem(e,e),sessionStorage.removeItem(e),!0}catch(e){return!1}}),n.addTest("cors","XMLHttpRequest"in s&&"withCredentials"in new XMLHttpRequest),n.addTest("history",function(){var e=navigator.userAgent;return(-1===e.indexOf("Android 2.")&&-1===e.indexOf("Android 4.0")||-1===e.indexOf("Mobile Safari")||-1!==e.indexOf("Chrome")||-1!==e.indexOf("Windows Phone")||"file:"===location.protocol)&&s.history&&"pushState"in s.history}),e._config.usePrefixes?" -webkit- -moz- -o- -ms- ".split(" "):["",""]),u=(e._prefixes=a,d.documentElement),m="svg"===u.nodeName.toLowerCase();if(!m){var t=void 0!==s?s:this,l=d;function I(e,t){var n=e.createElement("p"),e=e.getElementsByTagName("head")[0]||e.documentElement;return n.innerHTML="x<style>"+t+"</style>",e.insertBefore(n.lastChild,e.firstChild)}function f(){var e=w.elements;return"string"==typeof e?e.split(" "):e}function p(e){var t=X[e[G]];return t||(t={},v++,e[G]=v,X[v]=t),t}function W(e,t,n){return t=t||l,h?t.createElement(e):!(t=(n=n||p(t)).cache[e]?n.cache[e].cloneNode():V.test(e)?(n.cache[e]=n.createElem(e)).cloneNode():n.createElem(e)).canHaveChildren||J.test(e)||t.tagUrn?t:n.frag.appendChild(t)}function i(e){var t,n,r=p(e=e||l);return!w.shivCSS||c||r.hasCSS||(r.hasCSS=!!I(e,"article,aside,dialog,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}mark{background:#FF0;color:#000}template{display:none}")),h||(t=e,(n=r).cache||(n.cache={},n.createElem=t.createElement,n.createFrag=t.createDocumentFragment,n.frag=n.createFrag()),t.createElement=function(e){return w.shivMethods?W(e,t,n):n.createElem(e)},t.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+f().join().replace(/[\w\-:]+/g,function(e){return n.createElem(e),n.frag.createElement(e),'c("'+e+'")'})+");return n}")(w,n.frag)),e}function H(e){for(var t,n=e.getElementsByTagName("*"),r=n.length,o=RegExp("^(?:"+f().join("|")+")$","i"),i=[];r--;)t=n[r],o.test(t.nodeName)&&i.push(t.applyElement(function(e){for(var t,n=e.attributes,r=n.length,o=e.ownerDocument.createElement(y+":"+e.nodeName);r--;)(t=n[r]).specified&&o.setAttribute(t.nodeName,t.nodeValue);return o.style.cssText=e.style.cssText,o}(t)));return i}function B(a){function l(){clearTimeout(n._removeSheetTimer),c&&c.removeNode(!0),c=null}var c,d,n=p(a),e=a.namespaces,t=a.parentWindow;return!K||a.printShived||(void 0===e[y]&&e.add(y),t.attachEvent("onbeforeprint",function(){l();for(var e,t,n,r=a.styleSheets,o=[],i=r.length,s=Array(i);i--;)s[i]=r[i];for(;n=s.pop();)if(!n.disabled&&Z.test(n.media)){try{t=(e=n.imports).length}catch(e){t=0}for(i=0;i<t;i++)s.push(e[i]);try{o.push(n.cssText)}catch(e){}}o=function(e){for(var t,n=e.split("{"),r=n.length,o=RegExp("(^|[\\s,>+~])("+f().join("|")+")(?=[[\\s,>+~#.:]|$)","gi"),i="$1"+y+"\\:$2";r--;)(t=n[r]=n[r].split("}"))[t.length-1]=t[t.length-1].replace(o,i),n[r]=t.join("}");return n.join("{")}(o.reverse().join("")),d=H(a),c=I(a,o)}),t.attachEvent("onafterprint",function(){for(var e=d,t=e.length;t--;)e[t].removeNode();clearTimeout(n._removeSheetTimer),n._removeSheetTimer=setTimeout(l,500)}),a.printShived=!0),a}var c,h,g=t.html5||{},J=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,V=/^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i,G="_html5shiv",v=0,X={};try{var _=l.createElement("a");_.innerHTML="<xyz></xyz>",c="hidden"in _,h=1==_.childNodes.length||(l.createElement("a"),void 0===(O=l.createDocumentFragment()).cloneNode)||void 0===O.createDocumentFragment||void 0===O.createElement}catch(e){h=c=!0}var w={elements:g.elements||"abbr article aside audio bdi canvas data datalist details dialog figcaption figure footer header hgroup main mark meter nav output picture progress section summary template time video",version:"3.7.3",shivCSS:!1!==g.shivCSS,supportsUnknownElements:h,shivMethods:!1!==g.shivMethods,type:"default",shivDocument:i,createElement:W,createDocumentFragment:function(e,t){if(e=e||l,h)return e.createDocumentFragment();for(var n=(t=t||p(e)).frag.cloneNode(),r=0,o=f(),i=o.length;r<i;r++)n.createElement(o[r]);return n},addElements:function(e,t){var n=w.elements;"string"!=typeof n&&(n=n.join(" ")),"string"!=typeof e&&(e=e.join(" ")),w.elements=n+" "+e,i(t)}},Z=(t.html5=w,i(l),/^$|\b(?:all|print)\b/),y="html5shiv",K=!(h||(_=l.documentElement,void 0===l.namespaces)||void 0===l.parentWindow||void 0===_.applyElement||void 0===_.removeNode||void 0===t.attachEvent);w.type+=" print",(w.shivPrint=B)(l),"object"==typeof module&&module.exports&&(module.exports=w)}n.addTest("csspositionsticky",function(){var e="position:",t=T("a").style;return t.cssText=e+a.join("sticky;"+e).slice(0,-e.length),-1!==t.position.indexOf("sticky")});function Q(e){var t,n=a.length,r=s.CSSRule;if(void 0===r)return S;if(e){if((t=(e=e.replace(/^@/,"")).replace(/-/g,"_").toUpperCase()+"_RULE")in r)return"@"+e;for(var o=0;o<n;o++){var i=a[o];if(i.toUpperCase()+"_"+t in r)return"@-"+i.toLowerCase()+"-"+e}}return!1}Y=!("onblur"in d.documentElement);var Y,b,x,M,z,C,N,j,ee,k,A,te=function(e,t){var n;return!!e&&(!(n=(e="on"+e)in(t=t&&"string"!=typeof t?t:T(t||"div")))&&Y&&((t=t.setAttribute?t:T("div")).setAttribute(e,""),n="function"==typeof t[e],t[e]!==S&&(t[e]=S),t.removeAttribute(e)),n)},ne=(e.hasEvent=te,e.testStyles=R),O=(n.addTest("touchevents",function(){var t,e;return"ontouchstart"in s||s.DocumentTouch&&d instanceof DocumentTouch?t=!0:(e=["@media (",a.join("touch-enabled),("),"heartz",")","{#modernizr{top:9px;position:absolute}}"].join(""),ne(e,function(e){t=9===e.offsetTop})),t}),"Moz O ms Webkit"),P=e._config.usePrefixes?O.toLowerCase().split(" "):[],re=(e._domPrefixes=P,n.addTest("pointerevents",function(){for(var e=!1,t=P.length,e=n.hasEvent("pointerdown");t--&&!e;)te(P[t]+"pointerdown")&&(e=!0);return e}),e._config.usePrefixes?O.split(" "):[]),oe=(e._cssomPrefixes=re,e.atRule=Q,{elem:T("modernizr")}),L=(n._q.push(function(){delete oe.elem}),{style:oe.elem.style}),g=(n._q.unshift(function(){delete L.style}),e.testAllProps=r,e.prefixed=function(e,t,n){return 0===e.indexOf("@")?Q(e):(-1!=e.indexOf("-")&&(e=U(e)),t?r(e,t,n):r(e,"pfx"))});for(j in n.addTest("matchmedia",!!g("matchMedia",s)),e.testAllProps=F,n.addTest("flexwrap",F("flexWrap","wrap",!0)),o)if(o.hasOwnProperty(j)){if(b=[],(x=o[j]).name&&(b.push(x.name.toLowerCase()),x.options)&&x.options.aliases&&x.options.aliases.length)for(M=0;M<x.options.aliases.length;M++)b.push(x.options.aliases[M].toLowerCase());for(z=E(x.fn,"function")?x.fn():x.fn,C=0;C<b.length;C++)1===(N=b[C].split(".")).length?n[N[0]]=z:(!n[N[0]]||n[N[0]]instanceof Boolean||(n[N[0]]=new Boolean(n[N[0]])),n[N[0]][N[1]]=z),$.push((z?"":"no-")+N.join("-"))}t=$,k=u.className,A=n._config.classPrefix||"",m&&(k=k.baseVal),n._config.enableJSClass&&(ee=new RegExp("(^|\\s)"+A+"no-js(\\s|$)"),k=k.replace(ee,"$1"+A+"js$2")),n._config.enableClasses&&(k+=" "+A+t.join(" "+A),m?u.className.baseVal=k:u.className=k),delete e.addTest,delete e.addAsyncTest;for(var ie=0;ie<n._q.length;ie++)n._q[ie]();s.Modernizr=n}(window,document),Modernizr.viewport_width=Math.max(document.documentElement.clientWidth,window.innerWidth||0),Modernizr.viewport_height=Math.max(document.documentElement.clientHeight,window.innerHeight||0),Modernizr.narrow=Modernizr.viewport_width<=704,Modernizr.constrained=Modernizr.viewport_width<=1200,Modernizr.site_menu=Modernizr.viewport_width<=1020?"button":"nav_bar",Modernizr.touch=Modernizr.touchevents||Modernizr.pointerevents&&(0<navigator.MaxTouchPoints||0<navigator.msMaxTouchPoints),Modernizr.phone=Modernizr.narrow&&Modernizr.touch,Modernizr.tablet=Modernizr.viewport_width<1075&&Modernizr.touch,Modernizr.desktop=!Modernizr.constrained&&!Modernizr.touch,Modernizr.laptop=!(Modernizr.desktop||Modernizr.tablet||Modernizr.phone),new RegExp("hideallads")),sr_html=(Modernizr.adfree=patt.test(window.location.href),document.querySelector("html")),cn=sr_html.className,sr_host_parts=(Modernizr.phone?sr_html.className=cn.concat(" phone"):Modernizr.tablet?sr_html.className=cn.concat(" tablet"):(Modernizr.desktop||Modernizr.laptop)&&(sr_html.className=cn.concat(" desktop")),window.location.hostname.split(".")),cn=sr_html.className,sr_logger=(Modernizr.is_build=Modernizr.is_live=Modernizr.is_dev=!1,"www"===sr_host_parts[0]||"fbref"===sr_host_parts[0]?(Modernizr.is_live=!0,sr_html.className=cn.concat(" is_live")):sr_host_parts[0].startsWith("b")?(Modernizr.is_build=!0,sr_html.className=cn.concat(" is_build")):(sr_host_parts[0].startsWith("d")||sr_host_parts[0].startsWith("r"))&&(Modernizr.is_dev=!0,sr_html.className=cn.concat(" is_dev")),Modernizr.is_stathead=!1,("stathead"===sr_host_parts[1]&&"srdevel"===sr_host_parts[2]||"stathead"===sr_host_parts[0]||"www"===sr_host_parts[0]&&"stathead"===sr_host_parts[1])&&(cn=sr_html.className,sr_html.className=cn.concat(" is_stathead"),Modernizr.is_stathead=!0),function(){var e=null,t={enableLogger:function(){null!=e&&(window.console.log=e)},disableLogger:function(){e=console.log,window.console.log=function(){}}};return t}()),sr_utilities_js_loader=(!document.srdev&&sr_is_production&&sr_logger.disableLogger(),Modernizr.is_modern=1,Modernizr.lang=document.lang||"",Modernizr.srdev=document.srdev,[]);function vjs_readCookie(e){for(var t=e+"=",n=document.cookie.split(";"),r=0;r<n.length;r++){for(var o=n[r];" "===o.charAt(0);)o=o.substring(1,o.length);if(0===o.indexOf(t))return decodeURIComponent(o.substring(t.length,o.length))}return null}function vjs_createCookie(e,t,n){var r,o="",o=n?((r=new Date).setTime(r.getTime()+24*n*60*60*1e3),"; expires="+r.toGMTString()):"",n=encodeURIComponent(e)+"="+encodeURIComponent(t)+o+"; path=/";document.cookie=n}!function(o){function e(e,t){"use strict";var n=o.document.getElementsByTagName("script")[0],r=o.document.createElement("script");return r.src=e,r.async=!0,n.parentNode.insertBefore(r,n),t&&"function"==typeof t&&(r.onload=t),r}"undefined"!=typeof module?module.exports=e:o.loadJS=e}("undefined"!=typeof global?global:this),String.prototype.vjs_isMatch=function(e){return null!==this.match(e)};var sr_time_begin=new Date,sr_perf_startTime=new Date,sr_perf_log="<strong>Performance:</strong>",sr_perf_lastTime=new Date;function vjs_ready(e){"loading"!=document.readyState?e():document.addEventListener("DOMContentLoaded",e)}
</script>
<script>
let server = (document.srdev) ? 'https://cdn.ssref.net/nocdn/dev/' + document.srdev.substring(0, 2) : "https://cdn.ssref.net/req/202311303";
let _sr_modern_url = server 
	+ "/js/pfr" 
	+ "/sr"+ ((document.srdev) ? "" : "-min")   	+ ".js"
;
loadJS( _sr_modern_url, function() { vjs_ready(sr_fire_js); });
</script>
<!-- JS END -->


<!-- include:end  ="/inc/klecko_header_full_pfr.html_f" -->



    <meta name="revised" content="08:53:36 22-Dec-2023" />
    <meta name="HandheldFriendly" content="True" />
    <meta name="HandheldFriendly" content="True" />
    <meta name="generated-by"     content="build_year_pages.pl" />
    <meta name="sr-web-model"     content="SRlocal::Models::Web::CompetitionSeasons::Schedule" />
    <meta name="format-detection" content="telephone=no" />
    <meta name="apple-mobile-web-app-capable" content="no" />
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="theme-color" content="#384d42" />
    <meta name="msapplication-navbutton-color" content="#384d42" />
    <meta name="apple-mobile-web-app-status-bar-style" content="#384d42" />




<!-- HeaderSportsEventSchema -->
<script type="application/ld+json">
[

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			},
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			}
		],
		"description": "Kansas City Chiefs vs Detroit Lions on September 7, 2023",
		"endDate": "",
		"name": "Detroit Lions @ Kansas City Chiefs",
			"sport": "Football",
		"startDate": "September 7, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309070kan.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "GEHA Field at Arrowhead Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			},
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			}
		],
		"description": "Atlanta Falcons vs Carolina Panthers on September 10, 2023",
		"endDate": "",
		"name": "Carolina Panthers @ Atlanta Falcons",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100atl.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Mercedes-Benz Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			},
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			}
		],
		"description": "Cleveland Browns vs Cincinnati Bengals on September 10, 2023",
		"endDate": "",
		"name": "Cincinnati Bengals @ Cleveland Browns",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100cle.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Cleveland Browns Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			},
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			}
		],
		"description": "Indianapolis Colts vs Jacksonville Jaguars on September 10, 2023",
		"endDate": "",
		"name": "Jacksonville Jaguars @ Indianapolis Colts",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100clt.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lucas Oil Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			},
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			}
		],
		"description": "Washington Commanders vs Arizona Cardinals on September 10, 2023",
		"endDate": "",
		"name": "Arizona Cardinals @ Washington Commanders",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100was.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "FedExField"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			},
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			}
		],
		"description": "Baltimore Ravens vs Houston Texans on September 10, 2023",
		"endDate": "",
		"name": "Houston Texans @ Baltimore Ravens",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100rav.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "M&T Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			},
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			}
		],
		"description": "Minnesota Vikings vs Tampa Bay Buccaneers on September 10, 2023",
		"endDate": "",
		"name": "Tampa Bay Buccaneers @ Minnesota Vikings",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100min.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "U.S. Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			},
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			}
		],
		"description": "New Orleans Saints vs Tennessee Titans on September 10, 2023",
		"endDate": "",
		"name": "Tennessee Titans @ New Orleans Saints",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100nor.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Caesars Superdome"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			},
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			}
		],
		"description": "Pittsburgh Steelers vs San Francisco 49ers on September 10, 2023",
		"endDate": "",
		"name": "San Francisco 49ers @ Pittsburgh Steelers",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100pit.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Acrisure Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			},
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			}
		],
		"description": "Chicago Bears vs Green Bay Packers on September 10, 2023",
		"endDate": "",
		"name": "Green Bay Packers @ Chicago Bears",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100chi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Soldier Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			},
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			}
		],
		"description": "Denver Broncos vs Las Vegas Raiders on September 10, 2023",
		"endDate": "",
		"name": "Las Vegas Raiders @ Denver Broncos",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100den.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Empower Field at Mile High"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			}
		],
		"description": "Los Angeles Chargers vs Miami Dolphins on September 10, 2023",
		"endDate": "",
		"name": "Miami Dolphins @ Los Angeles Chargers",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100sdg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			},
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			}
		],
		"description": "New England Patriots vs Philadelphia Eagles on September 10, 2023",
		"endDate": "",
		"name": "Philadelphia Eagles @ New England Patriots",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100nwe.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Gillette Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			},
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			}
		],
		"description": "Seattle Seahawks vs Los Angeles Rams on September 10, 2023",
		"endDate": "",
		"name": "Los Angeles Rams @ Seattle Seahawks",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100sea.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lumen Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			}
		],
		"description": "New York Giants vs Dallas Cowboys on September 10, 2023",
		"endDate": "",
		"name": "Dallas Cowboys @ New York Giants",
			"sport": "Football",
		"startDate": "September 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309100nyg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			}
		],
		"description": "New York Jets vs Buffalo Bills on September 11, 2023",
		"endDate": "",
		"name": "Buffalo Bills @ New York Jets",
			"sport": "Football",
		"startDate": "September 11, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309110nyj.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			},
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			}
		],
		"description": "Philadelphia Eagles vs Minnesota Vikings on September 14, 2023",
		"endDate": "",
		"name": "Minnesota Vikings @ Philadelphia Eagles",
			"sport": "Football",
		"startDate": "September 14, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309140phi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lincoln Financial Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			},
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			}
		],
		"description": "Atlanta Falcons vs Green Bay Packers on September 17, 2023",
		"endDate": "",
		"name": "Green Bay Packers @ Atlanta Falcons",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170atl.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Mercedes-Benz Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			},
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			}
		],
		"description": "Buffalo Bills vs Las Vegas Raiders on September 17, 2023",
		"endDate": "",
		"name": "Las Vegas Raiders @ Buffalo Bills",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170buf.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Highmark Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			},
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			}
		],
		"description": "Tampa Bay Buccaneers vs Chicago Bears on September 17, 2023",
		"endDate": "",
		"name": "Chicago Bears @ Tampa Bay Buccaneers",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170tam.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Raymond James Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			},
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			}
		],
		"description": "Cincinnati Bengals vs Baltimore Ravens on September 17, 2023",
		"endDate": "",
		"name": "Baltimore Ravens @ Cincinnati Bengals",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170cin.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Paycor Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			},
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			}
		],
		"description": "Houston Texans vs Indianapolis Colts on September 17, 2023",
		"endDate": "",
		"name": "Indianapolis Colts @ Houston Texans",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170htx.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "NRG Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			},
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			}
		],
		"description": "Detroit Lions vs Seattle Seahawks on September 17, 2023",
		"endDate": "",
		"name": "Seattle Seahawks @ Detroit Lions",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170det.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Ford Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			},
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			}
		],
		"description": "Jacksonville Jaguars vs Kansas City Chiefs on September 17, 2023",
		"endDate": "",
		"name": "Kansas City Chiefs @ Jacksonville Jaguars",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170jax.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "EverBank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			},
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			}
		],
		"description": "Tennessee Titans vs Los Angeles Chargers on September 17, 2023",
		"endDate": "",
		"name": "Los Angeles Chargers @ Tennessee Titans",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170oti.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Nissan Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			},
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			}
		],
		"description": "Arizona Cardinals vs New York Giants on September 17, 2023",
		"endDate": "",
		"name": "New York Giants @ Arizona Cardinals",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170crd.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "State Farm Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			}
		],
		"description": "Los Angeles Rams vs San Francisco 49ers on September 17, 2023",
		"endDate": "",
		"name": "San Francisco 49ers @ Los Angeles Rams",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170ram.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			},
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			}
		],
		"description": "Dallas Cowboys vs New York Jets on September 17, 2023",
		"endDate": "",
		"name": "New York Jets @ Dallas Cowboys",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170dal.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "AT&T Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			},
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			}
		],
		"description": "Denver Broncos vs Washington Commanders on September 17, 2023",
		"endDate": "",
		"name": "Washington Commanders @ Denver Broncos",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170den.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Empower Field at Mile High"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			},
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			}
		],
		"description": "New England Patriots vs Miami Dolphins on September 17, 2023",
		"endDate": "",
		"name": "Miami Dolphins @ New England Patriots",
			"sport": "Football",
		"startDate": "September 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309170nwe.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Gillette Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			},
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			}
		],
		"description": "Carolina Panthers vs New Orleans Saints on September 18, 2023",
		"endDate": "",
		"name": "New Orleans Saints @ Carolina Panthers",
			"sport": "Football",
		"startDate": "September 18, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309180car.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Bank of America Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			},
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			}
		],
		"description": "Pittsburgh Steelers vs Cleveland Browns on September 18, 2023",
		"endDate": "",
		"name": "Cleveland Browns @ Pittsburgh Steelers",
			"sport": "Football",
		"startDate": "September 18, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309180pit.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Acrisure Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			},
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			}
		],
		"description": "San Francisco 49ers vs New York Giants on September 21, 2023",
		"endDate": "",
		"name": "New York Giants @ San Francisco 49ers",
			"sport": "Football",
		"startDate": "September 21, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309210sfo.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Levi's Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			},
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			}
		],
		"description": "Detroit Lions vs Atlanta Falcons on September 24, 2023",
		"endDate": "",
		"name": "Atlanta Falcons @ Detroit Lions",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240det.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Ford Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			},
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			}
		],
		"description": "Washington Commanders vs Buffalo Bills on September 24, 2023",
		"endDate": "",
		"name": "Buffalo Bills @ Washington Commanders",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240was.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "FedExField"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			},
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			}
		],
		"description": "Cleveland Browns vs Tennessee Titans on September 24, 2023",
		"endDate": "",
		"name": "Tennessee Titans @ Cleveland Browns",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240cle.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Cleveland Browns Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			},
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			}
		],
		"description": "Baltimore Ravens vs Indianapolis Colts on September 24, 2023",
		"endDate": "",
		"name": "Indianapolis Colts @ Baltimore Ravens",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240rav.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "M&T Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			},
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			}
		],
		"description": "Miami Dolphins vs Denver Broncos on September 24, 2023",
		"endDate": "",
		"name": "Denver Broncos @ Miami Dolphins",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240mia.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Hard Rock Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			},
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			}
		],
		"description": "Green Bay Packers vs New Orleans Saints on September 24, 2023",
		"endDate": "",
		"name": "New Orleans Saints @ Green Bay Packers",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240gnb.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lambeau Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			},
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			}
		],
		"description": "Jacksonville Jaguars vs Houston Texans on September 24, 2023",
		"endDate": "",
		"name": "Houston Texans @ Jacksonville Jaguars",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240jax.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "EverBank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			},
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			}
		],
		"description": "Minnesota Vikings vs Los Angeles Chargers on September 24, 2023",
		"endDate": "",
		"name": "Los Angeles Chargers @ Minnesota Vikings",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240min.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "U.S. Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			}
		],
		"description": "New York Jets vs New England Patriots on September 24, 2023",
		"endDate": "",
		"name": "New England Patriots @ New York Jets",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240nyj.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			},
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			}
		],
		"description": "Seattle Seahawks vs Carolina Panthers on September 24, 2023",
		"endDate": "",
		"name": "Carolina Panthers @ Seattle Seahawks",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240sea.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lumen Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			},
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			}
		],
		"description": "Kansas City Chiefs vs Chicago Bears on September 24, 2023",
		"endDate": "",
		"name": "Chicago Bears @ Kansas City Chiefs",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240kan.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "GEHA Field at Arrowhead Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			},
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			}
		],
		"description": "Arizona Cardinals vs Dallas Cowboys on September 24, 2023",
		"endDate": "",
		"name": "Dallas Cowboys @ Arizona Cardinals",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240crd.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "State Farm Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			},
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			}
		],
		"description": "Las Vegas Raiders vs Pittsburgh Steelers on September 24, 2023",
		"endDate": "",
		"name": "Pittsburgh Steelers @ Las Vegas Raiders",
			"sport": "Football",
		"startDate": "September 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309240rai.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Allegiant Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			},
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			}
		],
		"description": "Tampa Bay Buccaneers vs Philadelphia Eagles on September 25, 2023",
		"endDate": "",
		"name": "Philadelphia Eagles @ Tampa Bay Buccaneers",
			"sport": "Football",
		"startDate": "September 25, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309250tam.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Raymond James Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			},
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			}
		],
		"description": "Cincinnati Bengals vs Los Angeles Rams on September 25, 2023",
		"endDate": "",
		"name": "Los Angeles Rams @ Cincinnati Bengals",
			"sport": "Football",
		"startDate": "September 25, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309250cin.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Paycor Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			},
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			}
		],
		"description": "Green Bay Packers vs Detroit Lions on September 28, 2023",
		"endDate": "",
		"name": "Detroit Lions @ Green Bay Packers",
			"sport": "Football",
		"startDate": "September 28, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202309280gnb.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lambeau Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			},
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			}
		],
		"description": "Jacksonville Jaguars vs Atlanta Falcons on October 1, 2023",
		"endDate": "",
		"name": "Atlanta Falcons @ Jacksonville Jaguars",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010jax.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Wembley Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			},
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			}
		],
		"description": "Buffalo Bills vs Miami Dolphins on October 1, 2023",
		"endDate": "",
		"name": "Miami Dolphins @ Buffalo Bills",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010buf.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Highmark Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			},
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			}
		],
		"description": "Carolina Panthers vs Minnesota Vikings on October 1, 2023",
		"endDate": "",
		"name": "Minnesota Vikings @ Carolina Panthers",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010car.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Bank of America Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			},
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			}
		],
		"description": "Chicago Bears vs Denver Broncos on October 1, 2023",
		"endDate": "",
		"name": "Denver Broncos @ Chicago Bears",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010chi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Soldier Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			},
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			}
		],
		"description": "Tennessee Titans vs Cincinnati Bengals on October 1, 2023",
		"endDate": "",
		"name": "Cincinnati Bengals @ Tennessee Titans",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010oti.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Nissan Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			},
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			}
		],
		"description": "Cleveland Browns vs Baltimore Ravens on October 1, 2023",
		"endDate": "",
		"name": "Baltimore Ravens @ Cleveland Browns",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010cle.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Cleveland Browns Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			},
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			}
		],
		"description": "Indianapolis Colts vs Los Angeles Rams on October 1, 2023",
		"endDate": "",
		"name": "Los Angeles Rams @ Indianapolis Colts",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010clt.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lucas Oil Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			},
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			}
		],
		"description": "Houston Texans vs Pittsburgh Steelers on October 1, 2023",
		"endDate": "",
		"name": "Pittsburgh Steelers @ Houston Texans",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010htx.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "NRG Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			},
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			}
		],
		"description": "New Orleans Saints vs Tampa Bay Buccaneers on October 1, 2023",
		"endDate": "",
		"name": "Tampa Bay Buccaneers @ New Orleans Saints",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010nor.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Caesars Superdome"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			},
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			}
		],
		"description": "Philadelphia Eagles vs Washington Commanders on October 1, 2023",
		"endDate": "",
		"name": "Washington Commanders @ Philadelphia Eagles",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010phi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lincoln Financial Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			}
		],
		"description": "Los Angeles Chargers vs Las Vegas Raiders on October 1, 2023",
		"endDate": "",
		"name": "Las Vegas Raiders @ Los Angeles Chargers",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010sdg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			},
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			}
		],
		"description": "San Francisco 49ers vs Arizona Cardinals on October 1, 2023",
		"endDate": "",
		"name": "Arizona Cardinals @ San Francisco 49ers",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010sfo.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Levi's Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			},
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			}
		],
		"description": "Dallas Cowboys vs New England Patriots on October 1, 2023",
		"endDate": "",
		"name": "New England Patriots @ Dallas Cowboys",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010dal.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "AT&T Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			}
		],
		"description": "New York Jets vs Kansas City Chiefs on October 1, 2023",
		"endDate": "",
		"name": "Kansas City Chiefs @ New York Jets",
			"sport": "Football",
		"startDate": "October 1, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310010nyj.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			}
		],
		"description": "New York Giants vs Seattle Seahawks on October 2, 2023",
		"endDate": "",
		"name": "Seattle Seahawks @ New York Giants",
			"sport": "Football",
		"startDate": "October 2, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310020nyg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			},
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			}
		],
		"description": "Washington Commanders vs Chicago Bears on October 5, 2023",
		"endDate": "",
		"name": "Chicago Bears @ Washington Commanders",
			"sport": "Football",
		"startDate": "October 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310050was.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "FedExField"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			},
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			}
		],
		"description": "Buffalo Bills vs Jacksonville Jaguars on October 8, 2023",
		"endDate": "",
		"name": "Jacksonville Jaguars @ Buffalo Bills",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080buf.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Tottenham Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			},
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			}
		],
		"description": "Atlanta Falcons vs Houston Texans on October 8, 2023",
		"endDate": "",
		"name": "Houston Texans @ Atlanta Falcons",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080atl.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Mercedes-Benz Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			},
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			}
		],
		"description": "Detroit Lions vs Carolina Panthers on October 8, 2023",
		"endDate": "",
		"name": "Carolina Panthers @ Detroit Lions",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080det.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Ford Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			},
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			}
		],
		"description": "Indianapolis Colts vs Tennessee Titans on October 8, 2023",
		"endDate": "",
		"name": "Tennessee Titans @ Indianapolis Colts",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080clt.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lucas Oil Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			},
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			}
		],
		"description": "Miami Dolphins vs New York Giants on October 8, 2023",
		"endDate": "",
		"name": "New York Giants @ Miami Dolphins",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080mia.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Hard Rock Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			},
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			}
		],
		"description": "New England Patriots vs New Orleans Saints on October 8, 2023",
		"endDate": "",
		"name": "New Orleans Saints @ New England Patriots",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080nwe.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Gillette Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			},
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			}
		],
		"description": "Pittsburgh Steelers vs Baltimore Ravens on October 8, 2023",
		"endDate": "",
		"name": "Baltimore Ravens @ Pittsburgh Steelers",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080pit.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Acrisure Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			},
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			}
		],
		"description": "Arizona Cardinals vs Cincinnati Bengals on October 8, 2023",
		"endDate": "",
		"name": "Cincinnati Bengals @ Arizona Cardinals",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080crd.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "State Farm Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			}
		],
		"description": "Los Angeles Rams vs Philadelphia Eagles on October 8, 2023",
		"endDate": "",
		"name": "Philadelphia Eagles @ Los Angeles Rams",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080ram.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			},
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			}
		],
		"description": "Denver Broncos vs New York Jets on October 8, 2023",
		"endDate": "",
		"name": "New York Jets @ Denver Broncos",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080den.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Empower Field at Mile High"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			},
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			}
		],
		"description": "Minnesota Vikings vs Kansas City Chiefs on October 8, 2023",
		"endDate": "",
		"name": "Kansas City Chiefs @ Minnesota Vikings",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080min.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "U.S. Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			},
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			}
		],
		"description": "San Francisco 49ers vs Dallas Cowboys on October 8, 2023",
		"endDate": "",
		"name": "Dallas Cowboys @ San Francisco 49ers",
			"sport": "Football",
		"startDate": "October 8, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310080sfo.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Levi's Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			},
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			}
		],
		"description": "Las Vegas Raiders vs Green Bay Packers on October 9, 2023",
		"endDate": "",
		"name": "Green Bay Packers @ Las Vegas Raiders",
			"sport": "Football",
		"startDate": "October 9, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310090rai.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Allegiant Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			},
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			}
		],
		"description": "Kansas City Chiefs vs Denver Broncos on October 12, 2023",
		"endDate": "",
		"name": "Denver Broncos @ Kansas City Chiefs",
			"sport": "Football",
		"startDate": "October 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310120kan.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "GEHA Field at Arrowhead Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			},
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			}
		],
		"description": "Tennessee Titans vs Baltimore Ravens on October 15, 2023",
		"endDate": "",
		"name": "Baltimore Ravens @ Tennessee Titans",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150oti.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Tottenham Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			},
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			}
		],
		"description": "Cleveland Browns vs San Francisco 49ers on October 15, 2023",
		"endDate": "",
		"name": "San Francisco 49ers @ Cleveland Browns",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150cle.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Cleveland Browns Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			},
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			}
		],
		"description": "Atlanta Falcons vs Washington Commanders on October 15, 2023",
		"endDate": "",
		"name": "Washington Commanders @ Atlanta Falcons",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150atl.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Mercedes-Benz Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			},
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			}
		],
		"description": "Miami Dolphins vs Carolina Panthers on October 15, 2023",
		"endDate": "",
		"name": "Carolina Panthers @ Miami Dolphins",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150mia.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Hard Rock Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			},
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			}
		],
		"description": "Chicago Bears vs Minnesota Vikings on October 15, 2023",
		"endDate": "",
		"name": "Minnesota Vikings @ Chicago Bears",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150chi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Soldier Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			},
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			}
		],
		"description": "Cincinnati Bengals vs Seattle Seahawks on October 15, 2023",
		"endDate": "",
		"name": "Seattle Seahawks @ Cincinnati Bengals",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150cin.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Paycor Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			},
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			}
		],
		"description": "Jacksonville Jaguars vs Indianapolis Colts on October 15, 2023",
		"endDate": "",
		"name": "Indianapolis Colts @ Jacksonville Jaguars",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150jax.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "EverBank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			},
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			}
		],
		"description": "Houston Texans vs New Orleans Saints on October 15, 2023",
		"endDate": "",
		"name": "New Orleans Saints @ Houston Texans",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150htx.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "NRG Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			},
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			}
		],
		"description": "Las Vegas Raiders vs New England Patriots on October 15, 2023",
		"endDate": "",
		"name": "New England Patriots @ Las Vegas Raiders",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150rai.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Allegiant Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			}
		],
		"description": "Los Angeles Rams vs Arizona Cardinals on October 15, 2023",
		"endDate": "",
		"name": "Arizona Cardinals @ Los Angeles Rams",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150ram.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			},
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			}
		],
		"description": "Tampa Bay Buccaneers vs Detroit Lions on October 15, 2023",
		"endDate": "",
		"name": "Detroit Lions @ Tampa Bay Buccaneers",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150tam.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Raymond James Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			}
		],
		"description": "New York Jets vs Philadelphia Eagles on October 15, 2023",
		"endDate": "",
		"name": "Philadelphia Eagles @ New York Jets",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150nyj.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			},
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			}
		],
		"description": "Buffalo Bills vs New York Giants on October 15, 2023",
		"endDate": "",
		"name": "New York Giants @ Buffalo Bills",
			"sport": "Football",
		"startDate": "October 15, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310150buf.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Highmark Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			}
		],
		"description": "Los Angeles Chargers vs Dallas Cowboys on October 16, 2023",
		"endDate": "",
		"name": "Dallas Cowboys @ Los Angeles Chargers",
			"sport": "Football",
		"startDate": "October 16, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310160sdg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			},
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			}
		],
		"description": "New Orleans Saints vs Jacksonville Jaguars on October 19, 2023",
		"endDate": "",
		"name": "Jacksonville Jaguars @ New Orleans Saints",
			"sport": "Football",
		"startDate": "October 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310190nor.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Caesars Superdome"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			},
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			}
		],
		"description": "Indianapolis Colts vs Cleveland Browns on October 22, 2023",
		"endDate": "",
		"name": "Cleveland Browns @ Indianapolis Colts",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220clt.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lucas Oil Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			},
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			}
		],
		"description": "Tampa Bay Buccaneers vs Atlanta Falcons on October 22, 2023",
		"endDate": "",
		"name": "Atlanta Falcons @ Tampa Bay Buccaneers",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220tam.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Raymond James Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			},
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			}
		],
		"description": "New England Patriots vs Buffalo Bills on October 22, 2023",
		"endDate": "",
		"name": "Buffalo Bills @ New England Patriots",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220nwe.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Gillette Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			},
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			}
		],
		"description": "Chicago Bears vs Las Vegas Raiders on October 22, 2023",
		"endDate": "",
		"name": "Las Vegas Raiders @ Chicago Bears",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220chi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Soldier Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			},
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			}
		],
		"description": "Baltimore Ravens vs Detroit Lions on October 22, 2023",
		"endDate": "",
		"name": "Detroit Lions @ Baltimore Ravens",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220rav.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "M&T Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			}
		],
		"description": "New York Giants vs Washington Commanders on October 22, 2023",
		"endDate": "",
		"name": "Washington Commanders @ New York Giants",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220nyg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			}
		],
		"description": "Los Angeles Rams vs Pittsburgh Steelers on October 22, 2023",
		"endDate": "",
		"name": "Pittsburgh Steelers @ Los Angeles Rams",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220ram.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			},
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			}
		],
		"description": "Seattle Seahawks vs Arizona Cardinals on October 22, 2023",
		"endDate": "",
		"name": "Arizona Cardinals @ Seattle Seahawks",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220sea.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lumen Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			},
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			}
		],
		"description": "Denver Broncos vs Green Bay Packers on October 22, 2023",
		"endDate": "",
		"name": "Green Bay Packers @ Denver Broncos",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220den.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Empower Field at Mile High"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			},
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			}
		],
		"description": "Kansas City Chiefs vs Los Angeles Chargers on October 22, 2023",
		"endDate": "",
		"name": "Los Angeles Chargers @ Kansas City Chiefs",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220kan.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "GEHA Field at Arrowhead Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			},
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			}
		],
		"description": "Philadelphia Eagles vs Miami Dolphins on October 22, 2023",
		"endDate": "",
		"name": "Miami Dolphins @ Philadelphia Eagles",
			"sport": "Football",
		"startDate": "October 22, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310220phi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lincoln Financial Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			},
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			}
		],
		"description": "Minnesota Vikings vs San Francisco 49ers on October 23, 2023",
		"endDate": "",
		"name": "San Francisco 49ers @ Minnesota Vikings",
			"sport": "Football",
		"startDate": "October 23, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310230min.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "U.S. Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			},
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			}
		],
		"description": "Buffalo Bills vs Tampa Bay Buccaneers on October 26, 2023",
		"endDate": "",
		"name": "Tampa Bay Buccaneers @ Buffalo Bills",
			"sport": "Football",
		"startDate": "October 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310260buf.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Highmark Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			},
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			}
		],
		"description": "Carolina Panthers vs Houston Texans on October 29, 2023",
		"endDate": "",
		"name": "Houston Texans @ Carolina Panthers",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290car.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Bank of America Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			},
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			}
		],
		"description": "Dallas Cowboys vs Los Angeles Rams on October 29, 2023",
		"endDate": "",
		"name": "Los Angeles Rams @ Dallas Cowboys",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290dal.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "AT&T Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			},
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			}
		],
		"description": "Green Bay Packers vs Minnesota Vikings on October 29, 2023",
		"endDate": "",
		"name": "Minnesota Vikings @ Green Bay Packers",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290gnb.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lambeau Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			},
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			}
		],
		"description": "Tennessee Titans vs Atlanta Falcons on October 29, 2023",
		"endDate": "",
		"name": "Atlanta Falcons @ Tennessee Titans",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290oti.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Nissan Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			},
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			}
		],
		"description": "Indianapolis Colts vs New Orleans Saints on October 29, 2023",
		"endDate": "",
		"name": "New Orleans Saints @ Indianapolis Colts",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290clt.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lucas Oil Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			},
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			}
		],
		"description": "Pittsburgh Steelers vs Jacksonville Jaguars on October 29, 2023",
		"endDate": "",
		"name": "Jacksonville Jaguars @ Pittsburgh Steelers",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290pit.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Acrisure Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			},
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			}
		],
		"description": "Miami Dolphins vs New England Patriots on October 29, 2023",
		"endDate": "",
		"name": "New England Patriots @ Miami Dolphins",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290mia.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Hard Rock Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			}
		],
		"description": "New York Giants vs New York Jets on October 29, 2023",
		"endDate": "",
		"name": "New York Jets @ New York Giants",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290nyg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			},
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			}
		],
		"description": "Washington Commanders vs Philadelphia Eagles on October 29, 2023",
		"endDate": "",
		"name": "Philadelphia Eagles @ Washington Commanders",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290was.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "FedExField"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			},
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			}
		],
		"description": "Seattle Seahawks vs Cleveland Browns on October 29, 2023",
		"endDate": "",
		"name": "Cleveland Browns @ Seattle Seahawks",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290sea.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lumen Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			},
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			}
		],
		"description": "San Francisco 49ers vs Cincinnati Bengals on October 29, 2023",
		"endDate": "",
		"name": "Cincinnati Bengals @ San Francisco 49ers",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290sfo.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Levi's Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			},
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			}
		],
		"description": "Arizona Cardinals vs Baltimore Ravens on October 29, 2023",
		"endDate": "",
		"name": "Baltimore Ravens @ Arizona Cardinals",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290crd.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "State Farm Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			},
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			}
		],
		"description": "Denver Broncos vs Kansas City Chiefs on October 29, 2023",
		"endDate": "",
		"name": "Kansas City Chiefs @ Denver Broncos",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290den.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Empower Field at Mile High"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			}
		],
		"description": "Los Angeles Chargers vs Chicago Bears on October 29, 2023",
		"endDate": "",
		"name": "Chicago Bears @ Los Angeles Chargers",
			"sport": "Football",
		"startDate": "October 29, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310290sdg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			},
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			}
		],
		"description": "Detroit Lions vs Las Vegas Raiders on October 30, 2023",
		"endDate": "",
		"name": "Las Vegas Raiders @ Detroit Lions",
			"sport": "Football",
		"startDate": "October 30, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202310300det.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Ford Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			},
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			}
		],
		"description": "Pittsburgh Steelers vs Tennessee Titans on November 2, 2023",
		"endDate": "",
		"name": "Tennessee Titans @ Pittsburgh Steelers",
			"sport": "Football",
		"startDate": "November 2, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311020pit.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Acrisure Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			},
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			}
		],
		"description": "Kansas City Chiefs vs Miami Dolphins on November 5, 2023",
		"endDate": "",
		"name": "Miami Dolphins @ Kansas City Chiefs",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050kan.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Deutsche Bank Park"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			},
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			}
		],
		"description": "Cleveland Browns vs Arizona Cardinals on November 5, 2023",
		"endDate": "",
		"name": "Arizona Cardinals @ Cleveland Browns",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050cle.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Cleveland Browns Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			},
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			}
		],
		"description": "Green Bay Packers vs Los Angeles Rams on November 5, 2023",
		"endDate": "",
		"name": "Los Angeles Rams @ Green Bay Packers",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050gnb.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lambeau Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			},
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			}
		],
		"description": "Houston Texans vs Tampa Bay Buccaneers on November 5, 2023",
		"endDate": "",
		"name": "Tampa Bay Buccaneers @ Houston Texans",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050htx.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "NRG Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			},
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			}
		],
		"description": "Atlanta Falcons vs Minnesota Vikings on November 5, 2023",
		"endDate": "",
		"name": "Minnesota Vikings @ Atlanta Falcons",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050atl.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Mercedes-Benz Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			},
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			}
		],
		"description": "New Orleans Saints vs Chicago Bears on November 5, 2023",
		"endDate": "",
		"name": "Chicago Bears @ New Orleans Saints",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050nor.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Caesars Superdome"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			},
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			}
		],
		"description": "New England Patriots vs Washington Commanders on November 5, 2023",
		"endDate": "",
		"name": "Washington Commanders @ New England Patriots",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050nwe.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Gillette Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			},
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			}
		],
		"description": "Baltimore Ravens vs Seattle Seahawks on November 5, 2023",
		"endDate": "",
		"name": "Seattle Seahawks @ Baltimore Ravens",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050rav.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "M&T Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			},
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			}
		],
		"description": "Carolina Panthers vs Indianapolis Colts on November 5, 2023",
		"endDate": "",
		"name": "Indianapolis Colts @ Carolina Panthers",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050car.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Bank of America Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			},
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			}
		],
		"description": "Philadelphia Eagles vs Dallas Cowboys on November 5, 2023",
		"endDate": "",
		"name": "Dallas Cowboys @ Philadelphia Eagles",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050phi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lincoln Financial Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			},
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			}
		],
		"description": "Las Vegas Raiders vs New York Giants on November 5, 2023",
		"endDate": "",
		"name": "New York Giants @ Las Vegas Raiders",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050rai.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Allegiant Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			},
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			}
		],
		"description": "Cincinnati Bengals vs Buffalo Bills on November 5, 2023",
		"endDate": "",
		"name": "Buffalo Bills @ Cincinnati Bengals",
			"sport": "Football",
		"startDate": "November 5, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311050cin.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Paycor Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			}
		],
		"description": "New York Jets vs Los Angeles Chargers on November 6, 2023",
		"endDate": "",
		"name": "Los Angeles Chargers @ New York Jets",
			"sport": "Football",
		"startDate": "November 6, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311060nyj.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			},
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			}
		],
		"description": "Chicago Bears vs Carolina Panthers on November 9, 2023",
		"endDate": "",
		"name": "Carolina Panthers @ Chicago Bears",
			"sport": "Football",
		"startDate": "November 9, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311090chi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Soldier Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			},
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			}
		],
		"description": "New England Patriots vs Indianapolis Colts on November 12, 2023",
		"endDate": "",
		"name": "Indianapolis Colts @ New England Patriots",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120nwe.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Deutsche Bank Park"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			},
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			}
		],
		"description": "Cincinnati Bengals vs Houston Texans on November 12, 2023",
		"endDate": "",
		"name": "Houston Texans @ Cincinnati Bengals",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120cin.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Paycor Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			},
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			}
		],
		"description": "Baltimore Ravens vs Cleveland Browns on November 12, 2023",
		"endDate": "",
		"name": "Cleveland Browns @ Baltimore Ravens",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120rav.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "M&T Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			},
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			}
		],
		"description": "Pittsburgh Steelers vs Green Bay Packers on November 12, 2023",
		"endDate": "",
		"name": "Green Bay Packers @ Pittsburgh Steelers",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120pit.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Acrisure Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			},
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			}
		],
		"description": "Jacksonville Jaguars vs San Francisco 49ers on November 12, 2023",
		"endDate": "",
		"name": "San Francisco 49ers @ Jacksonville Jaguars",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120jax.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "EverBank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			},
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			}
		],
		"description": "Tampa Bay Buccaneers vs Tennessee Titans on November 12, 2023",
		"endDate": "",
		"name": "Tennessee Titans @ Tampa Bay Buccaneers",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120tam.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Raymond James Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			},
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			}
		],
		"description": "Minnesota Vikings vs New Orleans Saints on November 12, 2023",
		"endDate": "",
		"name": "New Orleans Saints @ Minnesota Vikings",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120min.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "U.S. Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			}
		],
		"description": "Los Angeles Chargers vs Detroit Lions on November 12, 2023",
		"endDate": "",
		"name": "Detroit Lions @ Los Angeles Chargers",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120sdg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			},
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			}
		],
		"description": "Arizona Cardinals vs Atlanta Falcons on November 12, 2023",
		"endDate": "",
		"name": "Atlanta Falcons @ Arizona Cardinals",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120crd.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "State Farm Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			},
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			}
		],
		"description": "Dallas Cowboys vs New York Giants on November 12, 2023",
		"endDate": "",
		"name": "New York Giants @ Dallas Cowboys",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120dal.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "AT&T Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			},
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			}
		],
		"description": "Seattle Seahawks vs Washington Commanders on November 12, 2023",
		"endDate": "",
		"name": "Washington Commanders @ Seattle Seahawks",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120sea.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lumen Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			},
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			}
		],
		"description": "Las Vegas Raiders vs New York Jets on November 12, 2023",
		"endDate": "",
		"name": "New York Jets @ Las Vegas Raiders",
			"sport": "Football",
		"startDate": "November 12, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311120rai.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Allegiant Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			},
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			}
		],
		"description": "Buffalo Bills vs Denver Broncos on November 13, 2023",
		"endDate": "",
		"name": "Denver Broncos @ Buffalo Bills",
			"sport": "Football",
		"startDate": "November 13, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311130buf.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Highmark Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			},
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			}
		],
		"description": "Baltimore Ravens vs Cincinnati Bengals on November 16, 2023",
		"endDate": "",
		"name": "Cincinnati Bengals @ Baltimore Ravens",
			"sport": "Football",
		"startDate": "November 16, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311160rav.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "M&T Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			},
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			}
		],
		"description": "Carolina Panthers vs Dallas Cowboys on November 19, 2023",
		"endDate": "",
		"name": "Dallas Cowboys @ Carolina Panthers",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190car.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Bank of America Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			},
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			}
		],
		"description": "Cleveland Browns vs Pittsburgh Steelers on November 19, 2023",
		"endDate": "",
		"name": "Pittsburgh Steelers @ Cleveland Browns",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190cle.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Cleveland Browns Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			},
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			}
		],
		"description": "Green Bay Packers vs Los Angeles Chargers on November 19, 2023",
		"endDate": "",
		"name": "Los Angeles Chargers @ Green Bay Packers",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190gnb.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lambeau Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			},
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			}
		],
		"description": "Jacksonville Jaguars vs Tennessee Titans on November 19, 2023",
		"endDate": "",
		"name": "Tennessee Titans @ Jacksonville Jaguars",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190jax.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "EverBank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			},
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			}
		],
		"description": "Miami Dolphins vs Las Vegas Raiders on November 19, 2023",
		"endDate": "",
		"name": "Las Vegas Raiders @ Miami Dolphins",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190mia.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Hard Rock Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			},
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			}
		],
		"description": "Detroit Lions vs Chicago Bears on November 19, 2023",
		"endDate": "",
		"name": "Chicago Bears @ Detroit Lions",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190det.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Ford Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			},
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			}
		],
		"description": "Houston Texans vs Arizona Cardinals on November 19, 2023",
		"endDate": "",
		"name": "Arizona Cardinals @ Houston Texans",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190htx.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "NRG Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			},
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			}
		],
		"description": "Washington Commanders vs New York Giants on November 19, 2023",
		"endDate": "",
		"name": "New York Giants @ Washington Commanders",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190was.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "FedExField"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			},
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			}
		],
		"description": "San Francisco 49ers vs Tampa Bay Buccaneers on November 19, 2023",
		"endDate": "",
		"name": "Tampa Bay Buccaneers @ San Francisco 49ers",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190sfo.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Levi's Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			}
		],
		"description": "Los Angeles Rams vs Seattle Seahawks on November 19, 2023",
		"endDate": "",
		"name": "Seattle Seahawks @ Los Angeles Rams",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190ram.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			},
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			}
		],
		"description": "Buffalo Bills vs New York Jets on November 19, 2023",
		"endDate": "",
		"name": "New York Jets @ Buffalo Bills",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190buf.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Highmark Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			},
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			}
		],
		"description": "Denver Broncos vs Minnesota Vikings on November 19, 2023",
		"endDate": "",
		"name": "Minnesota Vikings @ Denver Broncos",
			"sport": "Football",
		"startDate": "November 19, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311190den.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Empower Field at Mile High"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			},
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			}
		],
		"description": "Kansas City Chiefs vs Philadelphia Eagles on November 20, 2023",
		"endDate": "",
		"name": "Philadelphia Eagles @ Kansas City Chiefs",
			"sport": "Football",
		"startDate": "November 20, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311200kan.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "GEHA Field at Arrowhead Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			},
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			}
		],
		"description": "Detroit Lions vs Green Bay Packers on November 23, 2023",
		"endDate": "",
		"name": "Green Bay Packers @ Detroit Lions",
			"sport": "Football",
		"startDate": "November 23, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311230det.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Ford Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			},
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			}
		],
		"description": "Dallas Cowboys vs Washington Commanders on November 23, 2023",
		"endDate": "",
		"name": "Washington Commanders @ Dallas Cowboys",
			"sport": "Football",
		"startDate": "November 23, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311230dal.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "AT&T Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			},
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			}
		],
		"description": "Seattle Seahawks vs San Francisco 49ers on November 23, 2023",
		"endDate": "",
		"name": "San Francisco 49ers @ Seattle Seahawks",
			"sport": "Football",
		"startDate": "November 23, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311230sea.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lumen Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			}
		],
		"description": "New York Jets vs Miami Dolphins on November 24, 2023",
		"endDate": "",
		"name": "Miami Dolphins @ New York Jets",
			"sport": "Football",
		"startDate": "November 24, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311240nyj.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			},
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			}
		],
		"description": "Atlanta Falcons vs New Orleans Saints on November 26, 2023",
		"endDate": "",
		"name": "New Orleans Saints @ Atlanta Falcons",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260atl.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Mercedes-Benz Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			},
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			}
		],
		"description": "Tennessee Titans vs Carolina Panthers on November 26, 2023",
		"endDate": "",
		"name": "Carolina Panthers @ Tennessee Titans",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260oti.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Nissan Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			},
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			}
		],
		"description": "Cincinnati Bengals vs Pittsburgh Steelers on November 26, 2023",
		"endDate": "",
		"name": "Pittsburgh Steelers @ Cincinnati Bengals",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260cin.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Paycor Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			},
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			}
		],
		"description": "Indianapolis Colts vs Tampa Bay Buccaneers on November 26, 2023",
		"endDate": "",
		"name": "Tampa Bay Buccaneers @ Indianapolis Colts",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260clt.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lucas Oil Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			},
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			}
		],
		"description": "Houston Texans vs Jacksonville Jaguars on November 26, 2023",
		"endDate": "",
		"name": "Jacksonville Jaguars @ Houston Texans",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260htx.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "NRG Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			}
		],
		"description": "New York Giants vs New England Patriots on November 26, 2023",
		"endDate": "",
		"name": "New England Patriots @ New York Giants",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260nyg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			},
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			}
		],
		"description": "Denver Broncos vs Cleveland Browns on November 26, 2023",
		"endDate": "",
		"name": "Cleveland Browns @ Denver Broncos",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260den.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Empower Field at Mile High"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			},
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			}
		],
		"description": "Arizona Cardinals vs Los Angeles Rams on November 26, 2023",
		"endDate": "",
		"name": "Los Angeles Rams @ Arizona Cardinals",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260crd.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "State Farm Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			},
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			}
		],
		"description": "Las Vegas Raiders vs Kansas City Chiefs on November 26, 2023",
		"endDate": "",
		"name": "Kansas City Chiefs @ Las Vegas Raiders",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260rai.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Allegiant Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			},
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			}
		],
		"description": "Philadelphia Eagles vs Buffalo Bills on November 26, 2023",
		"endDate": "",
		"name": "Buffalo Bills @ Philadelphia Eagles",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260phi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lincoln Financial Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			}
		],
		"description": "Los Angeles Chargers vs Baltimore Ravens on November 26, 2023",
		"endDate": "",
		"name": "Baltimore Ravens @ Los Angeles Chargers",
			"sport": "Football",
		"startDate": "November 26, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311260sdg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			},
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			}
		],
		"description": "Minnesota Vikings vs Chicago Bears on November 27, 2023",
		"endDate": "",
		"name": "Chicago Bears @ Minnesota Vikings",
			"sport": "Football",
		"startDate": "November 27, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311270min.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "U.S. Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			},
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			}
		],
		"description": "Dallas Cowboys vs Seattle Seahawks on November 30, 2023",
		"endDate": "",
		"name": "Seattle Seahawks @ Dallas Cowboys",
			"sport": "Football",
		"startDate": "November 30, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202311300dal.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "AT&T Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			}
		],
		"description": "New York Jets vs Atlanta Falcons on December 3, 2023",
		"endDate": "",
		"name": "Atlanta Falcons @ New York Jets",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030nyj.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			},
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			}
		],
		"description": "Tennessee Titans vs Indianapolis Colts on December 3, 2023",
		"endDate": "",
		"name": "Indianapolis Colts @ Tennessee Titans",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030oti.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Nissan Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			},
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			}
		],
		"description": "Houston Texans vs Denver Broncos on December 3, 2023",
		"endDate": "",
		"name": "Denver Broncos @ Houston Texans",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030htx.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "NRG Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			},
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			}
		],
		"description": "New Orleans Saints vs Detroit Lions on December 3, 2023",
		"endDate": "",
		"name": "Detroit Lions @ New Orleans Saints",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030nor.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Caesars Superdome"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			},
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			}
		],
		"description": "Washington Commanders vs Miami Dolphins on December 3, 2023",
		"endDate": "",
		"name": "Miami Dolphins @ Washington Commanders",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030was.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "FedExField"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			},
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			}
		],
		"description": "New England Patriots vs Los Angeles Chargers on December 3, 2023",
		"endDate": "",
		"name": "Los Angeles Chargers @ New England Patriots",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030nwe.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Gillette Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			},
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			}
		],
		"description": "Pittsburgh Steelers vs Arizona Cardinals on December 3, 2023",
		"endDate": "",
		"name": "Arizona Cardinals @ Pittsburgh Steelers",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030pit.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Acrisure Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			},
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			}
		],
		"description": "Tampa Bay Buccaneers vs Carolina Panthers on December 3, 2023",
		"endDate": "",
		"name": "Carolina Panthers @ Tampa Bay Buccaneers",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030tam.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Raymond James Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			}
		],
		"description": "Los Angeles Rams vs Cleveland Browns on December 3, 2023",
		"endDate": "",
		"name": "Cleveland Browns @ Los Angeles Rams",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030ram.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			},
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			}
		],
		"description": "Philadelphia Eagles vs San Francisco 49ers on December 3, 2023",
		"endDate": "",
		"name": "San Francisco 49ers @ Philadelphia Eagles",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030phi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lincoln Financial Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			},
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			}
		],
		"description": "Green Bay Packers vs Kansas City Chiefs on December 3, 2023",
		"endDate": "",
		"name": "Kansas City Chiefs @ Green Bay Packers",
			"sport": "Football",
		"startDate": "December 3, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312030gnb.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lambeau Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			},
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			}
		],
		"description": "Jacksonville Jaguars vs Cincinnati Bengals on December 4, 2023",
		"endDate": "",
		"name": "Cincinnati Bengals @ Jacksonville Jaguars",
			"sport": "Football",
		"startDate": "December 4, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312040jax.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "EverBank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			},
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			}
		],
		"description": "Pittsburgh Steelers vs New England Patriots on December 7, 2023",
		"endDate": "",
		"name": "New England Patriots @ Pittsburgh Steelers",
			"sport": "Football",
		"startDate": "December 7, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312070pit.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Acrisure Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			},
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			}
		],
		"description": "Atlanta Falcons vs Tampa Bay Buccaneers on December 10, 2023",
		"endDate": "",
		"name": "Tampa Bay Buccaneers @ Atlanta Falcons",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100atl.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Mercedes-Benz Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			},
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			}
		],
		"description": "New Orleans Saints vs Carolina Panthers on December 10, 2023",
		"endDate": "",
		"name": "Carolina Panthers @ New Orleans Saints",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100nor.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Caesars Superdome"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			},
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			}
		],
		"description": "Chicago Bears vs Detroit Lions on December 10, 2023",
		"endDate": "",
		"name": "Detroit Lions @ Chicago Bears",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100chi.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Soldier Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			},
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			}
		],
		"description": "Cincinnati Bengals vs Indianapolis Colts on December 10, 2023",
		"endDate": "",
		"name": "Indianapolis Colts @ Cincinnati Bengals",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100cin.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Paycor Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			},
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			}
		],
		"description": "Cleveland Browns vs Jacksonville Jaguars on December 10, 2023",
		"endDate": "",
		"name": "Jacksonville Jaguars @ Cleveland Browns",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100cle.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Cleveland Browns Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			}
		],
		"description": "New York Jets vs Houston Texans on December 10, 2023",
		"endDate": "",
		"name": "Houston Texans @ New York Jets",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100nyj.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			},
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			}
		],
		"description": "Baltimore Ravens vs Los Angeles Rams on December 10, 2023",
		"endDate": "",
		"name": "Los Angeles Rams @ Baltimore Ravens",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100rav.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "M&T Bank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			},
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			}
		],
		"description": "Las Vegas Raiders vs Minnesota Vikings on December 10, 2023",
		"endDate": "",
		"name": "Minnesota Vikings @ Las Vegas Raiders",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100rai.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Allegiant Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			},
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			}
		],
		"description": "San Francisco 49ers vs Seattle Seahawks on December 10, 2023",
		"endDate": "",
		"name": "Seattle Seahawks @ San Francisco 49ers",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100sfo.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Levi's Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			},
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			}
		],
		"description": "Kansas City Chiefs vs Buffalo Bills on December 10, 2023",
		"endDate": "",
		"name": "Buffalo Bills @ Kansas City Chiefs",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100kan.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "GEHA Field at Arrowhead Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			}
		],
		"description": "Los Angeles Chargers vs Denver Broncos on December 10, 2023",
		"endDate": "",
		"name": "Denver Broncos @ Los Angeles Chargers",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100sdg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			},
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			}
		],
		"description": "Dallas Cowboys vs Philadelphia Eagles on December 10, 2023",
		"endDate": "",
		"name": "Philadelphia Eagles @ Dallas Cowboys",
			"sport": "Football",
		"startDate": "December 10, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312100dal.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "AT&T Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			},
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			}
		],
		"description": "New York Giants vs Green Bay Packers on December 11, 2023",
		"endDate": "",
		"name": "Green Bay Packers @ New York Giants",
			"sport": "Football",
		"startDate": "December 11, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312110nyg.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "MetLife Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			},
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			}
		],
		"description": "Miami Dolphins vs Tennessee Titans on December 11, 2023",
		"endDate": "",
		"name": "Tennessee Titans @ Miami Dolphins",
			"sport": "Football",
		"startDate": "December 11, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312110mia.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Hard Rock Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Chargers"
			},
			{
			"@type": "SportsTeam",
			"name": "Las Vegas Raiders"
			}
		],
		"description": "Las Vegas Raiders vs Los Angeles Chargers on December 14, 2023",
		"endDate": "",
		"name": "Los Angeles Chargers @ Las Vegas Raiders",
			"sport": "Football",
		"startDate": "December 14, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312140rai.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Allegiant Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Minnesota Vikings"
			},
			{
			"@type": "SportsTeam",
			"name": "Cincinnati Bengals"
			}
		],
		"description": "Cincinnati Bengals vs Minnesota Vikings on December 16, 2023",
		"endDate": "",
		"name": "Minnesota Vikings @ Cincinnati Bengals",
			"sport": "Football",
		"startDate": "December 16, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312160cin.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Paycor Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Pittsburgh Steelers"
			},
			{
			"@type": "SportsTeam",
			"name": "Indianapolis Colts"
			}
		],
		"description": "Indianapolis Colts vs Pittsburgh Steelers on December 16, 2023",
		"endDate": "",
		"name": "Pittsburgh Steelers @ Indianapolis Colts",
			"sport": "Football",
		"startDate": "December 16, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312160clt.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lucas Oil Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Denver Broncos"
			},
			{
			"@type": "SportsTeam",
			"name": "Detroit Lions"
			}
		],
		"description": "Detroit Lions vs Denver Broncos on December 16, 2023",
		"endDate": "",
		"name": "Denver Broncos @ Detroit Lions",
			"sport": "Football",
		"startDate": "December 16, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312160det.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Ford Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Atlanta Falcons"
			},
			{
			"@type": "SportsTeam",
			"name": "Carolina Panthers"
			}
		],
		"description": "Carolina Panthers vs Atlanta Falcons on December 17, 2023",
		"endDate": "",
		"name": "Atlanta Falcons @ Carolina Panthers",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170car.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Bank of America Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Chicago Bears"
			},
			{
			"@type": "SportsTeam",
			"name": "Cleveland Browns"
			}
		],
		"description": "Cleveland Browns vs Chicago Bears on December 17, 2023",
		"endDate": "",
		"name": "Chicago Bears @ Cleveland Browns",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170cle.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Cleveland Browns Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Tampa Bay Buccaneers"
			},
			{
			"@type": "SportsTeam",
			"name": "Green Bay Packers"
			}
		],
		"description": "Green Bay Packers vs Tampa Bay Buccaneers on December 17, 2023",
		"endDate": "",
		"name": "Tampa Bay Buccaneers @ Green Bay Packers",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170gnb.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lambeau Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Houston Texans"
			},
			{
			"@type": "SportsTeam",
			"name": "Tennessee Titans"
			}
		],
		"description": "Tennessee Titans vs Houston Texans on December 17, 2023",
		"endDate": "",
		"name": "Houston Texans @ Tennessee Titans",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170oti.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Nissan Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Kansas City Chiefs"
			},
			{
			"@type": "SportsTeam",
			"name": "New England Patriots"
			}
		],
		"description": "New England Patriots vs Kansas City Chiefs on December 17, 2023",
		"endDate": "",
		"name": "Kansas City Chiefs @ New England Patriots",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170nwe.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Gillette Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Jets"
			},
			{
			"@type": "SportsTeam",
			"name": "Miami Dolphins"
			}
		],
		"description": "Miami Dolphins vs New York Jets on December 17, 2023",
		"endDate": "",
		"name": "New York Jets @ Miami Dolphins",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170mia.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Hard Rock Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New York Giants"
			},
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			}
		],
		"description": "New Orleans Saints vs New York Giants on December 17, 2023",
		"endDate": "",
		"name": "New York Giants @ New Orleans Saints",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170nor.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Caesars Superdome"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "San Francisco 49ers"
			},
			{
			"@type": "SportsTeam",
			"name": "Arizona Cardinals"
			}
		],
		"description": "Arizona Cardinals vs San Francisco 49ers on December 17, 2023",
		"endDate": "",
		"name": "San Francisco 49ers @ Arizona Cardinals",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170crd.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "State Farm Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Washington Commanders"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			}
		],
		"description": "Los Angeles Rams vs Washington Commanders on December 17, 2023",
		"endDate": "",
		"name": "Washington Commanders @ Los Angeles Rams",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170ram.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Dallas Cowboys"
			},
			{
			"@type": "SportsTeam",
			"name": "Buffalo Bills"
			}
		],
		"description": "Buffalo Bills vs Dallas Cowboys on December 17, 2023",
		"endDate": "",
		"name": "Dallas Cowboys @ Buffalo Bills",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170buf.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Highmark Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Baltimore Ravens"
			},
			{
			"@type": "SportsTeam",
			"name": "Jacksonville Jaguars"
			}
		],
		"description": "Jacksonville Jaguars vs Baltimore Ravens on December 17, 2023",
		"endDate": "",
		"name": "Baltimore Ravens @ Jacksonville Jaguars",
			"sport": "Football",
		"startDate": "December 17, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312170jax.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "EverBank Stadium"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "Philadelphia Eagles"
			},
			{
			"@type": "SportsTeam",
			"name": "Seattle Seahawks"
			}
		],
		"description": "Seattle Seahawks vs Philadelphia Eagles on December 18, 2023",
		"endDate": "",
		"name": "Philadelphia Eagles @ Seattle Seahawks",
			"sport": "Football",
		"startDate": "December 18, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312180sea.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "Lumen Field"
		}
	},

	{
		"@context": "http://www.schema.org",
		"@type": "SportsEvent",
		"competitor": [
			{
			"@type": "SportsTeam",
			"name": "New Orleans Saints"
			},
			{
			"@type": "SportsTeam",
			"name": "Los Angeles Rams"
			}
		],
		"description": "Los Angeles Rams vs New Orleans Saints on December 21, 2023",
		"endDate": "",
		"name": "New Orleans Saints @ Los Angeles Rams",
			"sport": "Football",
		"startDate": "December 21, 2023",
			"url": "https://www.pro-football-reference.com/boxscores/202312210ram.htm",
		"eventStatus": "https://schema.org/EventScheduled",
		"location": {
			"@type": "Place",
			"name": "SoFi Stadium"
		}
	}

]</script>
<!-- HeaderSportsEventSchema:END -->

    <!-- HeaderSeoSocial -->
    <meta name="keywords" content="">
    <meta itemprop="url"           content="https://www.pro-football-reference.com">
    <meta itemprop="name"          content="Pro Football Reference">
    <meta itemprop="alternateName" content="PFRef">
    <meta property="fb:app_id"     content="">
    <meta property="og:url"          content="https://www.pro-football-reference.com/years/2023/games.htm">
    <meta property="og:title"        content="2023 NFL Weekly League Schedule | Pro-Football-Reference.com">
    <meta property="og:site_name"    content="Pro-Football-Reference.com">
    <meta property="og:type"         content="    article" />
    <meta property="og:description"  content="Check out the 2023 NFL Weekly League Schedule including AFC and NFC results and standings on Pro-football-reference.com">
    <meta property="og:image"        content="http://cdn.ssref.net/scripts/image_resize.cgi?min=200&url=https://cdn.ssref.net/req/202312151/tlogo/pfr/NFL-2023.png">
    <meta name="twitter:card"         content="summary">
    <meta name="twitter:site"         content="@pfref">
    <meta name="twitter:creator"      content="@pfref">
    <meta property="twitter:image"    content="http://cdn.ssref.net/scripts/image_resize.cgi?min=200&url=https://cdn.ssref.net/req/202312151/tlogo/pfr/NFL-2023.png">
    <meta name="twitter:domain"       content="Pro-Football-Reference.com">
    <meta name="referrer" content="unsafe-url">
    <!-- HeaderSeoSocial:END -->

    <!-- tiles, touch, favicons -->
    <link rel="apple-touch-icon-precomposed" sizes="180x180" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-180x180-precomposed.png">
    <link rel="icon"                         sizes="48x48"   href="https://cdn.ssref.net/req/202311303/favicons/pfr/favicon-48.png">
    <link rel="shortcut icon"                sizes="228x228" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-228x228-precomposed.png">
    <link rel="apple-touch-icon"             sizes="228x228" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-228x228-precomposed.png">
    <link rel="apple-touch-icon"             sizes="195x195" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-195x195-precomposed.png">
    <link rel="apple-touch-icon"             sizes="180x180" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-180x180-precomposed.png">
    <link rel="apple-touch-icon"             sizes="152x152" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-152x152-precomposed.png">
    <link rel="apple-touch-icon"             sizes="144x144" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon"             sizes="128x128" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-128x128-precomposed.png">
    <link rel="apple-touch-icon"             sizes="120x120" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-120x120-precomposed.png">
    <link rel="apple-touch-icon"             sizes="114x114" href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon"             sizes="76x76"   href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-76x76-precomposed.png">
    <link rel="apple-touch-icon"             sizes="72x72"   href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon"             sizes="57x57"   href="https://cdn.ssref.net/req/202311303/favicons/pfr/apple-touch-icon-57x57-precomposed.png">
    <link rel="icon"                         sizes="32x32"   href="https://cdn.ssref.net/req/202311303/favicons/pfr/favicon-32.png">
    <!--[if IE]>
    <link rel="shortcut icon"                                href="https://cdn.ssref.net/req/202311303/favicons/pfr/favicon.ico"><![endif]-->
    <meta name="msapplication-TileColor" content="#005629" />
    <meta name="msapplication-TileImage" content="https://cdn.ssref.net/req/202311303/favicons/pfr/ms-tile-144.png" />
    <link rel=search        type="application/opensearchdescription+xml" href="https://cdn.ssref.net/req/202311303/opensearch/opensearch-pfr.xml" title=" Player and Team Search">
    <!-- tiles, touch, favicons:end -->

<!-- ad code: begin -->


    <link rel="preconnect" href="https://a.pub.network/" crossorigin />
    <link rel="preconnect" href="https://b.pub.network/" crossorigin />
    <link rel="preconnect" href="https://c.pub.network/" crossorigin />
    <link rel="preconnect" href="https://d.pub.network/" crossorigin />
    <link rel="preconnect" href="https://c.amazon-adsystem.com" crossorigin />
    <link rel="preconnect" href="https://s.amazon-adsystem.com" crossorigin />
    <link rel="preconnect" href="https://btloader.com/" crossorigin />
    <link rel="preconnect" href="https://api.btloader.com/" crossorigin />
    <link rel="preconnect" href="https://confiant-integrations.global.ssl.fastly.net" crossorigin />
<script data-ad-client="ca-pub-5319453360923253" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

<link rel="stylesheet" href="https://a.pub.network/pro-football-reference/cls.css" type="text/css">
<script>
    var freestar = freestar || {};
    freestar.config = freestar.config || {};
    freestar.config.enabled_slots = [ "div-gpt-ad-300x250-ATF","div-gpt-ad-728x90-ATF","div-gpt-ad-728x90-GeneralHeader","div-gpt-ad-728x90-Footer" ];
    if (sr_detect_ie || sr_detect_edge || Modernizr.adfree || document.getElementById('sr_suppress_ads') || Modernizr.viewport_width < 1810) {
    // do not include the rails
    }
    else {
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
!function(a,b){
    if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {
        return;
    }  
    var c=b.getElementsByTagName("script")[0],
    d=b.createElement("script"),
    e="https://a.pub.network/pro-football-reference";
    e+=fs_debug?"/qa/pubfig.min.js":"/pubfig.min.js",
    d.async=!0,
    d.src=e,
    c.parentNode.insertBefore(d,c)
}(window,document);
</script>


<!-- ad code:end -->


</head>
<body class="pfr">
<div id="wrap">

  <div id="header" role="banner">

<ul id="subnav" class="notranslate">
	<li><a href="https://www.sports-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav"><svg height="15px" width="20px"><use xlink:href="#ic-sr-pennant"></use></svg> Sports&nbsp;Reference&#8239;&reg;</a></li>
	<li><a href="https://www.baseball-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Baseball</a></li>
	<li class="current"><a href="https://www.pro-football-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Football</a> <a href="https://www.sports-reference.com/cfb/">(college)</a></li>
	<li><a href="https://www.basketball-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Basketball</a> <a href="https://www.sports-reference.com/cbb/">(college)</a></li>
	<li><a href="https://www.hockey-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Hockey</a></li>





	<li><a href="https://fbref.com/de/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Fußball</a></li>

	<li><a href="https://www.sports-reference.com/blog/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Blog</a></li>
    <li><a href="https://stathead.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Stathead&#8239;&reg;</a></li>

	<li><a href="https://www.immaculategrid.com/football/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Immaculate Grid</a></li>


	<li><a href="https://www.sports-reference.com/feedback/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav">Questions or Comments?</a></li>
	<li class="user logged_in">Welcome <span class="username"></span>&nbsp;&#183;&nbsp;<a href="https://stathead.com/profile/?utm_source=pfr&amp;utm_medium=sr_xsite&amp;utm_campaign=2023_01_srnav_account">Your Account</a></li>
<li class="user logged_in"><a class="logout" onclick="sr_auth_logout_page_elements();if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/profile/?do=logout">Logout</a></li>
<li class="user not_logged_in"><a class="login" onclick="if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/users/login.cgi?token=1">Ad-Free Login</a></li>
<li class="user not_logged_in"><a href="https://stathead.com/users/signup.cgi">Create Account</a></li>

</ul>

  <a href="/"><img src="https://cdn.ssref.net/req/202311303/logos/pfr-logo.svg" onerror="this.src='https://cdn.ssref.net/req/202311303/logos/pfr-logo.png'; this.onerror = null;" alt="Pro-Football-Reference.com Logo &amp; Link to home page" /></a>
<div id="nav_trigger" role="button"><a href="#site_menu_link">MENU</a></div>
<div id="nav" role="navigation" aria-label="Pro-Football-Reference.com sections">
	<ul id="main_nav" class="hoversmooth nohover">	        <li id="header_players" ><a href="/players">Players</a></li>
		<li id="header_teams" ><a href="/teams/">Teams</a></li>
		<li id="header_years" class="current"><a href="/years/">Seasons</a></li>
		<li id="header_leaders" ><a href="/leaders/">Leaders</a></li>
		<li id="header_scores" ><a href="/boxscores/">NFL Scores</a></li>

		<li id="header_draft" class=""><a href="/draft/">Draft</a></li>	

		<li id="header_playindex" class=""><a href="https://stathead.com/sport/football/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_topnav_stathead&utm_content=lnk_top">Stathead</a></li>
		<li><a href="https://www.pro-football-reference.com/email/">Newsletter</a></li>

		<li><a data-scroll href="#site_menu_link" class="opener">Full Site Menu Below</a></li>
	</ul>
	<div class="breadcrumbs">You are here: <div itemscope itemtype="https://schema.org/BreadcrumbList" class="crumbs"><span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="/"><span itemprop="name">PFR Home Page</span></a> <meta itemprop="position" content="1" /></span> &gt; <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="/years/"><span itemprop="name">All Years</span></a> <meta itemprop="position" content="2" /></span> &gt; <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="/years/2023/"><span itemprop="name">2023 NFL</span></a> <meta itemprop="position" content="3" /></span> &gt; <strong>Schedule</strong></div></div>
	<ul class="usertools bullets-inline"><li class="user logged_in">Welcome <span class="username"></span>&nbsp;&#183;&nbsp;<a href="https://stathead.com/profile/?utm_source=pfr&amp;utm_medium=sr_xsite&amp;utm_campaign=2023_01_srnav_account">Your Account</a></li>
<li class="user logged_in"><a class="logout" onclick="sr_auth_logout_page_elements();if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/profile/?do=logout">Logout</a></li>
<li class="user not_logged_in"><a class="login" onclick="if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/users/login.cgi?token=1">Ad-Free Login</a></li>
<li class="user not_logged_in"><a href="https://stathead.com/users/signup.cgi">Create Account</a></li>
	</ul><!-- ul.user -->
</div><!-- div#nav -->
<script>
function sr_menus_setupMainNav_button_inline () {
    if (sr_detect_operaMini || !("classList" in document.createElement("_"))) {
	return false;
    }
    var nav_trigger = document.getElementById('nav_trigger');
    if(!nav_trigger || nav_trigger.triggered) {
	return false;
    }
    nav_trigger.triggered = true;
    var nav = document.getElementById('nav');
    var nav_trigger_a = nav_trigger.querySelector('a');
    if (nav_trigger_a) {
	nav_trigger_a.setAttribute('href','javascript:void(0)');
	nav_trigger.onclick = function (event) {
	    nav.classList.toggle('open');
	    var is_open = nav.classList.contains('open');
	    if (is_open) {
		nav_trigger.classList.add('open');
	    }
	    else {
		nav_trigger.classList.remove('open');
	    }
	    event.preventDefault();
	    try { sr_record_analytics_event('MainNavButtonClick_inline',sr_record_directory(),sr_record_page());}
	    catch(err) {}
	};
    }
    return true;
}
sr_menus_setupMainNav_button_inline();
</script><div class="search" role="search" aria-label="Site Search for players, teams and sections">
<form method="get" name="f_big"  action="/search/search.fcgi">
<div class="ac-outline">
  <div class="ac-wrapper"><input type="search" tabindex="-1" class="ac-hint" name="hint" placeholder="" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" dir="auto" aria-label="Search suggestions based on user search input">

<input tabindex="1" type="search" class="ac-input completely" name="search" placeholder="Enter Person, Team, Section, etc" aria-label="Enter a player, team or section name" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" dir="auto" />
    <div class="ac-dropdown"></div>
  </div>
</div>

<input type="submit" value="Search" tabindex="2" />
<input type="hidden" name="pid" value="" data-search-id>
<input type="hidden" name="idx" value="" data-search-idx>

</form>
</div><!-- div.search -->

</div><!-- div#header -->

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



<div id="info" class="years">
	<div id="meta">



	<div class="media-item logo loader">
		<img class="teamlogo"			src="https://cdn.ssref.net/req/202312151/tlogo/pfr/NFL.png"
			alt=" Logo">

			<p><a href="http://www.sportslogos.net/">via Sports Logos.net</a></p>
			<p><a href="https://www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">About logos</a></p>

	</div>



		<div>
			<h1>

				<span>2023</span> <span>NFL</span> <span class="header_end">Weekly League Schedule</span>

			</h1>
			<div class="prevnext">

  <a href="/years/2022/games.htm" class="button2 prev">Previous Season</a>




</div>

			<p><strong>Passing Leader</strong>: <a href="/players/T/TagoTu00.htm">Tua Tagovailoa</a>, 3921 Yds</p>
<p><strong>Rushing Leader</strong>: <a href="/players/M/McCaCh01.htm">Christian McCaffrey</a>, 1292 Yds</p>
<p><strong>Receiving Leader</strong>: <a href="/players/H/HillTy00.htm">Tyreek Hill</a>, 1542 Yds</p>


			<button id="meta_more_button" class="opener" data-type="hide_after" data-class="open" data-id="info">More league info</button>
<script>
// see sr.menus.js:sr_menus_checkInfoCookie to explain
function sr_menus_checkInfoCookie_inline(browserType) {
    var el_info = document.getElementById('info');
    var el_button = document.getElementById('meta_more_button');
    var bling_len = 0;    
    if (!el_button || !el_info || !el_info.classList) { console.log('no meta_button'); return; }
    var el = el_button;
    var siblingsHidden = 0;
    while (el = el.previousSibling) { if ((el.nodeType === 1) && (el.offsetWidth <= 0 || el.offsetHeight <= 0)) { siblingsHidden++; } }
    var button_cookie = false;
    if (browserType === 'desktop') {  button_cookie = vjs_readCookie('meta_more_button');   }
    // We allow up to four of bling lines or additional player bio data entries in mobile.
    if (el_info && el_button && (button_cookie || (siblingsHidden + bling_len <= 4))) {el_button.parentNode.removeChild(el_button);	el_info.classList.add('open');  }
    else { el_button.classList.add('show');  }
}
if (Modernizr.desktop || Modernizr.laptop) { sr_menus_checkInfoCookie_inline('desktop'); } else { sr_menus_checkInfoCookie_inline('mobile'); }
var sr_menus_checkInfoCookie_run_inline = true;
</script>

		</div>
	</div>

<div class="adblock ad300">

<!-- div#fs_fs_300_atf  -->
<div align="center" id="div-gpt-ad-300x250-ATF"  data-freestar-ad="__336x280">
    <script data-cfasync="false" type='text/javascript'>
    if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {
    }
    else {
        console.log('push ad:div-gpt-ad-300x250-ATF');
        freestar.queue.push(function() { googletag.display('div-gpt-ad-300x250-ATF'); });
    }
    </script>
</div>
<!-- /div.#fs_fs_300_atf -->


</div>


</div>
<div id="srcom">
<div class="adblock ad728">

<!-- div#fs_fs_728_atf  -->
<!-- sf:blank by design for send to news ad -->
<!-- /div.#fs_fs_728_atf -->


</div>


</div>

<div id="inner_nav" role="navigation" aria-label="Sections on this page and/or other pages related to this page" class=" inactive">
	<ul class="hoversmooth">
		<li			class="index "><a href="/years/2023/">2023 NFL Season</a>		</li>
		<li data-fade-selector="#inpage_nav"			class="full hasmore "><a href="#">Player&nbsp;Stats</a>
			<div>
<p class="listhead">Standard</p>
					<ul class="">
						<li><a href="/years/2023/passing.htm" >Passing</a></li>
						<li><a href="/years/2023/rushing.htm" >Rushing</a></li>
						<li><a href="/years/2023/receiving.htm" >Receiving</a></li>
						<li><a href="/years/2023/scrimmage.htm" >Scrimmage Stats</a></li>
						<li><a href="/years/2023/defense.htm" >Defense</a></li>
						<li><a href="/years/2023/kicking.htm" >Kicking</a></li>
						<li><a href="/years/2023/punting.htm" >Punting</a></li>
						<li><a href="/years/2023/returns.htm" >Kick &amp; Punt Returns</a></li>
						<li><a href="/years/2023/scoring.htm" >Scoring</a></li>
					</ul>

<p class="listhead">Advanced</p>
					<ul class="">
						<li><a href="/years/2023/passing_advanced.htm" >Passing</a></li>
						<li><a href="/years/2023/rushing_advanced.htm" >Rushing</a></li>
						<li><a href="/years/2023/receiving_advanced.htm" >Receiving</a></li>
						<li><a href="/years/2023/defense_advanced.htm" >Defense</a></li>
						<li><a href="/years/2023/advanced.htm" >Team Adv. Stats</a></li>
					</ul>

<p class="listhead">Fantasy</p>
					<ul class="">
						<li><a href="/years/2023/fantasy.htm" >Player Fantasy Ranks</a></li>
						<li><a href="/years/2023/redzone-passing.htm" >Red Zone Passing</a></li>
						<li><a href="/years/2023/redzone-rushing.htm" >Red Zone Rushing</a></li>
						<li><a href="/years/2023/redzone-receiving.htm" >Red Zone Receiving</a></li>
					</ul>

			</div>		</li>
		<li data-fade-selector="#inpage_nav"			class="full hasmore "><a href="#">Defensive Stats</a>
			<div>

					<ul class="">
						<li><a href="/years/2023/opp.htm" >Team Defense</a></li>
					</ul>

<p class="listhead">Defense vs. Pos</p>
					<ul class="">
						<li><a href="/years/2023/fantasy-points-against-RB.htm" >RB</a></li>
						<li><a href="/years/2023/fantasy-points-against-TE.htm" >TE</a></li>
						<li><a href="/years/2023/fantasy-points-against-QB.htm" >QB</a></li>
						<li><a href="/years/2023/fantasy-points-against-WR.htm" >WR</a></li>
					</ul>

			</div>		</li>
		<li data-fade-selector="#inpage_nav"			class="full hasmore "><a href="#">Weeks</a>
			<div>

					<ul class="">
						<li><a href="/years/2023/week_1.htm" >Week 1</a></li>
						<li><a href="/years/2023/week_2.htm" >Week 2</a></li>
						<li><a href="/years/2023/week_3.htm" >Week 3</a></li>
						<li><a href="/years/2023/week_4.htm" >Week 4</a></li>
						<li><a href="/years/2023/week_5.htm" >Week 5</a></li>
						<li><a href="/years/2023/week_6.htm" >Week 6</a></li>
						<li><a href="/years/2023/week_7.htm" >Week 7</a></li>
						<li><a href="/years/2023/week_8.htm" >Week 8</a></li>
						<li><a href="/years/2023/week_9.htm" >Week 9</a></li>
						<li><a href="/years/2023/week_10.htm" >Week 10</a></li>
						<li><a href="/years/2023/week_11.htm" >Week 11</a></li>
						<li><a href="/years/2023/week_12.htm" >Week 12</a></li>
						<li><a href="/years/2023/week_13.htm" >Week 13</a></li>
						<li><a href="/years/2023/week_14.htm" >Week 14</a></li>
						<li><a href="/years/2023/week_15.htm" >Week 15</a></li>
						<li><a href="/years/2023/week_16.htm" >Week 16</a></li>
						<li><a href="/years/2023/week_17.htm" >Week 17</a></li>
						<li><a href="/years/2023/week_18.htm" >Week 18</a></li>
					</ul>

			</div>		</li>
		<li			class="full "><a href="/years/2023/leaders.htm">Leaders</a>		</li>
		<li			class="full current "><a href="/years/2023/games.htm">Schedule</a>		</li>
		<li			class="full "><a href="/years/2023/coaches.htm">Coaches</a>		</li>
		<li data-fade-selector="#inpage_nav"			class="full hasmore "><a href="#">Awards</a>
			<div>

					<ul class="">
						<li><a href="/years/2023/allpro.htm" >AllPro</a></li>
						<li><a href="/years/2023/probowl.htm" >Pro&nbsp;Bowl</a></li>
						<li><a href="/awards/awards_2023.htm" >Awards Voting</a></li>
					</ul>

			</div>		</li>
		<li			class="full "><a href="/years/2023/draft.htm">Draft</a>		</li>
		<li data-fade-selector="#inpage_nav"			class="full hasmore "><a href="#">Other</a>
			<div>

					<ul class="">
						<li><a href="https://www.sports-reference.com/cfb/years/2023.html" >College Football</a></li>
						<li><a href="/years/2023/advanced.htm" >Advanced Stats</a></li>
						<li><a href="/years/2023/penalties.htm" >Penalties</a></li>
						<li><a href="/years/2023/ol_penalties.htm" >O-Line Penalties</a></li>
						<li><a href="/years/2023/training-camps.htm" >Training Camps</a></li>
						<li><a href="/years/2023/deaths.htm" >Deaths</a></li>
						<li><a href="/years/2023/debuts.htm" >Debuts</a></li>
						<li><a href="/years/2023/attendance.htm" >Attendance</a></li>
						<li><a href="/years/2023/preseason.htm" >Preseason</a></li>
						<li><a href="/years/2023/preseason_odds.htm" >Preseason Odds</a></li>
						<li><a href="/years/2023/splits.htm" >Splits</a></li>
					</ul>

<p class="listhead">Transactions</p>
					<ul class="">
						<li><a href="/years/2023/01_transactions.htm" >January</a></li>
						<li><a href="/years/2023/02_transactions.htm" >February</a></li>
						<li><a href="/years/2023/03_transactions.htm" >March</a></li>
						<li><a href="/years/2023/04_transactions.htm" >April</a></li>
						<li><a href="/years/2023/05_transactions.htm" >May</a></li>
						<li><a href="/years/2023/06_transactions.htm" >June</a></li>
						<li><a href="/years/2023/07_transactions.htm" >July</a></li>
						<li><a href="/years/2023/08_transactions.htm" >August</a></li>
						<li><a href="/years/2023/09_transactions.htm" >September</a></li>
						<li><a href="/years/2023/10_transactions.htm" >October</a></li>
						<li><a href="/years/2023/11_transactions.htm" >November</a></li>
						<li><a href="/years/2023/12_transactions.htm" >December</a></li>
					</ul>

			</div>		</li>
		<li data-fade-selector="#inpage_nav"			class="condensed hasmore "><span>More 2023 NFL Pages</span>
			<div>
<p class="listhead">Standard Player Stats</p>
					<ul class="">
						<li><a href="/years/2023/passing.htm" >Passing</a></li>
						<li><a href="/years/2023/rushing.htm" >Rushing</a></li>
						<li><a href="/years/2023/receiving.htm" >Receiving</a></li>
						<li><a href="/years/2023/scrimmage.htm" >Scrimmage Stats</a></li>
						<li><a href="/years/2023/defense.htm" >Defense</a></li>
						<li><a href="/years/2023/kicking.htm" >Kicking</a></li>
						<li><a href="/years/2023/punting.htm" >Punting</a></li>
						<li><a href="/years/2023/returns.htm" >Kick &amp; Punt Returns</a></li>
						<li><a href="/years/2023/scoring.htm" >Scoring</a></li>
					</ul>

<p class="listhead">Fantasy Player Stats</p>
					<ul class="">
						<li><a href="/years/2023/fantasy.htm" >Player Fantasy Ranks</a></li>
						<li><a href="/years/2023/redzone-passing.htm" >Red Zone Passing</a></li>
						<li><a href="/years/2023/redzone-rushing.htm" >Red Zone Rushing</a></li>
						<li><a href="/years/2023/redzone-receiving.htm" >Red Zone Receiving</a></li>
					</ul>

<p class="listhead">Defense vs. Pos</p>
					<ul class="">
						<li><a href="/years/2023/fantasy-points-against-RB.htm" >RB</a></li>
						<li><a href="/years/2023/fantasy-points-against-TE.htm" >TE</a></li>
						<li><a href="/years/2023/fantasy-points-against-QB.htm" >QB</a></li>
						<li><a href="/years/2023/fantasy-points-against-WR.htm" >WR</a></li>
					</ul>

<p class="listhead">Weeks</p>
					<ul class="">
						<li><a href="/years/2023/week_1.htm" >Week 1</a></li>
						<li><a href="/years/2023/week_2.htm" >Week 2</a></li>
						<li><a href="/years/2023/week_3.htm" >Week 3</a></li>
						<li><a href="/years/2023/week_4.htm" >Week 4</a></li>
						<li><a href="/years/2023/week_5.htm" >Week 5</a></li>
						<li><a href="/years/2023/week_6.htm" >Week 6</a></li>
						<li><a href="/years/2023/week_7.htm" >Week 7</a></li>
						<li><a href="/years/2023/week_8.htm" >Week 8</a></li>
						<li><a href="/years/2023/week_9.htm" >Week 9</a></li>
						<li><a href="/years/2023/week_10.htm" >Week 10</a></li>
						<li><a href="/years/2023/week_11.htm" >Week 11</a></li>
						<li><a href="/years/2023/week_12.htm" >Week 12</a></li>
						<li><a href="/years/2023/week_13.htm" >Week 13</a></li>
						<li><a href="/years/2023/week_14.htm" >Week 14</a></li>
						<li><a href="/years/2023/week_15.htm" >Week 15</a></li>
						<li><a href="/years/2023/week_16.htm" >Week 16</a></li>
						<li><a href="/years/2023/week_17.htm" >Week 17</a></li>
						<li><a href="/years/2023/week_18.htm" >Week 18</a></li>
					</ul>

<p class="listhead">Awards</p>
					<ul class="">
						<li><a href="/years/2023/allpro.htm" >AllPro</a></li>
						<li><a href="/years/2023/probowl.htm" >Pro&nbsp;Bowl</a></li>
						<li><a href="/awards/awards_2023.htm" >Awards Voting</a></li>
					</ul>


					<ul class=" in_list">
						<li><a href="/years/2023/opp.htm" >Team Defense</a></li>
						<li><a href="/years/2023/leaders.htm" >Leaders</a></li>
						<li><a href="/years/2023/games.htm" >Schedule</a></li>
						<li><a href="/years/2023/coaches.htm" >Coaches</a></li>
						<li><a href="/years/2023/draft.htm" >Draft</a></li>
						<li><a href="https://www.sports-reference.com/cfb/years/2023.html" >College Football</a></li>
						<li><a href="/years/2023/advanced.htm" >Advanced Stats</a></li>
						<li><a href="/years/2023/penalties.htm" >Penalties</a></li>
						<li><a href="/years/2023/ol_penalties.htm" >O-Line Penalties</a></li>
						<li><a href="/years/2023/training-camps.htm" >Training Camps</a></li>
						<li><a href="/years/2023/deaths.htm" >Deaths</a></li>
						<li><a href="/years/2023/debuts.htm" >Debuts</a></li>
						<li><a href="/years/2023/attendance.htm" >Attendance</a></li>
						<li><a href="/years/2023/preseason.htm" >Preseason</a></li>
						<li><a href="/years/2023/preseason_odds.htm" >Preseason Odds</a></li>
						<li><a href="/years/2023/splits.htm" >Splits</a></li>
					</ul>

<p class="listhead">Transactions</p>
					<ul class="">
						<li><a href="/years/2023/01_transactions.htm" >January</a></li>
						<li><a href="/years/2023/02_transactions.htm" >February</a></li>
						<li><a href="/years/2023/03_transactions.htm" >March</a></li>
						<li><a href="/years/2023/04_transactions.htm" >April</a></li>
						<li><a href="/years/2023/05_transactions.htm" >May</a></li>
						<li><a href="/years/2023/06_transactions.htm" >June</a></li>
						<li><a href="/years/2023/07_transactions.htm" >July</a></li>
						<li><a href="/years/2023/08_transactions.htm" >August</a></li>
						<li><a href="/years/2023/09_transactions.htm" >September</a></li>
						<li><a href="/years/2023/10_transactions.htm" >October</a></li>
						<li><a href="/years/2023/11_transactions.htm" >November</a></li>
						<li><a href="/years/2023/12_transactions.htm" >December</a></li>
					</ul>

			</div>		</li>
	</ul>






































</div><!-- div#inner_nav -->
<div id="content" role="main">









<!-- fs_general_header -->
<div class="adblock">


<!-- div#fs_fs_general_header  -->
<style>
    #srcom .adblock.stn,
    #content .adblock.stn { height: auto; width: 728px; max-width:100%; aspect-ratio: 1.677419;  margin: auto;  overflow: visible; }
    body:not(#stnPriority1):not(#stnPriority2):not(#stnPriority3) {    z-index: revert !important; }
</style>
<script>
function apiFunction(ApiHandshake)  {
    const playerDiv = document.querySelector('[data-stn-api="apiFunction"]');
    const api = ApiHandshake(playerDiv);
    new IntersectionObserver ( moes => { const bcr = moes.pop().boundingClientRect; api.float = bcr.y <= 0; },
                                       { threshold: [0.9] }).observe(document.querySelector('[data-stn-api="apiFunction"]'));
 }
</script>
<div class="adblock stn">
  <div class='s2nPlayer k-PV0o3K0Y' data-type='float' data-stn-api="apiFunction"></div>
  <script type='text/javascript' async src='//embed.sendtonews.com/player3/embedcode.js?fk=PV0o3K0Y&cid=13629&offsetx=0&offsety=0&floatwidth=400&floatposition=bottom-right' data-type='s2nScript'></script>
</div>
<!-- /div.#fs_fs_general_header -->


</div>





<div id="all_games" class="table_wrapper setup_long long">

<div class="section_heading assoc_games" id="games_sh">
  <span class="section_anchor" id="games_link" data-label="Week-by-Week Games"></span><h2>Week-by-Week Games</h2>    <div class="section_heading_text">
      <ul>
      </ul>
    </div>

</div>
<div class="table_container" id="div_games">

    <table class="sortable stats_table" id="games" data-cols-to-freeze="1,3">
    <caption>Week-by-Week Games Table</caption>


   <colgroup><col><col><col><col><col><col><col><col><col><col><col><col><col><col></colgroup>
   <thead>      
      <tr>
         <th aria-label="Week" data-stat="week_num" scope="col" class=" poptip sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" scope="col" class=" poptip sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" scope="col" class=" poptip sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" scope="col" class=" poptip sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" scope="col" class=" poptip sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" scope="col" class=" poptip sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" scope="col" class=" poptip sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" scope="col" class=" poptip sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" scope="col" class=" poptip center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" scope="col" class=" poptip center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" scope="col" class=" poptip center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" scope="col" class=" poptip center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" scope="col" class=" poptip center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" scope="col" class=" poptip center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      </thead>
<tbody><tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-09-07" >2023-09-07</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309070kan.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >368</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >316</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/atl/2023.htm">Atlanta Falcons</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100atl.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >221</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >281</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100cle.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >350</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >142</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100clt.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >21</td><td class="right " data-stat="yards_win" >342</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >280</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/was/2023.htm">Washington Commanders</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100was.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >248</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >210</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100rav.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>25</strong></td><td class="right " data-stat="pts_lose" >9</td><td class="right " data-stat="yards_win" >265</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >268</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100min.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >242</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >369</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nor/2023.htm">New Orleans Saints</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100nor.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>16</strong></td><td class="right " data-stat="pts_lose" >15</td><td class="right " data-stat="yards_win" >351</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >285</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100pit.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >7</td><td class="right " data-stat="yards_win" >391</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >239</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/gnb/2023.htm">Green Bay Packers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100chi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>38</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >329</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >311</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100den.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>17</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >261</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >260</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100sdg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>36</strong></td><td class="right " data-stat="pts_lose" >34</td><td class="right " data-stat="yards_win" >536</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >433</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100nwe.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>25</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >251</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >382</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/ram/2023.htm">Los Angeles Rams</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100sea.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >426</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >180</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-10" >2023-09-10</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309100nyg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>40</strong></td><td class="right iz" data-stat="pts_lose" >0</td><td class="right " data-stat="yards_win" >265</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >171</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="1" >1</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-09-11" >2023-09-11</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyj/2023.htm">New York Jets</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309110nyj.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>22</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >289</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >314</td><td class="right " data-stat="to_lose" >4</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-09-14" >2023-09-14</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309140phi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >28</td><td class="right " data-stat="yards_win" >430</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >374</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/atl/2023.htm">Atlanta Falcons</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170atl.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>25</strong></td><td class="right " data-stat="pts_lose" >24</td><td class="right " data-stat="yards_win" >446</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >224</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/buf/2023.htm">Buffalo Bills</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170buf.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>38</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >450</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >240</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170tam.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >437</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >236</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170cin.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >24</td><td class="right " data-stat="yards_win" >415</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >282</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/clt/2023.htm">Indianapolis Colts</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170htx.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >353</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >389</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sea/2023.htm">Seattle Seahawks</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/det/2023.htm">Detroit Lions</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170det.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >31</td><td class="right " data-stat="yards_win" >393</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >418</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170jax.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>17</strong></td><td class="right " data-stat="pts_lose" >9</td><td class="right " data-stat="yards_win" >399</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >271</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/oti/2023.htm">Tennessee Titans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170oti.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >24</td><td class="right " data-stat="yards_win" >341</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >342</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyg/2023.htm">New York Giants</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170crd.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >28</td><td class="right " data-stat="yards_win" >439</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >379</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170ram.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >23</td><td class="right " data-stat="yards_win" >365</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >386</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170dal.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >382</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >215</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/was/2023.htm">Washington Commanders</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170den.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>35</strong></td><td class="right " data-stat="pts_lose" >33</td><td class="right " data-stat="yards_win" >388</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >399</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-17" >2023-09-17</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309170nwe.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >389</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >288</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-09-18" >2023-09-18</td><td class="right " data-stat="gametime" >7:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nor/2023.htm">New Orleans Saints</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309180car.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >341</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >239</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="2" >2</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-09-18" >2023-09-18</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/cle/2023.htm">Cleveland Browns</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309180pit.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>26</strong></td><td class="right " data-stat="pts_lose" >22</td><td class="right " data-stat="yards_win" >255</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >408</td><td class="right " data-stat="to_lose" >4</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-09-21" >2023-09-21</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309210sfo.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >12</td><td class="right " data-stat="yards_win" >441</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >150</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240det.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >358</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >183</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/buf/2023.htm">Buffalo Bills</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240was.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >386</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >230</td><td class="right " data-stat="to_lose" >5</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240cle.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >341</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >94</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/clt/2023.htm">Indianapolis Colts</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/rav/2023.htm">Baltimore Ravens</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240rav.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>22</strong></td><td class="right " data-stat="pts_lose" >19</td><td class="right " data-stat="yards_win" >327</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >364</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240mia.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>70</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >726</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >363</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/gnb/2023.htm">Green Bay Packers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240gnb.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>18</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >340</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >252</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/htx/2023.htm">Houston Texans</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240jax.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >366</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >404</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240min.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >24</td><td class="right " data-stat="yards_win" >475</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >475</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nwe/2023.htm">New England Patriots</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240nyj.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>15</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >358</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >171</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sea/2023.htm">Seattle Seahawks</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240sea.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >27</td><td class="right " data-stat="yards_win" >425</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >378</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240kan.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>41</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >456</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >203</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/crd/2023.htm">Arizona Cardinals</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/dal/2023.htm">Dallas Cowboys</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240crd.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >400</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >416</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-09-24" >2023-09-24</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309240rai.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>23</strong></td><td class="right " data-stat="pts_lose" >18</td><td class="right " data-stat="yards_win" >333</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >362</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-09-25" >2023-09-25</td><td class="right " data-stat="gametime" >7:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309250tam.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>25</strong></td><td class="right " data-stat="pts_lose" >11</td><td class="right " data-stat="yards_win" >472</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >174</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="3" >3</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-09-25" >2023-09-25</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309250cin.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>19</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >309</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >292</td><td class="right " data-stat="to_lose" >2</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-09-28" >2023-09-28</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202309280gnb.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >401</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >230</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >9:30AM</td><td class="left " data-stat="winner" ><strong><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010jax.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>23</strong></td><td class="right " data-stat="pts_lose" >7</td><td class="right " data-stat="yards_win" >300</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >287</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/buf/2023.htm">Buffalo Bills</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/mia/2023.htm">Miami Dolphins</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010buf.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>48</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >414</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >393</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/min/2023.htm">Minnesota Vikings</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010car.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >265</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >232</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/den/2023.htm">Denver Broncos</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010chi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >28</td><td class="right " data-stat="yards_win" >311</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >471</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/oti/2023.htm">Tennessee Titans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010oti.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >400</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >211</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/cle/2023.htm">Cleveland Browns</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010cle.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >296</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >166</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/ram/2023.htm">Los Angeles Rams</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010clt.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>29</strong></td><td class="right " data-stat="pts_lose" >23</td><td class="right " data-stat="yards_win" >467</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >329</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/htx/2023.htm">Houston Texans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010htx.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >451</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >225</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010nor.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>26</strong></td><td class="right " data-stat="pts_lose" >9</td><td class="right " data-stat="yards_win" >353</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >197</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010phi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >31</td><td class="right " data-stat="yards_win" >415</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >365</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010sdg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >305</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >264</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010sfo.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>35</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >395</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >362</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010dal.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>38</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >377</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >253</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-01" >2023-10-01</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310010nyj.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>23</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >401</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >336</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="4" >4</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-10-02" >2023-10-02</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sea/2023.htm">Seattle Seahawks</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310020nyg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >281</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >248</td><td class="right " data-stat="to_lose" >3</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-10-05" >2023-10-05</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/chi/2023.htm">Chicago Bears</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310050was.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>40</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >451</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >388</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >9:30AM</td><td class="left " data-stat="winner" ><strong><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080buf.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>25</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >474</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >388</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/atl/2023.htm">Atlanta Falcons</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080atl.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >19</td><td class="right " data-stat="yards_win" >447</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >313</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080det.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>42</strong></td><td class="right " data-stat="pts_lose" >24</td><td class="right " data-stat="yards_win" >377</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >342</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/clt/2023.htm">Indianapolis Colts</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080clt.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>23</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >429</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >348</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080mia.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >524</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >268</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nor/2023.htm">New Orleans Saints</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080nwe.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right iz" data-stat="pts_lose" >0</td><td class="right " data-stat="yards_win" >304</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >156</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/rav/2023.htm">Baltimore Ravens</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080pit.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>17</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >289</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >335</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080crd.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >380</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >294</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080ram.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>23</strong></td><td class="right " data-stat="pts_lose" >14</td><td class="right " data-stat="yards_win" >454</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >249</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyj/2023.htm">New York Jets</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080den.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >21</td><td class="right " data-stat="yards_win" >407</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >308</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080min.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >333</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >329</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-08" >2023-10-08</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/dal/2023.htm">Dallas Cowboys</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310080sfo.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>42</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >421</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >197</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="5" >5</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-10-09" >2023-10-09</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310090rai.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>17</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >279</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >285</td><td class="right " data-stat="to_lose" >3</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-10-12" >2023-10-12</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310120kan.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>19</strong></td><td class="right " data-stat="pts_lose" >8</td><td class="right " data-stat="yards_win" >389</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >197</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >9:30AM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150oti.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >360</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >233</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150cle.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>19</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >334</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >215</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/was/2023.htm">Washington Commanders</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150atl.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >193</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >402</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150mia.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>42</strong></td><td class="right " data-stat="pts_lose" >21</td><td class="right " data-stat="yards_win" >424</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >296</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/min/2023.htm">Minnesota Vikings</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150chi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>19</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >220</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >275</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150cin.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>17</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >214</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >384</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150jax.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >233</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >354</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/htx/2023.htm">Houston Texans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150htx.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >297</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >430</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150rai.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >348</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >259</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/ram/2023.htm">Los Angeles Rams</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150ram.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>26</strong></td><td class="right " data-stat="pts_lose" >9</td><td class="right " data-stat="yards_win" >382</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >345</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150tam.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >380</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >251</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyj/2023.htm">New York Jets</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150nyj.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >14</td><td class="right " data-stat="yards_win" >244</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >348</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-15" >2023-10-15</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/buf/2023.htm">Buffalo Bills</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310150buf.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>14</strong></td><td class="right " data-stat="pts_lose" >9</td><td class="right " data-stat="yards_win" >297</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >317</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="6" >6</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-10-16" >2023-10-16</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310160sdg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >342</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >272</td><td class="right " data-stat="to_lose" >1</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-10-19" >2023-10-19</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310190nor.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >24</td><td class="right " data-stat="yards_win" >330</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >407</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220clt.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>39</strong></td><td class="right " data-stat="pts_lose" >38</td><td class="right " data-stat="yards_win" >316</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >456</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/atl/2023.htm">Atlanta Falcons</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220tam.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>16</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >401</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >329</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nwe/2023.htm">New England Patriots</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220nwe.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>29</strong></td><td class="right " data-stat="pts_lose" >25</td><td class="right " data-stat="yards_win" >364</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >339</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/chi/2023.htm">Chicago Bears</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220chi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >12</td><td class="right " data-stat="yards_win" >323</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >235</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/det/2023.htm">Detroit Lions</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220rav.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>38</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >503</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >337</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyg/2023.htm">New York Giants</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220nyg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>14</strong></td><td class="right " data-stat="pts_lose" >7</td><td class="right " data-stat="yards_win" >356</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >273</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220ram.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >300</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >354</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sea/2023.htm">Seattle Seahawks</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220sea.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >318</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >249</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/den/2023.htm">Denver Broncos</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220den.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>19</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >339</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >331</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220kan.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >483</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >358</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-22" >2023-10-22</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/mia/2023.htm">Miami Dolphins</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310220phi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >355</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >244</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="7" >7</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-10-23" >2023-10-23</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/min/2023.htm">Minnesota Vikings</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310230min.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>22</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >452</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >325</td><td class="right " data-stat="to_lose" >3</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-10-26" >2023-10-26</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/buf/2023.htm">Buffalo Bills</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310260buf.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >18</td><td class="right " data-stat="yards_win" >427</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >302</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/car/2023.htm">Carolina Panthers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290car.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>15</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >224</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >229</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290dal.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>43</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >387</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >280</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/min/2023.htm">Minnesota Vikings</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290gnb.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >346</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >270</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/oti/2023.htm">Tennessee Titans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290oti.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >23</td><td class="right " data-stat="yards_win" >375</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >342</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nor/2023.htm">New Orleans Saints</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290clt.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>38</strong></td><td class="right " data-stat="pts_lose" >27</td><td class="right " data-stat="yards_win" >511</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >371</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290pit.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >377</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >261</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290mia.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >390</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >218</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyj/2023.htm">New York Jets</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290nyg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>13</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >251</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >194</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290was.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>38</strong></td><td class="right " data-stat="pts_lose" >31</td><td class="right " data-stat="yards_win" >374</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >472</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sea/2023.htm">Seattle Seahawks</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/cle/2023.htm">Cleveland Browns</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290sea.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >362</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >385</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290sfo.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >400</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >460</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290crd.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >24</td><td class="right " data-stat="yards_win" >268</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >310</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/den/2023.htm">Denver Broncos</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290den.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >9</td><td class="right " data-stat="yards_win" >240</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >274</td><td class="right " data-stat="to_lose" >5</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-10-29" >2023-10-29</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310290sdg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >352</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >295</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="8" >8</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-10-30" >2023-10-30</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202310300det.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>26</strong></td><td class="right " data-stat="pts_lose" >14</td><td class="right " data-stat="yards_win" >486</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >157</td><td class="right " data-stat="to_lose" >1</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-11-02" >2023-11-02</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311020pit.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >326</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >340</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >9:30AM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/mia/2023.htm">Miami Dolphins</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050kan.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >14</td><td class="right " data-stat="yards_win" >267</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >292</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050cle.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right iz" data-stat="pts_lose" >0</td><td class="right " data-stat="yards_win" >326</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >58</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/gnb/2023.htm">Green Bay Packers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050gnb.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >391</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >187</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/htx/2023.htm">Houston Texans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050htx.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>39</strong></td><td class="right " data-stat="pts_lose" >37</td><td class="right " data-stat="yards_win" >496</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >332</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/min/2023.htm">Minnesota Vikings</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050atl.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >28</td><td class="right " data-stat="yards_win" >363</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >370</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nor/2023.htm">New Orleans Saints</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050nor.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >301</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >368</td><td class="right " data-stat="to_lose" >5</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/was/2023.htm">Washington Commanders</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050nwe.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >432</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >327</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050rav.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >515</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >151</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/clt/2023.htm">Indianapolis Colts</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050car.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >198</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >275</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/dal/2023.htm">Dallas Cowboys</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050phi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >23</td><td class="right " data-stat="yards_win" >292</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >406</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050rai.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >334</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >277</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-05" >2023-11-05</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311050cin.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >18</td><td class="right " data-stat="yards_win" >397</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >317</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="9" >9</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-11-06" >2023-11-06</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311060nyj.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >191</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >270</td><td class="right " data-stat="to_lose" >3</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-11-09" >2023-11-09</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/chi/2023.htm">Chicago Bears</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311090chi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>16</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >295</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >213</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >9:30AM</td><td class="left " data-stat="winner" ><strong><a href="/teams/clt/2023.htm">Indianapolis Colts</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120nwe.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>10</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >264</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >340</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/htx/2023.htm">Houston Texans</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120cin.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >27</td><td class="right " data-stat="yards_win" >544</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >380</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/rav/2023.htm">Baltimore Ravens</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120rav.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>33</strong></td><td class="right " data-stat="pts_lose" >31</td><td class="right " data-stat="yards_win" >373</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >306</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120pit.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>23</strong></td><td class="right " data-stat="pts_lose" >19</td><td class="right " data-stat="yards_win" >324</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >399</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120jax.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >3</td><td class="right " data-stat="yards_win" >437</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >221</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120tam.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >340</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >209</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/min/2023.htm">Minnesota Vikings</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120min.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >19</td><td class="right " data-stat="yards_win" >388</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >280</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120sdg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>41</strong></td><td class="right " data-stat="pts_lose" >38</td><td class="right " data-stat="yards_win" >533</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >421</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/crd/2023.htm">Arizona Cardinals</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120crd.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>25</strong></td><td class="right " data-stat="pts_lose" >23</td><td class="right " data-stat="yards_win" >352</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >254</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120dal.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>49</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >640</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >172</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sea/2023.htm">Seattle Seahawks</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120sea.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>29</strong></td><td class="right " data-stat="pts_lose" >26</td><td class="right " data-stat="yards_win" >489</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >356</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-12" >2023-11-12</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311120rai.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>16</strong></td><td class="right " data-stat="pts_lose" >12</td><td class="right " data-stat="yards_win" >274</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >365</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="10" >10</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-11-13" >2023-11-13</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/den/2023.htm">Denver Broncos</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311130buf.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >22</td><td class="right " data-stat="yards_win" >300</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >369</td><td class="right " data-stat="to_lose" >4</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-11-16" >2023-11-16</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311160rav.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >405</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >272</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190car.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>33</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >311</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >187</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190cle.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>13</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >259</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >249</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/gnb/2023.htm">Green Bay Packers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190gnb.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>23</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >397</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >394</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190jax.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >14</td><td class="right " data-stat="yards_win" >389</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >235</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190mia.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >422</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >296</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190det.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >26</td><td class="right " data-stat="yards_win" >338</td><td class="right " data-stat="to_win" >4</td><td class="right " data-stat="yards_lose" >334</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/htx/2023.htm">Houston Texans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190htx.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >419</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >319</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyg/2023.htm">New York Giants</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190was.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >19</td><td class="right " data-stat="yards_win" >292</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >404</td><td class="right " data-stat="to_lose" >6</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190sfo.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >14</td><td class="right " data-stat="yards_win" >420</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >287</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/ram/2023.htm">Los Angeles Rams</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190ram.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>17</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >267</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >291</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/buf/2023.htm">Buffalo Bills</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190buf.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>32</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >393</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >155</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-19" >2023-11-19</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/den/2023.htm">Denver Broncos</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311190den.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >295</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >385</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="11" >11</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-11-20" >2023-11-20</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311200kan.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >238</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >336</td><td class="right " data-stat="to_lose" >2</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-11-23" >2023-11-23</td><td class="right " data-stat="gametime" >12:30PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/gnb/2023.htm">Green Bay Packers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/det/2023.htm">Detroit Lions</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311230det.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>29</strong></td><td class="right " data-stat="pts_lose" >22</td><td class="right " data-stat="yards_win" >377</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >464</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-11-23" >2023-11-23</td><td class="right " data-stat="gametime" >4:30PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311230dal.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>45</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >431</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >376</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-11-23" >2023-11-23</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311230sea.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >377</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >220</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Fri</td><td class="left " data-stat="game_date" csk="2023-11-24" >2023-11-24</td><td class="right " data-stat="gametime" >3:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311240nyj.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >395</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >159</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/atl/2023.htm">Atlanta Falcons</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260atl.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >15</td><td class="right " data-stat="yards_win" >396</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >444</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/oti/2023.htm">Tennessee Titans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260oti.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>17</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >264</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >258</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260cin.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>16</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >421</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >222</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/clt/2023.htm">Indianapolis Colts</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260clt.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >394</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >298</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260htx.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >21</td><td class="right " data-stat="yards_win" >445</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >352</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyg/2023.htm">New York Giants</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260nyg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>10</strong></td><td class="right " data-stat="pts_lose" >7</td><td class="right " data-stat="yards_win" >220</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >283</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/den/2023.htm">Denver Broncos</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/cle/2023.htm">Cleveland Browns</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260den.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>29</strong></td><td class="right " data-stat="pts_lose" >12</td><td class="right " data-stat="yards_win" >294</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >269</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/ram/2023.htm">Los Angeles Rams</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260crd.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >14</td><td class="right " data-stat="yards_win" >457</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >292</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260rai.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >360</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >358</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260phi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >34</td><td class="right " data-stat="yards_win" >378</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >505</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-11-26" >2023-11-26</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311260sdg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >361</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >279</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="12" >12</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-11-27" >2023-11-27</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/chi/2023.htm">Chicago Bears</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311270min.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>12</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >317</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >242</td><td class="right " data-stat="to_lose" >4</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-11-30" >2023-11-30</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202311300dal.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>41</strong></td><td class="right " data-stat="pts_lose" >35</td><td class="right " data-stat="yards_win" >411</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >406</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/atl/2023.htm">Atlanta Falcons</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030nyj.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>13</strong></td><td class="right " data-stat="pts_lose" >8</td><td class="right " data-stat="yards_win" >194</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >259</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/clt/2023.htm">Indianapolis Colts</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030oti.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >28</td><td class="right " data-stat="yards_win" >355</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >381</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/htx/2023.htm">Houston Texans</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030htx.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>22</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >353</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >282</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030nor.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>33</strong></td><td class="right " data-stat="pts_lose" >28</td><td class="right " data-stat="yards_win" >347</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >362</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030was.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>45</strong></td><td class="right " data-stat="pts_lose" >15</td><td class="right " data-stat="yards_win" >406</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >245</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030nwe.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>6</strong></td><td class="right iz" data-stat="pts_lose" >0</td><td class="right " data-stat="yards_win" >241</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >257</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/crd/2023.htm">Arizona Cardinals</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030pit.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >282</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >317</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030tam.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >18</td><td class="right " data-stat="yards_win" >322</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >282</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/ram/2023.htm">Los Angeles Rams</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/cle/2023.htm">Cleveland Browns</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030ram.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>36</strong></td><td class="right " data-stat="pts_lose" >19</td><td class="right " data-stat="yards_win" >399</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >327</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030phi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>42</strong></td><td class="right " data-stat="pts_lose" >19</td><td class="right " data-stat="yards_win" >456</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >333</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-03" >2023-12-03</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/gnb/2023.htm">Green Bay Packers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312030gnb.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >19</td><td class="right " data-stat="yards_win" >382</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >337</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="13" >13</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-12-04" >2023-12-04</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312040jax.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >31</td><td class="right " data-stat="yards_win" >491</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >376</td><td class="right iz" data-stat="to_lose" >0</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-12-07" >2023-12-07</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nwe/2023.htm">New England Patriots</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312070pit.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>21</strong></td><td class="right " data-stat="pts_lose" >18</td><td class="right " data-stat="yards_win" >303</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >264</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100atl.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>29</strong></td><td class="right " data-stat="pts_lose" >25</td><td class="right " data-stat="yards_win" >290</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >434</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nor/2023.htm">New Orleans Saints</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100nor.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >207</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >303</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/chi/2023.htm">Chicago Bears</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/det/2023.htm">Detroit Lions</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100chi.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >336</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >267</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100cin.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >14</td><td class="right " data-stat="yards_win" >385</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >272</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100cle.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >27</td><td class="right " data-stat="yards_win" >389</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >293</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyj/2023.htm">New York Jets</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100nyj.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >347</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >135</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100rav.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>37</strong></td><td class="right " data-stat="pts_lose" >31</td><td class="right " data-stat="yards_win" >449</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >410</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/min/2023.htm">Minnesota Vikings</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100rai.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>3</strong></td><td class="right iz" data-stat="pts_lose" >0</td><td class="right " data-stat="yards_win" >231</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >202</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100sfo.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >527</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >324</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/buf/2023.htm">Buffalo Bills</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100kan.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >327</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >346</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/den/2023.htm">Denver Broncos</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100sdg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >7</td><td class="right " data-stat="yards_win" >322</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >283</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-10" >2023-12-10</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/dal/2023.htm">Dallas Cowboys</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312100dal.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>33</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >394</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >324</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-12-11" >2023-12-11</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nyg/2023.htm">New York Giants</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312110nyg.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >22</td><td class="right " data-stat="yards_win" >367</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >326</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="14" >14</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-12-11" >2023-12-11</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/oti/2023.htm">Tennessee Titans</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/mia/2023.htm">Miami Dolphins</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312110mia.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >27</td><td class="right " data-stat="yards_win" >403</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >366</td><td class="right " data-stat="to_lose" >1</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-12-14" >2023-12-14</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312140rai.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>63</strong></td><td class="right " data-stat="pts_lose" >21</td><td class="right " data-stat="yards_win" >378</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >326</td><td class="right " data-stat="to_lose" >5</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sat</td><td class="left " data-stat="game_date" csk="2023-12-16" >2023-12-16</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312160cin.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >24</td><td class="right " data-stat="yards_win" >378</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >424</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sat</td><td class="left " data-stat="game_date" csk="2023-12-16" >2023-12-16</td><td class="right " data-stat="gametime" >4:30PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/clt/2023.htm">Indianapolis Colts</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312160clt.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >13</td><td class="right " data-stat="yards_win" >372</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >216</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sat</td><td class="left " data-stat="game_date" csk="2023-12-16" >2023-12-16</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/det/2023.htm">Detroit Lions</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312160det.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>42</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >448</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >287</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/car/2023.htm">Carolina Panthers</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170car.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>9</strong></td><td class="right " data-stat="pts_lose" >7</td><td class="right " data-stat="yards_win" >283</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >204</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/cle/2023.htm">Cleveland Browns</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170cle.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >377</td><td class="right " data-stat="to_win" >3</td><td class="right " data-stat="yards_lose" >236</td><td class="right " data-stat="to_lose" >3</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170gnb.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>34</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >452</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >321</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/htx/2023.htm">Houston Texans</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170oti.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>19</strong></td><td class="right " data-stat="pts_lose" >16</td><td class="right " data-stat="yards_win" >340</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >204</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170nwe.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>27</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >326</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >206</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/mia/2023.htm">Miami Dolphins</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170mia.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right iz" data-stat="pts_lose" >0</td><td class="right " data-stat="yards_win" >290</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >103</td><td class="right " data-stat="to_lose" >4</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >1:00PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/nor/2023.htm">New Orleans Saints</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170nor.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>24</strong></td><td class="right " data-stat="pts_lose" >6</td><td class="right " data-stat="yards_win" >296</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >193</td><td class="right iz" data-stat="to_lose" >0</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170crd.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>45</strong></td><td class="right " data-stat="pts_lose" >29</td><td class="right " data-stat="yards_win" >406</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >436</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >4:05PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/ram/2023.htm">Los Angeles Rams</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170ram.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>28</strong></td><td class="right " data-stat="pts_lose" >20</td><td class="right " data-stat="yards_win" >445</td><td class="right " data-stat="to_win" >2</td><td class="right " data-stat="yards_lose" >297</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >4:25PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/buf/2023.htm">Buffalo Bills</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/dal/2023.htm">Dallas Cowboys</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170buf.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>31</strong></td><td class="right " data-stat="pts_lose" >10</td><td class="right " data-stat="yards_win" >351</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >195</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-17" >2023-12-17</td><td class="right " data-stat="gametime" >8:20PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/rav/2023.htm">Baltimore Ravens</a></strong></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312170jax.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>23</strong></td><td class="right " data-stat="pts_lose" >7</td><td class="right " data-stat="yards_win" >396</td><td class="right " data-stat="to_win" >1</td><td class="right " data-stat="yards_lose" >333</td><td class="right " data-stat="to_lose" >2</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="15" >15</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-12-18" >2023-12-18</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/sea/2023.htm">Seattle Seahawks</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312180sea.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>20</strong></td><td class="right " data-stat="pts_lose" >17</td><td class="right " data-stat="yards_win" >297</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >321</td><td class="right " data-stat="to_lose" >2</td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Winner/tie" data-stat="winner" class=" sort_default_asc center" >Winner/tie</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Loser/tie" data-stat="loser" class=" sort_default_asc center" >Loser/tie</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-12-21" >2023-12-21</td><td class="right " data-stat="gametime" >8:15PM</td><td class="left " data-stat="winner" ><strong><a href="/teams/ram/2023.htm">Los Angeles Rams</a></strong></td><td class="right iz" data-stat="game_location" ></td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312210ram.htm">boxscore</a></td><td class="right " data-stat="pts_win" ><strong>30</strong></td><td class="right " data-stat="pts_lose" >22</td><td class="right " data-stat="yards_win" >458</td><td class="right iz" data-stat="to_win" >0</td><td class="right " data-stat="yards_lose" >339</td><td class="right " data-stat="to_lose" >1</td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sat</td><td class="left " data-stat="game_date" csk="2023-12-23" >2023-12-23</td><td class="right " data-stat="gametime" csk="16:30:00" >4:30PM</td><td class="left " data-stat="winner" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312230pit.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sat</td><td class="left " data-stat="game_date" csk="2023-12-23" >2023-12-23</td><td class="right " data-stat="gametime" csk="20:00:00" >8:00PM</td><td class="left " data-stat="winner" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312230sdg.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/cle/2023.htm">Cleveland Browns</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240htx.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/det/2023.htm">Detroit Lions</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240min.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240car.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240oti.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240atl.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240nyj.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="16:05:00" >4:05PM</td><td class="left " data-stat="winner" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240tam.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="16:25:00" >4:25PM</td><td class="left " data-stat="winner" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240chi.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="16:25:00" >4:25PM</td><td class="left " data-stat="winner" ><a href="/teams/dal/2023.htm">Dallas Cowboys</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/mia/2023.htm">Miami Dolphins</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240mia.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-24" >2023-12-24</td><td class="right " data-stat="gametime" csk="20:15:00" >8:15PM</td><td class="left " data-stat="winner" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312240den.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-12-25" >2023-12-25</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312250kan.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-12-25" >2023-12-25</td><td class="right " data-stat="gametime" csk="16:30:00" >4:30PM</td><td class="left " data-stat="winner" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312250phi.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="16" >16</th><td class="left " data-stat="game_day_of_week" >Mon</td><td class="left " data-stat="game_date" csk="2023-12-25" >2023-12-25</td><td class="right " data-stat="gametime" csk="20:15:00" >8:15PM</td><td class="left " data-stat="winner" ><a href="/teams/rav/2023.htm">Baltimore Ravens</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312250sfo.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Visitor" data-stat="winner" class=" sort_default_asc center" >Visitor</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Home" data-stat="loser" class=" sort_default_asc center" >Home</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Thu</td><td class="left " data-stat="game_date" csk="2023-12-28" >2023-12-28</td><td class="right " data-stat="gametime" csk="20:15:00" >8:15PM</td><td class="left " data-stat="winner" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/cle/2023.htm">Cleveland Browns</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312280cle.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sat</td><td class="left " data-stat="game_date" csk="2023-12-30" >2023-12-30</td><td class="right " data-stat="gametime" csk="20:15:00" >8:15PM</td><td class="left " data-stat="winner" ><a href="/teams/det/2023.htm">Detroit Lions</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/dal/2023.htm">Dallas Cowboys</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312300dal.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310htx.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310clt.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310phi.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310jax.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310was.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310chi.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/mia/2023.htm">Miami Dolphins</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/rav/2023.htm">Baltimore Ravens</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310rav.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310nyg.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310tam.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310buf.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="16:05:00" >4:05PM</td><td class="left " data-stat="winner" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310sea.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="16:25:00" >4:25PM</td><td class="left " data-stat="winner" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310kan.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="16:25:00" >4:25PM</td><td class="left " data-stat="winner" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310den.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="17" >17</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2023-12-31" >2023-12-31</td><td class="right " data-stat="gametime" csk="20:20:00" >8:20PM</td><td class="left " data-stat="winner" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202312310min.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>


      <tr class="thead">
         <th aria-label="Week" data-stat="week_num" class=" sort_default_asc sorttable_nosort center" data-tip="Week number in season" >Week</th>
         <th aria-label="Day" data-stat="game_day_of_week" class=" sort_default_asc left" >Day</th>
         <th aria-label="Date" data-stat="game_date" class=" sort_default_asc center" >Date</th>
         <th aria-label="Time" data-stat="gametime" class=" sort_default_asc center" data-tip="Game Time, Eastern" >Time</th>
         <th aria-label="Visitor" data-stat="winner" class=" sort_default_asc center" >Visitor</th>
         <th aria-label="" data-stat="game_location" class=" sort_default_asc center" ></th>
         <th aria-label="Home" data-stat="loser" class=" sort_default_asc center" >Home</th>
         <th aria-label="" data-stat="boxscore_word" class=" sort_default_asc center" ></th>
         <th aria-label="PtsW" data-stat="pts_win" class=" center" data-tip="Points Scored by the winning team (first one listed)" >PtsW</th>
         <th aria-label="PtsL" data-stat="pts_lose" class=" center" data-tip="Points Scored by the losing team (second one listed)" >PtsL</th>
         <th aria-label="YdsW" data-stat="yards_win" class=" center" data-tip="Yards Gained by the winning team (first one listed)" >YdsW</th>
         <th aria-label="TOW" data-stat="to_win" class=" center" data-tip="Turnovers by the winning team (first one listed)" >TOW</th>
         <th aria-label="YdsL" data-stat="yards_lose" class=" center" data-tip="Yards Gained by the losing team (second one listed)" >YdsL</th>
         <th aria-label="TOL" data-stat="to_lose" class=" center" data-tip="Turnovers by the losing team (second one listed)" >TOL</th>
      </tr>
      <tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/ram/2023.htm">Los Angeles Rams</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sfo/2023.htm">San Francisco 49ers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070sfo.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/sea/2023.htm">Seattle Seahawks</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/crd/2023.htm">Arizona Cardinals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070crd.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/tam/2023.htm">Tampa Bay Buccaneers</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/car/2023.htm">Carolina Panthers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070car.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/kan/2023.htm">Kansas City Chiefs</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/sdg/2023.htm">Los Angeles Chargers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070sdg.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/pit/2023.htm">Pittsburgh Steelers</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/rav/2023.htm">Baltimore Ravens</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070rav.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/phi/2023.htm">Philadelphia Eagles</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nyg/2023.htm">New York Giants</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070nyg.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/nyj/2023.htm">New York Jets</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nwe/2023.htm">New England Patriots</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070nwe.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/min/2023.htm">Minnesota Vikings</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/det/2023.htm">Detroit Lions</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070det.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/jax/2023.htm">Jacksonville Jaguars</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/oti/2023.htm">Tennessee Titans</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070oti.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/htx/2023.htm">Houston Texans</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/clt/2023.htm">Indianapolis Colts</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070clt.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/den/2023.htm">Denver Broncos</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/rai/2023.htm">Las Vegas Raiders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070rai.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/dal/2023.htm">Dallas Cowboys</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/was/2023.htm">Washington Commanders</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070was.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/cle/2023.htm">Cleveland Browns</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/cin/2023.htm">Cincinnati Bengals</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070cin.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/chi/2023.htm">Chicago Bears</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/gnb/2023.htm">Green Bay Packers</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070gnb.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/buf/2023.htm">Buffalo Bills</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/mia/2023.htm">Miami Dolphins</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070mia.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>
<tr ><th scope="row" class="right " data-stat="week_num" csk="18" >18</th><td class="left " data-stat="game_day_of_week" >Sun</td><td class="left " data-stat="game_date" csk="2024-01-07" >2024-01-07</td><td class="right " data-stat="gametime" csk="13:00:00" >1:00PM</td><td class="left " data-stat="winner" ><a href="/teams/atl/2023.htm">Atlanta Falcons</a></td><td class="right " data-stat="game_location" >@</td><td class="left " data-stat="loser" ><a href="/teams/nor/2023.htm">New Orleans Saints</a></td><td class="center " data-stat="boxscore_word" ><a href="/boxscores/202401070nor.htm">preview</a></td><td class="right iz" data-stat="pts_win" ></td><td class="right iz" data-stat="pts_lose" ></td><td class="right iz" data-stat="yards_win" ></td><td class="right iz" data-stat="to_win" ></td><td class="right iz" data-stat="yards_lose" ></td><td class="right iz" data-stat="to_lose" ></td></tr>

</table>


</div>

<div class="placeholder"></div>

</div>







<!-- global.nonempty_tables_num: 1, table_count: 1 -->
   <!-- no Local/Partials/NoteBottom.tt2 -->
<div id="bottom_nav" class="section_wrapper">
<div class="section_heading"><span data-no-inpage="1" class="section_anchor" id="inner_nav_bottom_link" data-label="More 2023 NFL Pages"></span><h2>More 2023 NFL Pages</h2></div>
<div class="section_content" id="bottom_nav_container">

  <p><a href="/years/2023/">2023 NFL Season</a></p>
  <p class="listhead">Standard Player Stats</p>
        <ul class="">
          <li><a href="/years/2023/passing.htm">Passing</a></li>
          <li><a href="/years/2023/rushing.htm">Rushing</a></li>
          <li><a href="/years/2023/receiving.htm">Receiving</a></li>
          <li><a href="/years/2023/scrimmage.htm">Scrimmage Stats</a></li>
          <li><a href="/years/2023/defense.htm">Defense</a></li>
          <li><a href="/years/2023/kicking.htm">Kicking</a></li>
          <li><a href="/years/2023/punting.htm">Punting</a></li>
          <li><a href="/years/2023/returns.htm">Kick &amp; Punt Returns</a></li>
          <li><a href="/years/2023/scoring.htm">Scoring</a></li>
        </ul><p class="listhead">Fantasy Player Stats</p>
        <ul class="">
          <li><a href="/years/2023/fantasy.htm">Player Fantasy Ranks</a></li>
          <li><a href="/years/2023/redzone-passing.htm">Red Zone Passing</a></li>
          <li><a href="/years/2023/redzone-rushing.htm">Red Zone Rushing</a></li>
          <li><a href="/years/2023/redzone-receiving.htm">Red Zone Receiving</a></li>
        </ul><p class="listhead">Defense vs. Pos</p>
        <ul class="">
          <li><a href="/years/2023/fantasy-points-against-RB.htm">RB</a></li>
          <li><a href="/years/2023/fantasy-points-against-TE.htm">TE</a></li>
          <li><a href="/years/2023/fantasy-points-against-QB.htm">QB</a></li>
          <li><a href="/years/2023/fantasy-points-against-WR.htm">WR</a></li>
        </ul><p class="listhead">Weeks</p>
        <ul class="">
          <li><a href="/years/2023/week_1.htm">Week 1</a></li>
          <li><a href="/years/2023/week_2.htm">Week 2</a></li>
          <li><a href="/years/2023/week_3.htm">Week 3</a></li>
          <li><a href="/years/2023/week_4.htm">Week 4</a></li>
          <li><a href="/years/2023/week_5.htm">Week 5</a></li>
          <li><a href="/years/2023/week_6.htm">Week 6</a></li>
          <li><a href="/years/2023/week_7.htm">Week 7</a></li>
          <li><a href="/years/2023/week_8.htm">Week 8</a></li>
          <li><a href="/years/2023/week_9.htm">Week 9</a></li>
          <li><a href="/years/2023/week_10.htm">Week 10</a></li>
          <li><a href="/years/2023/week_11.htm">Week 11</a></li>
          <li><a href="/years/2023/week_12.htm">Week 12</a></li>
          <li><a href="/years/2023/week_13.htm">Week 13</a></li>
          <li><a href="/years/2023/week_14.htm">Week 14</a></li>
          <li><a href="/years/2023/week_15.htm">Week 15</a></li>
          <li><a href="/years/2023/week_16.htm">Week 16</a></li>
          <li><a href="/years/2023/week_17.htm">Week 17</a></li>
          <li><a href="/years/2023/week_18.htm">Week 18</a></li>
        </ul><p class="listhead">Awards</p>
        <ul class="">
          <li><a href="/years/2023/allpro.htm">AllPro</a></li>
          <li><a href="/years/2023/probowl.htm">Pro&nbsp;Bowl</a></li>
          <li><a href="/awards/awards_2023.htm">Awards Voting</a></li>
        </ul>
        <ul class="">
          <li><a href="/years/2023/opp.htm">Team Defense</a></li>
          <li><a href="/years/2023/leaders.htm">Leaders</a></li>
          <li><a href="/years/2023/games.htm">Schedule</a></li>
          <li><a href="/years/2023/coaches.htm">Coaches</a></li>
          <li><a href="/years/2023/draft.htm">Draft</a></li>
          <li><a href="https://www.sports-reference.com/cfb/years/2023.html">College Football</a></li>
          <li><a href="/years/2023/advanced.htm">Advanced Stats</a></li>
          <li><a href="/years/2023/penalties.htm">Penalties</a></li>
          <li><a href="/years/2023/ol_penalties.htm">O-Line Penalties</a></li>
          <li><a href="/years/2023/training-camps.htm">Training Camps</a></li>
          <li><a href="/years/2023/deaths.htm">Deaths</a></li>
          <li><a href="/years/2023/debuts.htm">Debuts</a></li>
          <li><a href="/years/2023/attendance.htm">Attendance</a></li>
          <li><a href="/years/2023/preseason.htm">Preseason</a></li>
          <li><a href="/years/2023/preseason_odds.htm">Preseason Odds</a></li>
          <li><a href="/years/2023/splits.htm">Splits</a></li>
        </ul><p class="listhead">Transactions</p>
        <ul class="">
          <li><a href="/years/2023/01_transactions.htm">January</a></li>
          <li><a href="/years/2023/02_transactions.htm">February</a></li>
          <li><a href="/years/2023/03_transactions.htm">March</a></li>
          <li><a href="/years/2023/04_transactions.htm">April</a></li>
          <li><a href="/years/2023/05_transactions.htm">May</a></li>
          <li><a href="/years/2023/06_transactions.htm">June</a></li>
          <li><a href="/years/2023/07_transactions.htm">July</a></li>
          <li><a href="/years/2023/08_transactions.htm">August</a></li>
          <li><a href="/years/2023/09_transactions.htm">September</a></li>
          <li><a href="/years/2023/10_transactions.htm">October</a></li>
          <li><a href="/years/2023/11_transactions.htm">November</a></li>
          <li><a href="/years/2023/12_transactions.htm">December</a></li>
        </ul></div></div>




<!-- fs_footer -->
<div class="adblock">
<!-- div#fs_fs_footer  -->
<div align="center" id="div-gpt-ad-728x90-Footer"  data-freestar-ad="__300x250 __970x90">
    <script data-cfasync="false" type='text/javascript'>
    if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {
    }
    else {
        console.log('push ad:div-gpt-ad-728x90-Footer');
        freestar.queue.push(function() { googletag.display('div-gpt-ad-728x90-Footer'); });
    }
    </script>
</div>
<!-- /div.#fs_fs_footer -->

</div>





</div><!-- div#content -->


<div id="footer" role="contentinfo">
	<div id="footer_header">
		 <ul class="bullets-inline"><li class="user logged_in">Welcome <span class="username"></span>&nbsp;&#183;&nbsp;<a href="https://stathead.com/profile/?utm_source=pfr&amp;utm_medium=sr_xsite&amp;utm_campaign=2023_01_srnav_account">Your Account</a></li>
<li class="user logged_in"><a class="logout" onclick="sr_auth_logout_page_elements();if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/profile/?do=logout">Logout</a></li>
<li class="user not_logged_in"><a class="login" onclick="if(!this.href.match('redirect_uri')){this.href += '&redirect_uri='+escape(document.location.href)}" href="https://stathead.com/users/login.cgi?token=1">Ad-Free Login</a></li>
<li class="user not_logged_in"><a href="https://stathead.com/users/signup.cgi">Create Account</a></li>
</ul>
		 <div class="breadcrumbs">You are here: <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="/"><span itemprop="name">PFR Home Page</span></a> <meta itemprop="position" content="1" /></span> &gt; <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="/years/"><span itemprop="name">All Years</span></a> <meta itemprop="position" content="2" /></span> &gt; <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="/years/2023/"><span itemprop="name">2023 NFL</span></a> <meta itemprop="position" content="3" /></span> &gt; <strong>Schedule</strong></div>
	</div><!-- div#footer_header -->

	<div id="footer_general">
		<div id="site_menu" role="navigation" aria-label="complete site index">


<div class="section_heading assoc_site_menu" id="site_menu_sh">
  <span class="section_anchor" id="site_menu_link" data-label="Full Site Menu"></span><h2>Full Site Menu</h2>    <div class="section_heading_text">
      <ul><li><a data-scroll href="#header">Return to Top</a></li>
      </ul>
    </div>

</div>

				    <ul>
	<li><a href="/players">Players</a>
	    <div>In the News: <a title="Brock Purdy" href="/players/P/PurdBr00.htm">Brock Purdy</a>, <a title="Christian McCaffrey" href="/players/M/McCaCh01.htm">Christian McCaffrey</a>, <a title="Justin Fields" href="/players/F/FielJu00.htm">Justin Fields</a>, <a title="Baker Mayfield" href="/players/M/MayfBa00.htm">Baker Mayfield</a>, <a title="Kyler Murray" href="/players/M/MurrKy00.htm">Kyler Murray</a>, <a title="Patrick Mahomes" href="/players/M/MahoPa00.htm">Patrick Mahomes</a> <a href="/players/">...</a></div>
	<div>Popular: <a title="Tom Brady" href="/players/B/BradTo00.htm">Tom Brady</a>, <a title="Cam Newton" href="/players/N/NewtCa00.htm">Cam Newton</a>, <a title="Aaron Donald" href="/players/D/DonaAa00.htm">Aaron Donald</a>, <a title="Russell Wilson" href="/players/W/WilsRu00.htm">Russell Wilson</a>, <a title="Aaron Rodgers" href="/players/R/RodgAa00.htm">Aaron Rodgers</a>, <a title="Odell Beckham" href="/players/B/BeckOd00.htm">Odell Beckham Jr.</a>, <a title="J.J. Watt" href="/players/W/WattJ.00.htm">J.J. Watt</a>, <a title="Peyton Manning" href="/players/M/MannPe00.htm">Peyton Manning</a>, <a title="Patrick Mahomes" href="/players/M/MahoPa00.htm">Patrick Mahomes</a>, <a title="Julio Jones" href="/players/J/JoneJu02.htm">Julio Jones</a>, <a title="Antonio Brown" href="/players/B/BrowAn04.htm">Antonio Brown</a>, <a title="Ben Roethlisberger" href="/players/R/RoetBe00.htm">Ben Roethlisberger</a>, <a title="Drew Brees" href="/players/B/BreeDr00.htm">Drew Brees</a>, <a title="Todd Gurley" href="/players/G/GurlTo01.htm">Todd Gurley</a> <a href="/players/">...</a></div>

	<div><a href="/hof/">Hall of Famers</a>, <a href="/probowl/">Pro Bowlers</a>, <a href="/awards/ap-nfl-mvp-award.htm">MVPs</a>, <a href="/friv/linkify.cgi">Player Linker Tool</a> ...</div>
	</li>

	<li><a href="/teams/">Teams</a>
	<div>AFC East: <a href="/teams/mia/2023.htm">Dolphins</a>, <a href="/teams/buf/2023.htm">Bills</a>, <a href="/teams/nyj/2023.htm">Jets</a>, <a href="/teams/nwe/2023.htm">Patriots</a></div>
<div>AFC North: <a href="/teams/rav/2023.htm">Ravens</a>, <a href="/teams/cle/2023.htm">Browns</a>, <a href="/teams/cin/2023.htm">Bengals</a>, <a href="/teams/pit/2023.htm">Steelers</a></div>
<div>AFC South: <a href="/teams/htx/2023.htm">Texans</a>, <a href="/teams/jax/2023.htm">Jaguars</a>, <a href="/teams/clt/2023.htm">Colts</a>, <a href="/teams/oti/2023.htm">Titans</a></div>
<div>AFC West: <a href="/teams/kan/2023.htm">Chiefs</a>, <a href="/teams/den/2023.htm">Broncos</a>, <a href="/teams/rai/2023.htm">Raiders</a>, <a href="/teams/sdg/2023.htm">Chargers</a></div>
<div>NFC East: <a href="/teams/dal/2023.htm">Cowboys</a>, <a href="/teams/phi/2023.htm">Eagles</a>, <a href="/teams/nyg/2023.htm">Giants</a>, <a href="/teams/was/2023.htm">Commanders</a></div>
<div>NFC North: <a href="/teams/det/2023.htm">Lions</a>, <a href="/teams/min/2023.htm">Vikings</a>, <a href="/teams/gnb/2023.htm">Packers</a>, <a href="/teams/chi/2023.htm">Bears</a></div>
<div>NFC South: <a href="/teams/tam/2023.htm">Buccaneers</a>, <a href="/teams/nor/2023.htm">Saints</a>, <a href="/teams/atl/2023.htm">Falcons</a>, <a href="/teams/car/2023.htm">Panthers</a></div>
<div>NFC West: <a href="/teams/sfo/2023.htm">49ers</a>, <a href="/teams/ram/2023.htm">Rams</a>, <a href="/teams/sea/2023.htm">Seahawks</a>, <a href="/teams/crd/2023.htm">Cardinals</a></div>

	</li>

	<li><a href="/years/">Seasons</a>
	<div><a href="/years/2023/">Current Season</a>, <a href="/years/2023/games.htm">Current Season Schedule</a>, <a href="/years/2023/leaders.htm">Current Leaders</a></div><div><a href="/years/2022/">2022</a>, <a href="/years/2021/">2021</a>, <a href="/years/2020/">2020</a>, <a href="/years/2019/">2019</a>, <a href="/years/2018/">2018</a>, <a href="/years/">...</a></div>
	</li>

	<li><a href="/leaders/">NFL Leaders</a>
	<div><a href="/leaders/pass_yds_career.htm">Career Passing Yards</a>, <a href="/leaders/rush_td_single_season.htm">Single Season Rush TD</a>, <a href="/leaders/sacks_single_game.htm">Single Game Sacks</a> ...</div>
	</li>

	<li><a href="/boxscores/">NFL Scores</a>
	<div><a href="/boxscores/game-scores.htm">All-time Scores</a>, <a href="/boxscores/game_scores_find.cgi">Find a Score</a> ...</div>
	</li>

	<li><a href="/draft/">NFL Draft</a>
	<div><a href="/years/2023/draft.htm">2023 Draft</a>, <a href="/draft/">Draft History</a> ...</div>
	</li>

	<li>
		<a target='_blank' rel='noopener' href="https://stathead.com/football/?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Stathead</a>
		<div><strong>Player Finders</strong>: 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player-season-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Season Finder</a>, 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player-game-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Game Finder</a>, 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player-streak-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Streak Finder</a>,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player-span-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Span Finder</a>,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/player_split_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Split Finder</a>
		</div>
		<div><strong>Team Finders</strong>: 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/team-season-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Season Finder</a>, 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/team-game-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Game Finder</a>, 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/team-streak-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Streak Finder</a>,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/team-span-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Span Finder</a>,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/split_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Split Finder</a>
		</div>
		<div><strong>Other Finders</strong>: 
		<a target='_blank' rel='noopener' href="https://stathead.com/football/versus-finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Versus Finder</a>,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/ptd_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Touchdown Finder</a>,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/fg_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Field Goal Finder</a>,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/play_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Game Play Finder</a>,
		<a target='_blank' rel='noopener' href="https://stathead.com/football/drive_finder.cgi?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footernav_stathead">Drive Finder</a>
		</div>
	</li>

	<li><a href="/super-bowl/">Super Bowl Winners</a>
	<div><a href="/super-bowl/leaders.htm">Super Bowl Leaders</a>, <a href="/super-bowl/standings.htm">Super Bowl Standings</a> ...</div>
	</li>

	<li><a href="/schools/">Schools</a>
	<div><a href="/schools/">All Player Colleges</a>, <a href="/schools/high_schools.cgi">High Schools</a> ...</div>
	</li>

	<li><a href="/coaches/">NFL Coaches</a>
	<div>Active Coaches: <a href="/coaches/BeliBi0.htm">Bill Belichick</a>, <a href="/coaches/ReidAn0.htm">Andy Reid</a>, <a href="/coaches/TomlMi0.htm">Mike Tomlin</a>, <a href="/coaches/CarrPe0.htm">Pete Carroll</a> ...</div><div>Historical Coaches: <a href="/coaches/ShulDo0.htm">Don Shula</a>, <a href="/coaches/HalaGe0.htm">George Halas</a>, <a href="/coaches/LandTo0.htm">Tom Landry</a>, <a href="/coaches/LambCu0.htm">Curly Lambeau</a> ...</div>
	</li>

	<li><a href="/executives/">Executives</a>
	<div><a href="/executives/AdamBu0.htm">Bud Adams</a>, <a href="/executives/PiolSc0.htm">Scott Pioli</a>, <a href="/executives/HalaGe0.htm">George Halas</a> ...</div>
	</li>

	<li><a href="/officials/">NFL Officials</a>
	<div><a href="/officials/HochEd0r.htm">Ed Hochuli</a>, <a href="/officials/SterTo0r.htm">Tony Steratore</a>, <a href="/officials/McAuTe0r.htm">Terry McAulay</a> ...</div>
	</li>

	<li><a href="/fantasy/">Fantasy Football Stats</a>
	<div><a href="/fantasy/QB-fantasy-matchups.htm">Current Fantasy Matchups</a>, <a href="/years/2023/fantasy-points-against-QB.htm">Fantasy Points Allowed</a> ...</div>
	</li>
	<li><a href="/stadiums/">Stadiums</a>
	<div><a href="/stadiums/GNB00.htm">Lambeau Field</a>, <a href="/stadiums/NOR00.htm">Superdome</a>, <a href="/stadiums/SFO00.htm">Candlestick Park</a> ...</div>
	</li>

	<li><a href="/awards/">NFL Awards</a>
	<div><a href="/hof/">Pro Football Hall of Fame</a>, <a href="/awards/ap-nfl-mvp-award.htm">AP NFL MVP</a>, <a href="/probowl/">Pro Bowl</a> ...</div>
	</li>

	<li><a href="/friv/">Frivolities</a>
	<div><a href="/friv/players-who-played-for-multiple-teams-franchises.fcgi">Players who played for multiple teams</a>, <a href="/linker">Player Linker Tool</a>, <a href="/friv/birthdays.cgi">Birthdays</a>, <a href="/players/uniform.cgi">Uniform Numbers</a> ...</div>
	</li>

  <li><a href="/about/">About</a>
    <div><a href="/about/glossary.htm">Glossary</a>, <a href="/about/minimums.htm">Stat Minimums</a>, <a href="/about/nfl-football-faqs.html">Frequently Asked Questions about the NFL and Football</a> ...</div>
  </li>

  <li><a href="https://www.immaculategrid.com/football/?utm_campaign=2023_07_lnk_home_footer_ig&utm_source=pfr&utm_medium=sr_xsite">Immaculate Grid</a>
    <div>Put your football knowledge to the test with our daily football trivia game. Can you complete the grid?</div>
  <li>

  <li><a href="
	</ul>




      <ul>
       <li></li>      
       <li><a href="https://www.pro-football-reference.com/pfr-blog/">Pro-Football-Reference.com Blog and Articles</a></li>

	        </div><!-- div#site_menu -->
		<div>
			<div id="social" class="icon_group noload">

<div class="section_heading assoc_" id="_sh">
  <span class="section_anchor" id="_link" data-label="We're Social...for Statheads" data-no-inpage="1"></span><h2>We're Social...for Statheads</h2>		
</div>
	<a href="tel://888-512-8907" data-tip="Call us on Telephone" data-label="Telephone" aria-label="Telephone" class="poptip"><svg class="icon phone"><use xlink:href="#ic-phone"></use></svg></a>
	<a href="//www.sports-reference.com/blog/" data-tip="The Sports Reference Blog" data-label="Our Blog" aria-label="Our Blog" class="poptip"><svg class="icon wordpress"><use xlink:href="#ic-wordpress"></use></svg></a>
	<a href="https://www.sports-reference.com/blog/feed/" data-tip="Our Blog's RSS Feed" data-label="RSS Feed" aria-label="RSS Feed" class="poptip"><svg class="icon rss"><use xlink:href="#ic-rss"></use></svg></a>
		<a href="https://www.facebook.com/Pro.Football.Reference" data-tip="Pro-Football-Reference.com at Facebook" data-label="Facebook" aria-label="Facebook" class="poptip"><svg class="icon facebook"><use xlink:href="#ic-facebook"></use></svg></a>
		<a href="https://twitter.com/pfref" data-tip="Pro-Football-Reference.com at Twitter" data-label="Twitter" aria-label="Twitter" class="poptip"><svg class="icon twitter"><use xlink:href="#ic-twitter"></use></svg></a>
		<a href="https://instagram.com/profootballreference" data-tip="Pro-Football-Reference.com at Instagram" data-label="Instagram" aria-label="Instagram" class="poptip"><svg class="icon instagram"><use xlink:href="#ic-instagram"></use></svg></a>
		<a href="https://www.tiktok.com/@profootballreference" data-tip="Pro-Football-Reference.com at TikTok" data-label="TikTok" aria-label="TikTok" class="poptip"><svg class="icon tiktok"><use xlink:href="#ic-tiktok"></use></svg></a>
	<a href="https://reddit.com/r/SportsReference" data-tip="Reddit/r/SportsReference" data-label="Reddit/r/SR" aria-label="Reddit/r/SR" class="poptip"><svg class="icon reddit"><use xlink:href="#ic-reddit"></use></svg></a>
	<a href="https://www.youtube.com/user/sportsreference" data-tip="YouTube/SportsReference" data-label="YouTube" aria-label="YouTube" class="poptip"><svg class="icon youtube"><use xlink:href="#ic-youtube"></use></svg></a>
	<a href="https://www.linkedin.com/company/sports-reference-llc" data-tip="Follow SR on LinkedIn" data-label="LinkedIn" aria-label="LinkedIn" class="poptip"><svg class="icon linkedin"><use xlink:href="#ic-linkedin"></use></svg></a>
	<a href="https://www.paypal.me/sportsref" data-tip="Send us money via PayPal" data-label="PayPal" aria-label="PayPal" class="poptip"><svg class="icon paypal"><use xlink:href="#ic-paypal"></use></svg></a>

<p>Every <a href="https://www.sports-reference.com/blog/sports-reference-social-media/">Sports Reference Social Media Account</a></p>
<p><strong>Site Last Updated:</strong> Friday, December 22,  2:32PM
</p>
<p><a href="https://www.sports-reference.com/feedback/" class="button" style="display: block">Question, Comment, Feedback, or Correction?</a></p>

<p><a style="display: block" href="https://www.pro-football-reference.com/email" class="button">Subscribe to our Free Email Newsletter</a></p>


<p><a style="background-color:#7e3e89; color: #fff;" href="https://stathead.com/sport/football/?utm_medium=sr_xsite&utm_source=pfr&utm_campaign=2023_01_footerbttn_stathead" class="button alt">Subscribe to Stathead Football: Get your first month FREE<br><em>Your All-Access Ticket to the Pro Football Reference Database</em></a></p>


<p><a href="https://www.sports-reference.com/blog/ways-sports-reference-can-help-your-website/?utm_medium=sr&utm_source=pfr&utm_campaign=site-footer-ways-help">Do you have a sports website? Or write about sports? We have tools and resources that can help you use sports data.  Find out more.</a></p>


</div><!-- div#social -->

			<div id="tips_tricks">

<div class="section_heading assoc_tips" id="tips_sh">
  <span class="section_anchor" id="tips_link" data-label="FAQs, Tip &amp; Tricks" data-no-inpage="1"></span><h2>FAQs, Tip &amp; Tricks</h2>		
</div>
   <ul>
<li>Learn about the <a href="https://www.pro-football-reference.com/blog/index37a8.html">Approximate Value Formula</a></li>
<li>Details on the Pro Football Reference <a href="https://www.pro-football-reference.com/about/win_prob.htm">Win Probability</a></li>


           <li><a href="//www.sports-reference.com/blog/category/tips-and-tricks/">Tips and Tricks from our Blog.</a></li>
           <li><a href="/linker/">Do you have a blog? Join our linker program.</a></li>
	   <li><a href="https://www.sports-reference.com/blog/category/stathead-tutorial-series/">Watch our How-To Videos to Become a Stathead</a></li>
	   <li><a href="//stathead.com/?ref=pfr">Subscribe to Stathead and get access to more data than you can imagine</a></li>
   </ul>
</div><!-- div#tips_tricks -->

			<div id="credits">
				<p>All logos are the trademark &amp; property of their owners and not Sports Reference LLC.  We present them here for purely educational purposes.
				<a href="https://www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">Our reasoning for presenting offensive logos.</a></p>
				<p>

					Logos were compiled by the amazing <a href="http://sportslogos.net/">SportsLogos.net.</a>
				</p>

<div class="notice">
<p>Data Provided By
	<a href="https://www.sportradar.com/" rel="nofollow"><img alt="SportRadar" border=0 width=275 src="https://cdn.ssref.net/req/202311303/images/klecko/sportradar.png"  style="background-color:#666; padding:.5em; border-radius:.25em"></a>
	</p>


</div>

     <p>Copyright &copy; 2000-2023 <a href="//www.sports-reference.com/">Sports Reference LLC</a>. All rights reserved.</p>

     <p>The SPORTS REFERENCE and STATHEAD trademarks are owned exclusively by Sports Reference LLC. Use without license or authorization is expressly prohibited.
<p>Please see our <a href="https://www.pro-football-reference.com/about/sources.htm">Contributors and Sources page</a> for data source details.</p>

			</div><!-- div#credits -->
		</div>
	</div>


<ul id="site_dirs" class="notranslate bullets-inline">
	<li><a href="https://www.sports-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer"><svg height="15px" width="20px"><use xlink:href="#ic-sr-pennant"></use></svg> Sports&nbsp;Reference&#8239;&reg;</a></li>
	<li><a href="https://www.baseball-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Baseball</a></li>
	<li class="current"><a href="https://www.pro-football-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Football</a> <a href="https://www.sports-reference.com/cfb/">(college)</a></li>
	<li><a href="https://www.basketball-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Basketball</a> <a href="https://www.sports-reference.com/cbb/">(college)</a></li>
	<li><a href="https://www.hockey-reference.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Hockey</a></li>





	<li><a href="https://fbref.com/de/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Fußball</a></li>

	<li><a href="https://www.sports-reference.com/blog/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Blog</a></li>
    <li><a href="https://stathead.com/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Stathead&#8239;&reg;</a></li>

	<li><a href="https://www.immaculategrid.com/football/?utm_source=pfr&utm_medium=sr_xsite&utm_campaign=2023_01_srnav_footer">Immaculate Grid</a></li>



</ul>

	<div id="about">
  <a href="//www.sports-reference.com/about.html">About</a> &bull;
  <a href="//www.sports-reference.com/termsofuse.html">Conditions &amp; Terms of Service</a> &bull;
  <a href="//www.sports-reference.com/advertise.html">Advertise With Us</a>
 &bull;
  <a href="//www.sports-reference.com/jobs.html">Jobs at SR</a>
  <br><br>
Sports Reference Purpose: We will be the trusted source of information and tools that inspire and empower users to enjoy, understand, and share the sports they love.
  <br><br>
  <a href="//www.sports-reference.com/privacy.html">Privacy Policy</a> &bull;
  <a href="//www.sports-reference.com/gambling-revenue-policy.html">Gambling Revenue Policy</a> &bull;
  <a href="//www.sports-reference.com/accessibility-policy.html">Accessibility Policy</a> &bull;
  <a href="//www.sports-reference.com/data_use.html">Use of Data</a>
  </div>
  <!-- div#about -->
</div><!-- div#footer -->

</div><!-- div#wrap -->
<!-- yes sticky url:  https://www.pro-football-reference.com/years/2023/games.htm -->
<div id="fs-select-footer"></div>




<!-- rails -->

<div class="adblock rails  left"><!-- div#fs_fs_rails_left  -->
<div align="center" id="div-gpt-ad-160x600-1"  data-freestar-ad="">
    <script data-cfasync="false" type='text/javascript'>
    if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {
    }
    else {
        console.log('push ad:div-gpt-ad-160x600-1');
        freestar.queue.push(function() { googletag.display('div-gpt-ad-160x600-1'); });
    }
    </script>
</div>
<!-- /div.#fs_fs_rails_left -->
</div>
<div class="adblock rails right"><!-- div#fs_fs_rails_right  -->
<div align="center" id="div-gpt-ad-160x600-2"  data-freestar-ad="">
    <script data-cfasync="false" type='text/javascript'>
    if (sr_detect_ie || sr_detect_edge || Modernizr.adfree) {
    }
    else {
        console.log('push ad:div-gpt-ad-160x600-2');
        freestar.queue.push(function() { googletag.display('div-gpt-ad-160x600-2'); });
    }
    </script>
</div>
<!-- /div.#fs_fs_rails_right -->
</div>


<!-- sr_gender is used in Templates/Assets/GoogleAnalytics.tt2 -->
<script>var sr_gender = "";</script>
<!-- Google Analytics -->
<!-- Google Analytics UA,  UA-1890630-3 -->
<!-- Google Analytics GA4, G-EMBDG7RM0K -->
<!-- Google Tag Manager --> <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-MC36NL2');</script> <!-- End Google Tag Manager --> <!-- Google Tag Manager (noscript) --> <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MC36NL2" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript> <!-- End Google Tag Manager (noscript) -->
<script> var sr_cookie = vjs_readCookie('stathead_user') || ''; var sr_cookie_split = sr_cookie.split("::"); var sr_session_key = (sr_cookie_split.length > 1)?sr_cookie_split[2]:''; var sr_ad_free_key = "3"; var sr_site_id = "pfr"; var sr_is_subscriber = (sr_ad_free_key && sr_session_key.vjs_isMatch(new RegExp(sr_ad_free_key + "$"))) || sr_session_key.vjs_isMatch(/1$/) || (sr_site_id === 'stathead' && sr_session_key.vjs_isMatch(/[0-7]$/)); var sr_is_user = sr_cookie !== null && sr_cookie !== ''; var sr_seen_modal = vjs_readCookie('modal_ad') !== null; var sr_device = 'unk'; if (Modernizr.phone) { sr_device = 'phone'; } else if (Modernizr.tablet) { sr_device = 'tablet'; } else if (Modernizr.laptop) { sr_device = 'laptop'; } else if (Modernizr.desktop) { sr_device = 'desktop'; } var sr_stathead_site = vjs_readCookie('stathead_site') || ''; var sr_stathead_type = vjs_readCookie('stathead_type') || ''; window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); /* GA4: individual site code config, do not send a page view (double counts) */ gtag('config', 'G-EMBDG7RM0K', { 'is_sub': sr_is_subscriber, 'is_user': sr_is_user, 'page_gender': typeof(sr_gender) === 'string'? sr_gender: null, 'stathead_type': sr_stathead_type, 'stathead_site': sr_stathead_site, 'viewport_width': Modernizr.viewport_width, send_page_view: false }); /* GA4: all sr sites together */ /* I believe linker works as a parameter here, although there didn\'t seem to be a simple "true" value to set besides this one --NW https://developers.google.com/analytics/devguides/collection/gtagjs/cross-domain Add configs for both sets of code. */ gtag('config', 'G-80FRT7VJ60', { 'linker': { 'domains' : ['stathead.com'] }, 'is_sub': sr_is_subscriber, 'is_user': sr_is_user, 'page_gender': typeof(sr_gender) === 'string'? sr_gender: null, 'stathead_type': sr_stathead_type, 'stathead_site': sr_stathead_site, 'viewport_width': Modernizr.viewport_width }); </script>
<!-- End Google Analytics -->

<!-- Start of HubSpot Embed Code -->
<script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/20503178.js"></script>
<!-- End of HubSpot Embed Code -->

</body>
<!-- SR -->
</html>


"""
