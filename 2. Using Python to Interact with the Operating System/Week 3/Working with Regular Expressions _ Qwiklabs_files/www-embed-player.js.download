(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var n;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ba="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)};
function ca(a){a=["object"==typeof globalThis&&globalThis,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global,a];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var da=ca(this);function ea(){ea=function(){};
da.Symbol||(da.Symbol=fa)}
function ha(a,b){this.f=a;ba(this,"description",{configurable:!0,writable:!0,value:b})}
ha.prototype.toString=function(){return this.f};
var fa=function(){function a(c){if(this instanceof a)throw new TypeError("Symbol is not a constructor");return new ha("jscomp_symbol_"+(c||"")+"_"+b++,c)}
var b=0;return a}();
function ia(){ea();var a=da.Symbol.iterator;a||(a=da.Symbol.iterator=da.Symbol("Symbol.iterator"));"function"!=typeof Array.prototype[a]&&ba(Array.prototype,a,{configurable:!0,writable:!0,value:function(){return ja(aa(this))}});
ia=function(){}}
function ja(a){ia();a={next:a};a[da.Symbol.iterator]=function(){return this};
return a}
function q(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}}
function ka(a){for(var b,c=[];!(b=a.next()).done;)c.push(b.value);return c}
var la="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ma;
if("function"==typeof Object.setPrototypeOf)ma=Object.setPrototypeOf;else{var oa;a:{var pa={a:!0},qa={};try{qa.__proto__=pa;oa=qa.a;break a}catch(a){}oa=!1}ma=oa?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var ra=ma;
function t(a,b){a.prototype=la(b.prototype);a.prototype.constructor=a;if(ra)ra(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.L=b.prototype}
function u(a,b){if(b){for(var c=da,d=a.split("."),e=0;e<d.length-1;e++){var f=d[e];f in c||(c[f]={});c=c[f]}d=d[d.length-1];e=c[d];f=b(e);f!=e&&null!=f&&ba(c,d,{configurable:!0,writable:!0,value:f})}}
function sa(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
u("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=sa(this,b,"endsWith");b+="";void 0===c&&(c=d.length);for(var e=Math.max(0,Math.min(c|0,d.length)),f=b.length;0<f&&0<e;)if(d[--e]!=b[--f])return!1;return 0>=f}});
u("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=sa(this,b,"startsWith");b+="";for(var e=d.length,f=b.length,g=Math.max(0,Math.min(c|0,d.length)),h=0;h<f&&g<e;)if(d[g++]!=b[h++])return!1;return h>=f}});
function w(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var ta="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)w(d,e)&&(a[e]=d[e])}return a};
u("Object.assign",function(a){return a||ta});
u("WeakMap",function(a){function b(k){this.f=(h+=Math.random()+1).toString();if(k){k=q(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!w(k,g)){var l=new c;ba(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(m){if(m instanceof c)return m;e(m);return l(m)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),m=new a([[k,2],[l,3]]);if(2!=m.get(k)||3!=m.get(l))return!1;m["delete"](k);m.set(l,4);return!m.has(k)&&4==m.get(l)}catch(p){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!w(k,g))throw Error("WeakMap key fail: "+k);k[g][this.f]=l;return this};
b.prototype.get=function(k){return d(k)&&w(k,g)?k[g][this.f]:void 0};
b.prototype.has=function(k){return d(k)&&w(k,g)&&w(k[g],this.f)};
b.prototype["delete"]=function(k){return d(k)&&w(k,g)&&w(k[g],this.f)?delete k[g][this.f]:!1};
return b});
u("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h.f;return ja(function(){if(l){for(;l.head!=h.f;)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var m=h.g[l];if(m&&w(h.g,l))for(var p=0;p<m.length;p++){var v=m[p];if(k!==k&&v.key!==v.key||k===v.key)return{id:l,list:m,index:p,u:v}}return{id:l,list:m,index:-1,u:void 0}}
function e(h){this.g={};this.f=b();this.size=0;if(h){h=q(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(q([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),m=l.next();if(m.done||m.value[0]!=h||"s"!=m.value[1])return!1;m=l.next();return m.done||4!=m.value[0].x||"t"!=m.value[1]||!l.next().done?!1:!0}catch(p){return!1}}())return a;
ia();var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this.g[l.id]=[]);l.u?l.u.value=k:(l.u={next:this.f,previous:this.f.previous,head:this.f,key:h,value:k},l.list.push(l.u),this.f.previous.next=l.u,this.f.previous=l.u,this.size++);return this};
e.prototype["delete"]=function(h){h=d(this,h);return h.u&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.g[h.id],h.u.previous.next=h.u.next,h.u.next.previous=h.u.previous,h.u.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.g={};this.f=this.f.previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).u};
e.prototype.get=function(h){return(h=d(this,h).u)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),m;!(m=l.next()).done;)m=m.value,h.call(k,m[1],m[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
u("Set",function(a){function b(c){this.f=new Map;if(c){c=q(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.f.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(q([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
ia();b.prototype.add=function(c){c=0===c?0:c;this.f.set(c,c);this.size=this.f.size;return this};
b.prototype["delete"]=function(c){c=this.f["delete"](c);this.size=this.f.size;return c};
b.prototype.clear=function(){this.f.clear();this.size=0};
b.prototype.has=function(c){return this.f.has(c)};
b.prototype.entries=function(){return this.f.entries()};
b.prototype.values=function(){return this.f.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.f.forEach(function(f){return c.call(d,f,f,e)})};
return b});
u("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)w(b,d)&&c.push([d,b[d]]);return c}});
u("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==sa(this,b,"includes").indexOf(b,c||0)}});
u("Promise",function(a){function b(g){this.g=0;this.h=void 0;this.f=[];var h=this.i();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.f=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.g=function(g){if(null==this.f){this.f=[];var h=this;this.h(function(){h.j()})}this.f.push(g)};
var e=da.setTimeout;c.prototype.h=function(g){e(g,0)};
c.prototype.j=function(){for(;this.f&&this.f.length;){var g=this.f;this.f=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.i(l)}}}this.f=null};
c.prototype.i=function(g){this.h(function(){throw g;})};
b.prototype.i=function(){function g(l){return function(m){k||(k=!0,l.call(h,m))}}
var h=this,k=!1;return{resolve:g(this.A),reject:g(this.j)}};
b.prototype.A=function(g){if(g===this)this.j(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.D(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.w(g):this.l(g)}};
b.prototype.w=function(g){var h=void 0;try{h=g.then}catch(k){this.j(k);return}"function"==typeof h?this.F(h,g):this.l(g)};
b.prototype.j=function(g){this.m(2,g)};
b.prototype.l=function(g){this.m(1,g)};
b.prototype.m=function(g,h){if(0!=this.g)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.g);this.g=g;this.h=h;this.B()};
b.prototype.B=function(){if(null!=this.f){for(var g=0;g<this.f.length;++g)f.g(this.f[g]);this.f=null}};
var f=new c;b.prototype.D=function(g){var h=this.i();g.aa(h.resolve,h.reject)};
b.prototype.F=function(g,h){var k=this.i();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(v,r){return"function"==typeof v?function(B){try{l(v(B))}catch(K){m(K)}}:r}
var l,m,p=new b(function(v,r){l=v;m=r});
this.aa(k(g,l),k(h,m));return p};
b.prototype["catch"]=function(g){return this.then(void 0,g)};
b.prototype.aa=function(g,h){function k(){switch(l.g){case 1:g(l.h);break;case 2:h(l.h);break;default:throw Error("Unexpected state: "+l.g);}}
var l=this;null==this.f?f.g(k):this.f.push(k)};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=q(g),m=l.next();!m.done;m=l.next())d(m.value).aa(h,k)})};
b.all=function(g){var h=q(g),k=h.next();return k.done?d([]):new b(function(l,m){function p(B){return function(K){v[B]=K;r--;0==r&&l(v)}}
var v=[],r=0;do v.push(void 0),r++,d(k.value).aa(p(v.length-1),m),k=h.next();while(!k.done)})};
return b});
var ua=function(){function a(){function c(){}
new c;Reflect.construct(c,[],function(){});
return new c instanceof c}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(c,d,e){c=b(c,d);e&&Reflect.setPrototypeOf(c,e.prototype);return c}}return function(c,d,e){void 0===e&&(e=c);
e=la(e.prototype||Object.prototype);return Function.prototype.apply.call(c,e,d)||e}}();
u("Reflect.construct",function(){return ua});
var x=this||self;function y(a,b,c){a=a.split(".");c=c||x;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
var va=/^[\w+/_-]+[=]{0,2}$/,wa=null;function z(a,b){for(var c=a.split("."),d=b||x,e=0;e<c.length;e++)if(d=d[c[e]],null==d)return null;return d}
function xa(){}
function ya(a){a.ia=void 0;a.getInstance=function(){return a.ia?a.ia:a.ia=new a}}
function za(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function Aa(a){return"array"==za(a)}
function Ba(a){var b=za(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Ca(a){return"function"==za(a)}
function Da(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Ea(a){return Object.prototype.hasOwnProperty.call(a,Fa)&&a[Fa]||(a[Fa]=++Ga)}
var Fa="closure_uid_"+(1E9*Math.random()>>>0),Ga=0;function Ha(a,b,c){return a.call.apply(a.bind,arguments)}
function Ia(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function A(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?A=Ha:A=Ia;return A.apply(null,arguments)}
function Ka(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
var C=Date.now||function(){return+new Date};
function La(a,b){y(a,b,void 0)}
function D(a,b){function c(){}
c.prototype=b.prototype;a.L=b.prototype;a.prototype=new c;a.prototype.constructor=a}
;function Ma(a,b){if(!a||/[?&]dsh=1(&|$)/.test(a))return null;if(/[?&]ae=1(&|$)/.test(a)){var c=/[?&]adurl=([^&]+)/.exec(a);if(!c)return null;var d=b?c.index:a.length;try{return{xa:a.slice(0,d)+"&act=1"+a.slice(d),za:decodeURIComponent(c[1])}}catch(f){return null}}if(/[?&]ae=2(&|$)/.test(a)){c=a;d="";if(b){var e=a.indexOf("&adurl=");0<e&&(c=a.slice(0,e),d=a.slice(e))}return{xa:c+"&act=1"+d,za:c+"&dct=1"+d}}return null}
;function E(a){if(Error.captureStackTrace)Error.captureStackTrace(this,E);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
D(E,Error);E.prototype.name="CustomError";var Na=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},F=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Oa=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f="string"===typeof a?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},Pa=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},Qa=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
F(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function Ra(a,b){a:{var c=a.length;for(var d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:"string"===typeof a?a.charAt(c):a[c]}
function Sa(a,b){var c=Na(a,b);0<=c&&Array.prototype.splice.call(a,c,1)}
function Ta(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function Ua(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Ba(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function Va(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;function Wa(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function Xa(a,b){var c=Ba(b),d=c?b:arguments;for(c=c?0:1;c<d.length;c++){if(null==a)return;a=a[d[c]]}return a}
function Ya(a){var b=Za,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function $a(a){for(var b in a)return!1;return!0}
function ab(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function bb(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function cb(a){var b={},c;for(c in a)b[c]=a[c];return b}
function db(a){var b=za(a);if("object"==b||"array"==b){if(Ca(a.clone))return a.clone();b="array"==b?[]:{};for(var c in a)b[c]=db(a[c]);return b}return a}
var eb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function fb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<eb.length;f++)c=eb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;function gb(a,b){this.f=a===hb&&b||"";this.g=ib}
gb.prototype.J=!0;gb.prototype.I=function(){return this.f};
function jb(){var a=kb;return a instanceof gb&&a.constructor===gb&&a.g===ib?a.f:"type_error:Const"}
var ib={},hb={},kb=new gb(hb,"");function lb(a,b){this.f=a===mb&&b||"";this.g=nb}
lb.prototype.J=!0;lb.prototype.I=function(){return this.f.toString()};
lb.prototype.ha=!0;lb.prototype.ea=function(){return 1};
function ob(a){if(a instanceof lb&&a.constructor===lb&&a.g===nb)return a.f;za(a);return"type_error:TrustedResourceUrl"}
var nb={},mb={};var pb=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
function qb(a,b){if(b)a=a.replace(rb,"&amp;").replace(sb,"&lt;").replace(tb,"&gt;").replace(ub,"&quot;").replace(vb,"&#39;").replace(wb,"&#0;");else{if(!xb.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(rb,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(sb,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(tb,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(ub,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace(vb,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(wb,"&#0;"))}return a}
var rb=/&/g,sb=/</g,tb=/>/g,ub=/"/g,vb=/'/g,wb=/\x00/g,xb=/[\x00&<>"']/;function G(a,b){this.f=a===yb&&b||"";this.g=zb}
G.prototype.J=!0;G.prototype.I=function(){return this.f.toString()};
G.prototype.ha=!0;G.prototype.ea=function(){return 1};
function Ab(a){if(a instanceof G&&a.constructor===G&&a.g===zb)return a.f;za(a);return"type_error:SafeUrl"}
var Bb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function Cb(a){if(a instanceof G)return a;a="object"==typeof a&&a.J?a.I():String(a);Bb.test(a)||(a="about:invalid#zClosurez");return new G(yb,a)}
var zb={},yb={};var Db;a:{var Eb=x.navigator;if(Eb){var Fb=Eb.userAgent;if(Fb){Db=Fb;break a}}Db=""}function H(a){return-1!=Db.indexOf(a)}
;function Gb(){this.f="";this.h=Hb;this.g=null}
Gb.prototype.ha=!0;Gb.prototype.ea=function(){return this.g};
Gb.prototype.J=!0;Gb.prototype.I=function(){return this.f.toString()};
function Ib(a){if(a instanceof Gb&&a.constructor===Gb&&a.h===Hb)return a.f;za(a);return"type_error:SafeHtml"}
var Hb={};function Jb(a,b){var c=new Gb;c.f=a;c.g=b;return c}
Jb("<!DOCTYPE html>",0);var Lb=Jb("",0);Jb("<br>",0);function Mb(a,b){var c=b instanceof G?b:Cb(b);a.href=Ab(c)}
function Nb(a,b){a.src=ob(b);if(null===wa)b:{var c=x.document;if((c=c.querySelector&&c.querySelector("script[nonce]"))&&(c=c.nonce||c.getAttribute("nonce"))&&va.test(c)){wa=c;break b}wa=""}c=wa;c&&a.setAttribute("nonce",c)}
;function Ob(a){return a=qb(a,void 0)}
function Pb(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var Qb=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^\\/?#]*)@)?([^\\/?#]*?)(?::([0-9]+))?(?=[\\/?#]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function I(a){return a?decodeURI(a):a}
function J(a,b){return b.match(Qb)[a]||null}
function Rb(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)Rb(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function Sb(a){var b=[],c;for(c in a)Rb(c,a[c],b);return b.join("&")}
function Tb(a,b){var c=Sb(b);if(c){var d=a.indexOf("#");0>d&&(d=a.length);var e=a.indexOf("?");if(0>e||e>d){e=d;var f=""}else f=a.substring(e+1,d);d=[a.substr(0,e),f,a.substr(d)];e=d[1];d[1]=c?e?e+"&"+c:c:e;c=d[0]+(d[1]?"?"+d[1]:"")+d[2]}else c=a;return c}
var Ub=/#|$/;function Vb(a,b){var c=a.search(Ub);a:{var d=0;for(var e=b.length;0<=(d=a.indexOf(b,d))&&d<c;){var f=a.charCodeAt(d-1);if(38==f||63==f)if(f=a.charCodeAt(d+e),!f||61==f||38==f||35==f)break a;d+=e+1}d=-1}if(0>d)return null;e=a.indexOf("&",d);if(0>e||e>c)e=c;d+=b.length+1;return decodeURIComponent(a.substr(d,e-d).replace(/\+/g," "))}
;function Wb(a){var b=a.url,c=a.ub;this.j=!!a.xb;this.g=Ma(b,c);a=/[?&]dsh=1(&|$)/.test(b);this.h=!a&&/[?&]ae=1(&|$)/.test(b);this.i=!a&&/[?&]ae=2(&|$)/.test(b);this.f=/[?&]adurl=([^&]*)/.exec(b)}
;var Xb=H("Opera"),Yb=H("Trident")||H("MSIE"),Zb=H("Edge"),$b=H("Gecko")&&!(-1!=Db.toLowerCase().indexOf("webkit")&&!H("Edge"))&&!(H("Trident")||H("MSIE"))&&!H("Edge"),ac=-1!=Db.toLowerCase().indexOf("webkit")&&!H("Edge");function bc(){var a=x.document;return a?a.documentMode:void 0}
var cc;a:{var dc="",ec=function(){var a=Db;if($b)return/rv:([^\);]+)(\)|;)/.exec(a);if(Zb)return/Edge\/([\d\.]+)/.exec(a);if(Yb)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(ac)return/WebKit\/(\S+)/.exec(a);if(Xb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
ec&&(dc=ec?ec[1]:"");if(Yb){var fc=bc();if(null!=fc&&fc>parseFloat(dc)){cc=String(fc);break a}}cc=dc}var gc=cc,hc;if(x.document&&Yb){var ic=bc();hc=ic?ic:parseInt(gc,10)||void 0}else hc=void 0;var jc=hc;var kc={},lc=null;var L=window;function mc(a){var b=z("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(f){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||x.$googDebugFname||b}catch(f){e="Not available",c=!0}return!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name?a:(b=a.message,null==b&&(a.constructor&&
a.constructor instanceof Function?(a.constructor.name?b=a.constructor.name:(b=a.constructor,nc[b]?b=nc[b]:(b=String(b),nc[b]||(c=/function\s+([^\(]+)/m.exec(b),nc[b]=c?c[1]:"[Anonymous]"),b=nc[b])),b='Unknown Error of type "'+b+'"'):b="Unknown Error of unknown type"),{message:b,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:a.stack||"Not available"})}
var nc={};function oc(a){this.f=a||{cookie:""}}
n=oc.prototype;n.isEnabled=function(){return navigator.cookieEnabled};
n.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.wb;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.ma}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);c=f?";domain="+f:"";g=g?";path="+g:"";d=d?";secure":"";h=0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(C()+1E3*h)).toUTCString();this.f.cookie=a+"="+b+c+g+h+d+(null!=e?";samesite="+e:
"")};
n.get=function(a,b){for(var c=a+"=",d=(this.f.cookie||"").split(";"),e=0,f;e<d.length;e++){f=pb(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
n.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{ma:0,path:b,domain:c});return d};
n.isEmpty=function(){return!this.f.cookie};
n.clear=function(){for(var a=(this.f.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=pb(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var pc=new oc("undefined"==typeof document?null:document);var qc=!Yb||9<=Number(jc);function rc(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
n=rc.prototype;n.clone=function(){return new rc(this.x,this.y)};
n.equals=function(a){return a instanceof rc&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
n.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
n.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
n.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function sc(a,b){this.width=a;this.height=b}
n=sc.prototype;n.clone=function(){return new sc(this.width,this.height)};
n.aspectRatio=function(){return this.width/this.height};
n.isEmpty=function(){return!(this.width*this.height)};
n.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
n.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
n.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function tc(a){var b=document;return"string"===typeof a?b.getElementById(a):a}
function uc(a,b){Wa(b,function(c,d){c&&"object"==typeof c&&c.J&&(c=c.I());"style"==d?a.style.cssText=c:"class"==d?a.className=c:"for"==d?a.htmlFor=c:vc.hasOwnProperty(d)?a.setAttribute(vc[d],c):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,c):a[d]=c})}
var vc={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
function wc(a,b,c){var d=arguments,e=document,f=String(d[0]),g=d[1];if(!qc&&g&&(g.name||g.type)){f=["<",f];g.name&&f.push(' name="',Ob(g.name),'"');if(g.type){f.push(' type="',Ob(g.type),'"');var h={};fb(h,g);delete h.type;g=h}f.push(">");f=f.join("")}f=xc(e,f);g&&("string"===typeof g?f.className=g:Array.isArray(g)?f.className=g.join(" "):uc(f,g));2<d.length&&yc(e,f,d);return f}
function yc(a,b,c){function d(g){g&&b.appendChild("string"===typeof g?a.createTextNode(g):g)}
for(var e=2;e<c.length;e++){var f=c[e];!Ba(f)||Da(f)&&0<f.nodeType?d(f):F(zc(f)?Ta(f):f,d)}}
function xc(a,b){b=String(b);"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)}
function zc(a){if(a&&"number"==typeof a.length){if(Da(a))return"function"==typeof a.item||"string"==typeof a.item;if(Ca(a))return"function"==typeof a.item}return!1}
function Ac(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Bc(a){Cc();return new lb(mb,a)}
var Cc=xa;function Dc(a){var b=Ec;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a.call(void 0,b[c],c,b)}
function Fc(){var a=[];Dc(function(b){a.push(b)});
return a}
var Ec={bb:"allow-forms",cb:"allow-modals",eb:"allow-orientation-lock",fb:"allow-pointer-lock",gb:"allow-popups",hb:"allow-popups-to-escape-sandbox",ib:"allow-presentation",jb:"allow-same-origin",kb:"allow-scripts",lb:"allow-top-navigation",mb:"allow-top-navigation-by-user-activation"},Gc=Va(function(){return Fc()});
function Hc(){var a=xc(document,"IFRAME"),b={};F(Gc(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
;function M(){this.g=this.g;this.B=this.B}
M.prototype.g=!1;M.prototype.dispose=function(){this.g||(this.g=!0,this.o())};
function Ic(a,b){a.g?b():(a.B||(a.B=[]),a.B.push(b))}
M.prototype.o=function(){if(this.B)for(;this.B.length;)this.B.shift()()};
function Jc(a){a&&"function"==typeof a.dispose&&a.dispose()}
function Kc(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];Ba(d)?Kc.apply(null,d):Jc(d)}}
;/*
 Copyright (c) Microsoft Corporation. All rights reserved.
 Licensed under the Apache License, Version 2.0 (the "License"); you may not use
 this file except in compliance with the License. You may obtain a copy of the
 License at http://www.apache.org/licenses/LICENSE-2.0

 THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED
 WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
 MERCHANTABLITY OR NON-INFRINGEMENT.

 See the Apache Version 2.0 License for specific language governing permissions
 and limitations under the License.
*/
function Lc(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var Mc=(new Date).getTime();function Oc(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));a=a.substring(0,a.indexOf("://"));if("http"!==a&&"https"!==a&&"chrome-extension"!==a&&"file"!==a&&"android-app"!==a&&"chrome-search"!==a&&"chrome-untrusted"!==a&&"app"!==a)throw Error("Invalid URI scheme in origin: "+a);c="";var d=b.indexOf(":");
if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===a&&"80"!==e||"https"===a&&"443"!==e)c=":"+e}return a+"://"+b+c}
;function Pc(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;m=l=0}
function b(p){for(var v=g,r=0;64>r;r+=4)v[r/4]=p[r]<<24|p[r+1]<<16|p[r+2]<<8|p[r+3];for(r=16;80>r;r++)p=v[r-3]^v[r-8]^v[r-14]^v[r-16],v[r]=(p<<1|p>>>31)&4294967295;p=e[0];var B=e[1],K=e[2],na=e[3],Nc=e[4];for(r=0;80>r;r++){if(40>r)if(20>r){var Ja=na^B&(K^na);var Kb=1518500249}else Ja=B^K^na,Kb=1859775393;else 60>r?(Ja=B&K|na&(B|K),Kb=2400959708):(Ja=B^K^na,Kb=3395469782);Ja=((p<<5|p>>>27)&4294967295)+Ja+Nc+Kb+v[r]&4294967295;Nc=na;na=K;K=(B<<30|B>>>2)&4294967295;B=p;p=Ja}e[0]=e[0]+p&4294967295;e[1]=
e[1]+B&4294967295;e[2]=e[2]+K&4294967295;e[3]=e[3]+na&4294967295;e[4]=e[4]+Nc&4294967295}
function c(p,v){if("string"===typeof p){p=unescape(encodeURIComponent(p));for(var r=[],B=0,K=p.length;B<K;++B)r.push(p.charCodeAt(B));p=r}v||(v=p.length);r=0;if(0==l)for(;r+64<v;)b(p.slice(r,r+64)),r+=64,m+=64;for(;r<v;)if(f[l++]=p[r++],m++,64==l)for(l=0,b(f);r+64<v;)b(p.slice(r,r+64)),r+=64,m+=64}
function d(){var p=[],v=8*m;56>l?c(h,56-l):c(h,64-(l-56));for(var r=63;56<=r;r--)f[r]=v&255,v>>>=8;b(f);for(r=v=0;5>r;r++)for(var B=24;0<=B;B-=8)p[v++]=e[r]>>B&255;return p}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,m;a();return{reset:a,update:c,digest:d,ya:function(){for(var p=d(),v="",r=0;r<p.length;r++)v+="0123456789ABCDEF".charAt(Math.floor(p[r]/16))+"0123456789ABCDEF".charAt(p[r]%16);return v}}}
;function Qc(a,b,c){var d=[],e=[];if(1==(Aa(c)?2:1))return e=[b,a],F(d,function(h){e.push(h)}),Rc(e.join(" "));
var f=[],g=[];F(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];F(d,function(h){e.push(h)});
a=Rc(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function Rc(a){var b=Pc();b.update(a);return b.ya().toLowerCase()}
;function Sc(a){var b=Oc(String(x.location.href)),c;(c=x.__SAPISID||x.__APISID||x.__OVERRIDE_SID)?c=!0:(c=new oc(document),c=c.get("SAPISID")||c.get("APISID")||c.get("__Secure-3PAPISID")||c.get("SID"),c=!!c);if(c&&(c=(b=0==b.indexOf("https:")||0==b.indexOf("chrome-extension:"))?x.__SAPISID:x.__APISID,c||(c=new oc(document),c=c.get(b?"SAPISID":"APISID")||c.get("__Secure-3PAPISID")),c)){b=b?"SAPISIDHASH":"APISIDHASH";var d=String(x.location.href);return d&&c&&b?[b,Qc(Oc(d),c,a||null)].join(" "):null}return null}
;function Tc(){this.g=[];this.f=-1}
Tc.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&0===a%1&&this.g[a]!=b&&(this.g[a]=b,this.f=-1)};
Tc.prototype.get=function(a){return!!this.g[a]};
function Uc(a){-1==a.f&&(a.f=Qa(a.g,function(b,c,d){return c?b+Math.pow(2,d):b},0));
return a.f}
;function Vc(a,b){this.h=a;this.i=b;this.g=0;this.f=null}
Vc.prototype.get=function(){if(0<this.g){this.g--;var a=this.f;this.f=a.next;a.next=null}else a=this.h();return a};
function Wc(a,b){a.i(b);100>a.g&&(a.g++,b.next=a.f,a.f=b)}
;function Xc(a){x.setTimeout(function(){throw a;},0)}
var Yc;
function Zc(){var a=x.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!H("Presto")&&(a=function(){var e=xc(document,"IFRAME");e.style.display="none";e.src=ob(new lb(mb,jb())).toString();document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.write(Ib(Lb));e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=A(function(k){if(("*"==h||
k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!H("Trident")&&!H("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.la;c.la=null;e()}};
return function(e){d.next={la:e};d=d.next;b.port2.postMessage(0)}}return function(e){x.setTimeout(e,0)}}
;function $c(){this.g=this.f=null}
var bd=new Vc(function(){return new ad},function(a){a.reset()});
$c.prototype.add=function(a,b){var c=bd.get();c.set(a,b);this.g?this.g.next=c:this.f=c;this.g=c};
$c.prototype.remove=function(){var a=null;this.f&&(a=this.f,this.f=this.f.next,this.f||(this.g=null),a.next=null);return a};
function ad(){this.next=this.scope=this.f=null}
ad.prototype.set=function(a,b){this.f=a;this.scope=b;this.next=null};
ad.prototype.reset=function(){this.next=this.scope=this.f=null};function cd(a,b){dd||ed();fd||(dd(),fd=!0);gd.add(a,b)}
var dd;function ed(){if(x.Promise&&x.Promise.resolve){var a=x.Promise.resolve(void 0);dd=function(){a.then(hd)}}else dd=function(){var b=hd;
!Ca(x.setImmediate)||x.Window&&x.Window.prototype&&!H("Edge")&&x.Window.prototype.setImmediate==x.setImmediate?(Yc||(Yc=Zc()),Yc(b)):x.setImmediate(b)}}
var fd=!1,gd=new $c;function hd(){for(var a;a=gd.remove();){try{a.f.call(a.scope)}catch(b){Xc(b)}Wc(bd,a)}fd=!1}
;function id(){this.g=-1}
;function jd(){this.g=64;this.f=[];this.l=[];this.m=[];this.i=[];this.i[0]=128;for(var a=1;a<this.g;++a)this.i[a]=0;this.j=this.h=0;this.reset()}
D(jd,id);jd.prototype.reset=function(){this.f[0]=1732584193;this.f[1]=4023233417;this.f[2]=2562383102;this.f[3]=271733878;this.f[4]=3285377520;this.j=this.h=0};
function kd(a,b,c){c||(c=0);var d=a.m;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.f[0];c=a.f[1];var g=a.f[2],h=a.f[3],k=a.f[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.f[0]=a.f[0]+b&4294967295;a.f[1]=a.f[1]+c&4294967295;a.f[2]=a.f[2]+g&4294967295;a.f[3]=a.f[3]+h&4294967295;a.f[4]=a.f[4]+k&4294967295}
jd.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.g,d=0,e=this.l,f=this.h;d<b;){if(0==f)for(;d<=c;)kd(this,a,d),d+=this.g;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.g){kd(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.g){kd(this,e);f=0;break}}this.h=f;this.j+=b}};
jd.prototype.digest=function(){var a=[],b=8*this.j;56>this.h?this.update(this.i,56-this.h):this.update(this.i,this.g-(this.h-56));for(var c=this.g-1;56<=c;c--)this.l[c]=b&255,b/=256;kd(this,this.l);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.f[c]>>d&255,++b;return a};function ld(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}
function md(a,b){"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function nd(a,b){if(a.classList)var c=a.classList.contains(b);else c=a.classList?a.classList:ld(a).match(/\S+/g)||[],c=0<=Na(c,b);return c}
function od(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):nd(a,"inverted-hdpi")&&md(a,Oa(a.classList?a.classList:ld(a).match(/\S+/g)||[],function(b){return"inverted-hdpi"!=b}).join(" "))}
;var pd="StopIteration"in x?x.StopIteration:{message:"StopIteration",stack:""};function qd(){}
qd.prototype.next=function(){throw pd;};
qd.prototype.G=function(){return this};
function rd(a){if(a instanceof qd)return a;if("function"==typeof a.G)return a.G(!1);if(Ba(a)){var b=0,c=new qd;c.next=function(){for(;;){if(b>=a.length)throw pd;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function sd(a,b){if(Ba(a))try{F(a,b,void 0)}catch(c){if(c!==pd)throw c;}else{a=rd(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==pd)throw c;}}}
function td(a){if(Ba(a))return Ta(a);a=rd(a);var b=[];sd(a,function(c){b.push(c)});
return b}
;function ud(a,b){this.h={};this.f=[];this.H=this.g=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof ud)for(c=vd(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function vd(a){wd(a);return a.f.concat()}
n=ud.prototype;n.equals=function(a,b){if(this===a)return!0;if(this.g!=a.g)return!1;var c=b||xd;wd(this);for(var d,e=0;d=this.f[e];e++)if(!c(this.get(d),a.get(d)))return!1;return!0};
function xd(a,b){return a===b}
n.isEmpty=function(){return 0==this.g};
n.clear=function(){this.h={};this.H=this.g=this.f.length=0};
n.remove=function(a){return Object.prototype.hasOwnProperty.call(this.h,a)?(delete this.h[a],this.g--,this.H++,this.f.length>2*this.g&&wd(this),!0):!1};
function wd(a){if(a.g!=a.f.length){for(var b=0,c=0;b<a.f.length;){var d=a.f[b];Object.prototype.hasOwnProperty.call(a.h,d)&&(a.f[c++]=d);b++}a.f.length=c}if(a.g!=a.f.length){var e={};for(c=b=0;b<a.f.length;)d=a.f[b],Object.prototype.hasOwnProperty.call(e,d)||(a.f[c++]=d,e[d]=1),b++;a.f.length=c}}
n.get=function(a,b){return Object.prototype.hasOwnProperty.call(this.h,a)?this.h[a]:b};
n.set=function(a,b){Object.prototype.hasOwnProperty.call(this.h,a)||(this.g++,this.f.push(a),this.H++);this.h[a]=b};
n.forEach=function(a,b){for(var c=vd(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
n.clone=function(){return new ud(this)};
n.G=function(a){wd(this);var b=0,c=this.H,d=this,e=new qd;e.next=function(){if(c!=d.H)throw Error("The map has changed since the iterator was created");if(b>=d.f.length)throw pd;var f=d.f[b++];return a?f:d.h[f]};
return e};function yd(a){var b=[];zd(new Ad,a,b);return b.join("")}
function Ad(){}
function zd(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),zd(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),Bd(d,c),c.push(":"),zd(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Bd(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Cd={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Dd=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Bd(a,b){b.push('"',a.replace(Dd,function(c){var d=Cd[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).substr(1),Cd[c]=d);return d}),'"')}
;function Ed(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function N(a){this.f=0;this.m=void 0;this.i=this.g=this.h=null;this.j=this.l=!1;if(a!=xa)try{var b=this;a.call(void 0,function(c){Fd(b,2,c)},function(c){Fd(b,3,c)})}catch(c){Fd(this,3,c)}}
function Gd(){this.next=this.context=this.onRejected=this.g=this.f=null;this.h=!1}
Gd.prototype.reset=function(){this.context=this.onRejected=this.g=this.f=null;this.h=!1};
var Hd=new Vc(function(){return new Gd},function(a){a.reset()});
function Id(a,b,c){var d=Hd.get();d.g=a;d.onRejected=b;d.context=c;return d}
function Jd(a){return new N(function(b,c){c(a)})}
N.prototype.then=function(a,b,c){return Kd(this,Ca(a)?a:null,Ca(b)?b:null,c)};
N.prototype.$goog_Thenable=!0;function Ld(a,b){return Kd(a,null,b,void 0)}
N.prototype.cancel=function(a){if(0==this.f){var b=new Md(a);cd(function(){Nd(this,b)},this)}};
function Nd(a,b){if(0==a.f)if(a.h){var c=a.h;if(c.g){for(var d=0,e=null,f=null,g=c.g;g&&(g.h||(d++,g.f==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.f&&1==d?Nd(c,b):(f?(d=f,d.next==c.i&&(c.i=d),d.next=d.next.next):Od(c),Pd(c,e,3,b)))}a.h=null}else Fd(a,3,b)}
function Qd(a,b){a.g||2!=a.f&&3!=a.f||Rd(a);a.i?a.i.next=b:a.g=b;a.i=b}
function Kd(a,b,c,d){var e=Id(null,null,null);e.f=new N(function(f,g){e.g=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.onRejected=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof Md?g(h):f(k)}catch(l){g(l)}}:g});
e.f.h=a;Qd(a,e);return e.f}
N.prototype.w=function(a){this.f=0;Fd(this,2,a)};
N.prototype.A=function(a){this.f=0;Fd(this,3,a)};
function Fd(a,b,c){if(0==a.f){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.f=1;a:{var d=c,e=a.w,f=a.A;if(d instanceof N){Qd(d,Id(e||xa,f||null,a));var g=!0}else if(Ed(d))d.then(e,f,a),g=!0;else{if(Da(d))try{var h=d.then;if(Ca(h)){Sd(d,h,e,f,a);g=!0;break a}}catch(k){f.call(a,k);g=!0;break a}g=!1}}g||(a.m=c,a.f=b,a.h=null,Rd(a),3!=b||c instanceof Md||Td(a,c))}}
function Sd(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Rd(a){a.l||(a.l=!0,cd(a.B,a))}
function Od(a){var b=null;a.g&&(b=a.g,a.g=b.next,b.next=null);a.g||(a.i=null);return b}
N.prototype.B=function(){for(var a;a=Od(this);)Pd(this,a,this.f,this.m);this.l=!1};
function Pd(a,b,c,d){if(3==c&&b.onRejected&&!b.h)for(;a&&a.j;a=a.h)a.j=!1;if(b.f)b.f.h=null,Ud(b,c,d);else try{b.h?b.g.call(b.context):Ud(b,c,d)}catch(e){Vd.call(null,e)}Wc(Hd,b)}
function Ud(a,b,c){2==b?a.g.call(a.context,c):a.onRejected&&a.onRejected.call(a.context,c)}
function Td(a,b){a.j=!0;cd(function(){a.j&&Vd.call(null,b)})}
var Vd=Xc;function Md(a){E.call(this,a)}
D(Md,E);Md.prototype.name="cancel";function O(a){M.call(this);this.l=1;this.i=[];this.j=0;this.f=[];this.h={};this.m=!!a}
D(O,M);n=O.prototype;n.subscribe=function(a,b,c){var d=this.h[a];d||(d=this.h[a]=[]);var e=this.l;this.f[e]=a;this.f[e+1]=b;this.f[e+2]=c;this.l=e+3;d.push(e);return e};
function Wd(a,b,c,d){if(b=a.h[b]){var e=a.f;(b=Ra(b,function(f){return e[f+1]==c&&e[f+2]==d}))&&a.N(b)}}
n.N=function(a){var b=this.f[a];if(b){var c=this.h[b];0!=this.j?(this.i.push(a),this.f[a+1]=xa):(c&&Sa(c,a),delete this.f[a],delete this.f[a+1],delete this.f[a+2])}return!!b};
n.M=function(a,b){var c=this.h[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.m)for(e=0;e<c.length;e++){var g=c[e];Xd(this.f[g+1],this.f[g+2],d)}else{this.j++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.f[g+1].apply(this.f[g+2],d)}finally{if(this.j--,0<this.i.length&&0==this.j)for(;c=this.i.pop();)this.N(c)}}return 0!=e}return!1};
function Xd(a,b,c){cd(function(){a.apply(b,c)})}
n.clear=function(a){if(a){var b=this.h[a];b&&(F(b,this.N,this),delete this.h[a])}else this.f.length=0,this.h={}};
n.o=function(){O.L.o.call(this);this.clear();this.i.length=0};function Yd(a){this.f=a}
Yd.prototype.set=function(a,b){void 0===b?this.f.remove(a):this.f.set(a,yd(b))};
Yd.prototype.get=function(a){try{var b=this.f.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
Yd.prototype.remove=function(a){this.f.remove(a)};function Zd(a){this.f=a}
D(Zd,Yd);function $d(a){this.data=a}
function ae(a){return void 0===a||a instanceof $d?a:new $d(a)}
Zd.prototype.set=function(a,b){Zd.L.set.call(this,a,ae(b))};
Zd.prototype.g=function(a){a=Zd.L.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
Zd.prototype.get=function(a){if(a=this.g(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function be(a){this.f=a}
D(be,Zd);be.prototype.set=function(a,b,c){if(b=ae(b)){if(c){if(c<C()){be.prototype.remove.call(this,a);return}b.expiration=c}b.creation=C()}be.L.set.call(this,a,b)};
be.prototype.g=function(a){var b=be.L.g.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<C()||c&&c>C())be.prototype.remove.call(this,a);else return b}};function ce(){}
;function de(){}
D(de,ce);de.prototype.clear=function(){var a=td(this.G(!0)),b=this;F(a,function(c){b.remove(c)})};function ee(a){this.f=a}
D(ee,de);n=ee.prototype;n.isAvailable=function(){if(!this.f)return!1;try{return this.f.setItem("__sak","1"),this.f.removeItem("__sak"),!0}catch(a){return!1}};
n.set=function(a,b){try{this.f.setItem(a,b)}catch(c){if(0==this.f.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
n.get=function(a){a=this.f.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
n.remove=function(a){this.f.removeItem(a)};
n.G=function(a){var b=0,c=this.f,d=new qd;d.next=function(){if(b>=c.length)throw pd;var e=c.key(b++);if(a)return e;e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
n.clear=function(){this.f.clear()};
n.key=function(a){return this.f.key(a)};function fe(){var a=null;try{a=window.localStorage||null}catch(b){}this.f=a}
D(fe,ee);function ge(a,b){this.g=a;this.f=null;if(Yb&&!(9<=Number(jc))){he||(he=new ud);this.f=he.get(a);this.f||(b?this.f=document.getElementById(b):(this.f=document.createElement("userdata"),this.f.addBehavior("#default#userData"),document.body.appendChild(this.f)),he.set(a,this.f));try{this.f.load(this.g)}catch(c){this.f=null}}}
D(ge,de);var ie={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},he=null;function je(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return ie[b]})}
n=ge.prototype;n.isAvailable=function(){return!!this.f};
n.set=function(a,b){this.f.setAttribute(je(a),b);ke(this)};
n.get=function(a){a=this.f.getAttribute(je(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
n.remove=function(a){this.f.removeAttribute(je(a));ke(this)};
n.G=function(a){var b=0,c=this.f.XMLDocument.documentElement.attributes,d=new qd;d.next=function(){if(b>=c.length)throw pd;var e=c[b++];if(a)return decodeURIComponent(e.nodeName.replace(/\./g,"%")).substr(1);e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
n.clear=function(){for(var a=this.f.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);ke(this)};
function ke(a){try{a.f.save(a.g)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function le(a,b){this.g=a;this.f=b+"::"}
D(le,de);le.prototype.set=function(a,b){this.g.set(this.f+a,b)};
le.prototype.get=function(a){return this.g.get(this.f+a)};
le.prototype.remove=function(a){this.g.remove(this.f+a)};
le.prototype.G=function(a){var b=this.g.G(!0),c=this,d=new qd;d.next=function(){for(var e=b.next();e.substr(0,c.f.length)!=c.f;)e=b.next();return a?e.substr(c.f.length):c.g.get(e)};
return d};function me(a,b){1<b.length?a[b[0]]=b[1]:1===b.length&&Object.assign(a,b[0])}
;var ne=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};y("yt.config_",ne,void 0);function P(a){me(ne,arguments)}
function Q(a,b){return a in ne?ne[a]:b}
function oe(){return Q("PLAYER_CONFIG",{})}
function pe(a){var b=ne.EXPERIMENT_FLAGS;return b?b[a]:void 0}
;var qe=[];function re(a){qe.forEach(function(b){return b(a)})}
function se(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){te(b),re(b)}}:a}
function te(a){var b=z("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0):(b=Q("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0]),P("ERRORS",b))}
function ue(a){var b=z("yt.logging.errors.log");b?b(a,"WARNING",void 0,void 0,void 0):(b=Q("ERRORS",[]),b.push([a,"WARNING",void 0,void 0,void 0]),P("ERRORS",b))}
;function ve(){var a=we;z("yt.ads.biscotti.getId_")||y("yt.ads.biscotti.getId_",a,void 0)}
function xe(a){y("yt.ads.biscotti.lastId_",a,void 0)}
;function ye(a){a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length)try{var f=decodeURIComponent((e[0]||"").replace(/\+/g," ")),g=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?Aa(b[f])?Ua(b[f],g):b[f]=[b[f],g]:b[f]=g}catch(k){if("q"!=e[0]){var h=Error("Error decoding URL component");h.params={key:e[0],value:e[1]};te(h)}}}return b}
function ze(a){var b=[];Wa(a,function(c,d){var e=encodeURIComponent(String(d)),f;Aa(c)?f=c:f=[c];F(f,function(g){""==g?b.push(e):b.push(e+"="+encodeURIComponent(String(g)))})});
return b.join("&")}
function Ae(a){"?"==a.charAt(0)&&(a=a.substr(1));return ye(a)}
function Be(a,b){return Ce(a,b||{},!0)}
function Ce(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=Ae(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);return Tb(a,e)+d}
;function De(a){var b=Ee;a=void 0===a?z("yt.ads.biscotti.lastId_")||"":a;b=Object.assign(Fe(b),Ge(b));b.ca_type="image";a&&(b.bid=a);return b}
function Fe(a){var b={};b.dt=Mc;b.flash="0";a:{try{var c=a.f.top.location.href}catch(f){a=2;break a}a=c?c===a.g.location.href?0:1:2}b=(b.frm=a,b);b.u_tz=-(new Date).getTimezoneOffset();var d=void 0===d?L:d;try{var e=d.history.length}catch(f){e=0}b.u_his=e;b.u_java=!!L.navigator&&"unknown"!==typeof L.navigator.javaEnabled&&!!L.navigator.javaEnabled&&L.navigator.javaEnabled();L.screen&&(b.u_h=L.screen.height,b.u_w=L.screen.width,b.u_ah=L.screen.availHeight,b.u_aw=L.screen.availWidth,b.u_cd=L.screen.colorDepth);
L.navigator&&L.navigator.plugins&&(b.u_nplug=L.navigator.plugins.length);L.navigator&&L.navigator.mimeTypes&&(b.u_nmime=L.navigator.mimeTypes.length);return b}
function Ge(a){var b=a.f;try{var c=b.screenX;var d=b.screenY}catch(p){}try{var e=b.outerWidth;var f=b.outerHeight}catch(p){}try{var g=b.innerWidth;var h=b.innerHeight}catch(p){}b=[b.screenLeft,b.screenTop,c,d,b.screen?b.screen.availWidth:void 0,b.screen?b.screen.availTop:void 0,e,f,g,h];c=a.f.top;try{var k=(c||window).document,l="CSS1Compat"==k.compatMode?k.documentElement:k.body;var m=(new sc(l.clientWidth,l.clientHeight)).round()}catch(p){m=new sc(-12245933,-12245933)}k=m;m={};l=new Tc;x.SVGElement&&
x.document.createElementNS&&l.set(0);c=Hc();c["allow-top-navigation-by-user-activation"]&&l.set(1);c["allow-popups-to-escape-sandbox"]&&l.set(2);x.crypto&&x.crypto.subtle&&l.set(3);x.TextDecoder&&x.TextEncoder&&l.set(4);l=Uc(l);m.bc=l;m.bih=k.height;m.biw=k.width;m.brdim=b.join();a=a.g;return m.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[a.visibilityState||a.webkitVisibilityState||a.mozVisibilityState||""]||0,m.wgl=!!L.WebGLRenderingContext,m}
var Ee=new function(){var a=window.document;this.f=window;this.g=a};
y("yt.ads_.signals_.getAdSignalsString",function(a){return ze(De(a))},void 0);C();function R(a){a=He(a);return"string"===typeof a&&"false"===a?!1:!!a}
function Ie(a,b){var c=He(a);return void 0===c&&void 0!==b?b:Number(c||0)}
function He(a){var b=Q("EXPERIMENTS_FORCED_FLAGS",{});return void 0!==b[a]?b[a]:Q("EXPERIMENT_FLAGS",{})[a]}
;var Je=void 0!==XMLHttpRequest?function(){return new XMLHttpRequest}:void 0!==ActiveXObject?function(){return new ActiveXObject("Microsoft.XMLHTTP")}:null;
function Ke(){if(!Je)return null;var a=Je();return"open"in a?a:null}
function Le(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function S(a,b){Ca(a)&&(a=se(a));return window.setTimeout(a,b)}
function T(a){window.clearTimeout(a)}
;var Me={Authorization:"AUTHORIZATION","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},Ne="app debugcss debugjs expflag force_ad_params force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address".split(" "),
Oe=!1;
function Pe(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=J(1,a),e=I(J(3,a));d&&e?(d=c,c=a.match(Qb),d=d.match(Qb),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?I(J(3,c))==e&&(Number(J(4,c))||null)==(Number(J(4,a))||null):!0;d=R("web_ajax_ignore_global_headers_if_set");for(var f in Me)e=Q(Me[f]),!e||!c&&!Qe(a,f)||d&&void 0!==b[f]||(b[f]=e);if(c||Qe(a,"X-YouTube-Utc-Offset"))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());(c||Qe(a,"X-YouTube-Time-Zone"))&&(f="undefined"!=typeof Intl?
(new Intl.DateTimeFormat).resolvedOptions().timeZone:null)&&(b["X-YouTube-Time-Zone"]=f);if(c||Qe(a,"X-YouTube-Ad-Signals"))b["X-YouTube-Ad-Signals"]=ze(De(void 0));return b}
function Re(a){var b=window.location.search,c=I(J(3,a)),d=I(J(5,a));d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=Ae(b),f={};F(Ne,function(g){e[g]&&(f[g]=e[g])});
return Ce(a,f||{},!1)}
function Qe(a,b){var c=Q("CORS_HEADER_WHITELIST")||{},d=I(J(3,a));return d?(c=c[d])?0<=Na(c,b):!1:!0}
function Se(a,b){if(window.fetch&&"XML"!=b.format){var c={method:b.method||"GET",credentials:"same-origin"};b.headers&&(c.headers=b.headers);a=Te(a,b);var d=Ue(a,b);d&&(c.body=d);b.withCredentials&&(c.credentials="include");var e=!1,f;fetch(a,c).then(function(g){if(!e){e=!0;f&&T(f);var h=g.ok,k=function(l){l=l||{};var m=b.context||x;h?b.onSuccess&&b.onSuccess.call(m,l,g):b.onError&&b.onError.call(m,l,g);b.ja&&b.ja.call(m,l,g)};
"JSON"==(b.format||"JSON")&&(h||400<=g.status&&500>g.status)?g.json().then(k,function(){k(null)}):k(null)}});
b.qa&&0<b.timeout&&(f=S(function(){e||(e=!0,T(f),b.qa.call(b.context||x))},b.timeout))}else Ve(a,b)}
function Ve(a,b){var c=b.format||"JSON";a=Te(a,b);var d=Ue(a,b),e=!1,f,g=We(a,function(h){if(!e){e=!0;f&&T(f);var k=Le(h),l=null,m=400<=h.status&&500>h.status,p=500<=h.status&&600>h.status;if(k||m||p)l=Xe(c,h,b.qb);if(k)a:if(h&&204==h.status)k=!0;else{switch(c){case "XML":k=0==parseInt(l&&l.return_code,10);break a;case "RAW":k=!0;break a}k=!!l}l=l||{};m=b.context||x;k?b.onSuccess&&b.onSuccess.call(m,h,l):b.onError&&b.onError.call(m,h,l);b.ja&&b.ja.call(m,h,l)}},b.method,d,b.headers,b.responseType,
b.withCredentials);
b.O&&0<b.timeout&&(f=S(function(){e||(e=!0,g.abort(),T(f),b.O.call(b.context||x,g))},b.timeout));
return g}
function Te(a,b){b.tb&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=Q("XSRF_FIELD_NAME",void 0),d=b.ab;d&&(d[c]&&delete d[c],a=Be(a,d));return a}
function Ue(a,b){var c=Q("XSRF_FIELD_NAME",void 0),d=Q("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.C,g=Q("XSRF_FIELD_NAME",void 0),h;b.headers&&(h=b.headers["Content-Type"]);b.sb||I(J(3,a))&&!b.withCredentials&&I(J(3,a))!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.C&&b.C[g]||(f||(f={}),f[c]=d);f&&"string"===typeof e&&(e=Ae(e),fb(e,f),e=b.ra&&"JSON"==b.ra?JSON.stringify(e):Sb(e));f=e||f&&!$a(f);!Oe&&f&&"POST"!=b.method&&(Oe=!0,te(Error("AJAX request with postData should use POST")));
return e}
function Xe(a,b,c){var d=null;switch(a){case "JSON":a=b.responseText;b=b.getResponseHeader("Content-Type")||"";a&&0<=b.indexOf("json")&&(d=JSON.parse(a));break;case "XML":if(b=(b=b.responseXML)?Ye(b):null)d={},F(b.getElementsByTagName("*"),function(e){d[e.tagName]=Ze(e)})}c&&$e(d);
return d}
function $e(a){if(Da(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Jb(a[b],null);a[c]=d}else $e(a[b])}}
function Ye(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Ze(a){var b="";F(a.childNodes,function(c){b+=c.nodeValue});
return b}
function We(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&se(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=Ke();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;R("debug_forward_web_query_parameters")&&(a=Re(a));k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=Pe(a,e))for(var l in e)k.setRequestHeader(l,e[l]),"content-type"==l.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);
return k}
;var af={},bf=0;
function cf(a,b,c,d,e){e=void 0===e?"":e;a&&(c&&(c=Db,c=!(c&&0<=c.toLowerCase().indexOf("cobalt"))),c?a&&(a instanceof G||(a="object"==typeof a&&a.J?a.I():String(a),Bb.test(a)||(a="about:invalid#zClosurez"),a=new G(yb,a)),b=Ab(a),"about:invalid#zClosurez"===b?a="":(b instanceof Gb?a=b:(d="object"==typeof b,a=null,d&&b.ha&&(a=b.ea()),b=qb(d&&b.J?b.I():String(b)),a=Jb(b,a)),a=Ib(a).toString(),a=encodeURIComponent(String(yd(a)))),/^[\s\xa0]*$/.test(a)||(a=wc("IFRAME",{src:'javascript:"<body><img src=\\""+'+a+
'+"\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a))):e?We(a,b,"POST",e,d):Q("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d?We(a,b,"GET","",d):df(a,b)||ef(a,b))}
function df(a,b){if(!pe("web_use_beacon_api_for_ad_click_server_pings"))return!1;if(pe("use_sonic_js_library_for_v4_support"))try{var c,d=I(J(5,a));if(!(c=!(d&&d.endsWith("/aclk")))){var e=new Wb({url:a});c=!(e.j?e.h&&e.f&&e.f[1]||e.i:e.g)}if(c)return!1}catch(f){return ue(Error("ClickUrl library throws error, url = "+a)),!1}else if(c=I(J(5,a)),!c||-1==c.indexOf("/aclk")||"1"!==Vb(a,"ae")||"1"!==Vb(a,"act"))return!1;return ff(a)?(b&&b(),!0):!1}
function ff(a,b){try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,void 0===b?"":b))return!0}catch(c){}return!1}
function ef(a,b){var c=new Image,d=""+bf++;af[d]=c;c.onload=c.onerror=function(){b&&af[d]&&b();delete af[d]};
c.src=a}
;var gf=z("ytPubsubPubsubInstance")||new O;O.prototype.subscribe=O.prototype.subscribe;O.prototype.unsubscribeByKey=O.prototype.N;O.prototype.publish=O.prototype.M;O.prototype.clear=O.prototype.clear;y("ytPubsubPubsubInstance",gf,void 0);var hf=z("ytPubsubPubsubSubscribedKeys")||{};y("ytPubsubPubsubSubscribedKeys",hf,void 0);var jf=z("ytPubsubPubsubTopicToKeys")||{};y("ytPubsubPubsubTopicToKeys",jf,void 0);var kf=z("ytPubsubPubsubIsSynchronous")||{};y("ytPubsubPubsubIsSynchronous",kf,void 0);
function lf(a,b){var c=mf();if(c){var d=c.subscribe(a,function(){var e=arguments;var f=function(){hf[d]&&b.apply(window,e)};
try{kf[a]?f():S(f,0)}catch(g){te(g)}},void 0);
hf[d]=!0;jf[a]||(jf[a]=[]);jf[a].push(d);return d}return 0}
function nf(a){var b=mf();b&&("number"===typeof a?a=[a]:"string"===typeof a&&(a=[parseInt(a,10)]),F(a,function(c){b.unsubscribeByKey(c);delete hf[c]}))}
function of(a,b){var c=mf();c&&c.publish.apply(c,arguments)}
function pf(a){var b=mf();if(b)if(b.clear(a),a)qf(a);else for(var c in jf)qf(c)}
function mf(){return z("ytPubsubPubsubInstance")}
function qf(a){jf[a]&&(a=jf[a],F(a,function(b){hf[b]&&delete hf[b]}),a.length=0)}
;var rf=window,U=rf.ytcsi&&rf.ytcsi.now?rf.ytcsi.now:rf.performance&&rf.performance.timing&&rf.performance.now&&rf.performance.timing.navigationStart?function(){return rf.performance.timing.navigationStart+rf.performance.now()}:function(){return(new Date).getTime()};var sf=Ie("initial_gel_batch_timeout",1E3),tf=Math.pow(2,16)-1,uf=null,vf=0,wf={log_event:"events",log_interaction:"interactions"},xf=Object.create(null);xf.log_event="GENERIC_EVENT_LOGGING";xf.log_interaction="INTERACTION_LOGGING";var yf=new Set(["log_event"]),zf={},Af=0,Bf=0,Cf=0,Df=!0,V=z("ytLoggingTransportLogPayloadsQueue_")||{};y("ytLoggingTransportLogPayloadsQueue_",V,void 0);var Ef=z("ytLoggingTransportTokensToCttTargetIds_")||{};y("ytLoggingTransportTokensToCttTargetIds_",Ef,void 0);
var Ff=z("ytLoggingTransportDispatchedStats_")||{};y("ytLoggingTransportDispatchedStats_",Ff,void 0);var Gf=z("ytLoggingTransportCapturedTime_")||{};y("ytytLoggingTransportCapturedTime_",Gf,void 0);
function Hf(){T(Af);T(Bf);Bf=0;if(!$a(V)){for(var a in V){var b=zf[a];if(b&&b.isReady()){var c=void 0,d=a,e=b,f=wf[d],g=Ff[d]||{};Ff[d]=g;b=Math.round(U());for(c in V[d]){var h=db,k=e.f||If();k={client:{hl:k.Ia,gl:k.Ha,clientName:k.Ga,clientVersion:k.innertubeContextClientVersion,configInfo:k.Fa}};var l=window.devicePixelRatio;l&&1!=l&&(k.client.screenDensityFloat=String(l));l=Q("EXPERIMENTS_TOKEN","");""!==l&&(k.client.experimentsToken=l);var m=l=void 0,p=[],v=Q("EXPERIMENTS_FORCED_FLAGS",{});for(m in v)p.push({key:m,
value:String(v[m])});m=Q("EXPERIMENT_FLAGS",{});for(l in m)l.startsWith("force_")&&void 0===v[l]&&p.push({key:l,value:String(m[l])});l=p;0<l.length&&(k.request={internalExperimentFlags:l});Q("DELEGATED_SESSION_ID")&&!R("pageid_as_header_web")&&(k.user={onBehalfOfUser:Q("DELEGATED_SESSION_ID")});R("enable_device_forwarding_from_xhr_client")&&(k.client=Object.assign(k.client,Jf()));h=h({context:k});h[f]=Kf(d,c);g.dispatchedEventCount=g.dispatchedEventCount||0;g.dispatchedEventCount+=h[f].length;if(k=
Ef[c])a:{p=h;v=c;if(k.videoId)l="VIDEO";else if(k.playlistId)l="PLAYLIST";else break a;p.credentialTransferTokenTargetId=k;p.context=p.context||{};p.context.user=p.context.user||{};p.context.user.credentialTransferTokens=[{token:v,scope:l}]}delete Ef[c];k=h;k.requestTimeMs=b;R("unsplit_gel_payloads_in_logs")&&(k.unsplitGelPayloadsInLogs=!0);if(l=Q("EVENT_ID",void 0))p=Q("BATCH_CLIENT_COUNTER",void 0)||0,!p&&R("web_client_counter_random_seed")&&(p=Math.floor(Math.random()*tf/2)),p++,p>tf&&(p=1),P("BATCH_CLIENT_COUNTER",
p),l={serializedEventId:l,clientCounter:p},k.serializedClientEventId=l,uf&&vf&&R("log_gel_rtt_web")&&(k.previousBatchInfo={serializedClientEventId:uf,roundtripMs:vf}),uf=l,vf=0;Lf(e,d,h,{retry:yf.has(d),onSuccess:Ka(Mf,U())})}c=g;d=b;c.previousDispatchMs&&(b=d-c.previousDispatchMs,e=c.diffCount||0,c.averageTimeBetweenDispatchesMs=e?((c.averageTimeBetweenDispatchesMs||0)*e+b)/(e+1):b,c.diffCount=e+1);c.previousDispatchMs=d;delete V[a];Df=!1}}$a(V)||Nf()}}
function Of(){var a=[];for(e in V){var b=Ff[e]||{};Ff[e]=b;for(var c in V[e]){var d=Kf(e,c);b.storedEventsCount=b.storedEventsCount||0;b.storedEventsCount+=d.length}}var e=Math.round(U());for(var f in Ff)b=Ff[f],b.eventType=f in xf?xf[f]:"UNKNOWN_TYPE",c=Gf[f],b.metricIntervalMs=c?e-c:e-NaN,a.push(b),Gf[f]=e,delete Ff[f];return a}
function Nf(){R("web_gel_timeout_cap")&&!Bf&&(Bf=S(Hf,6E4));T(Af);var a=Q("LOGGING_BATCH_TIMEOUT",Ie("web_gel_debounce_ms",1E4));R("shorten_initial_gel_batch_timeout")&&Df&&(a=sf);Af=S(Hf,a)}
function Kf(a,b){b=void 0===b?"":b;V[a]=V[a]||{};V[a][b]=V[a][b]||[];return V[a][b]}
function Mf(a){vf=Math.round(U()-a)}
;var Pf=0;y("ytDomDomGetNextId",z("ytDomDomGetNextId")||function(){return++Pf},void 0);var Qf={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function Rf(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in Qf||(this[b]=a[b]);var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==
this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.f=a.pageX;this.g=a.pageY}}catch(e){}}
function Sf(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.f=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.g=a.clientY+b}}
Rf.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
Rf.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
Rf.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var Za=z("ytEventsEventsListeners")||{};y("ytEventsEventsListeners",Za,void 0);var Tf=z("ytEventsEventsCounter")||{count:0};y("ytEventsEventsCounter",Tf,void 0);
function Uf(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return Ya(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Da(e[4])&&Da(d)&&bb(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
var Vf=Va(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function W(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=Uf(a,b,c,d);if(e)return e;e=++Tf.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new Rf(h);if(!Ac(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new Rf(h);
h.currentTarget=a;return c.call(a,h)};
g=se(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),Vf()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);Za[e]=[a,b,c,g,d];return e}
function Wf(a){a&&("string"==typeof a&&(a=[a]),F(a,function(b){if(b in Za){var c=Za[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?Vf()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete Za[b]}}))}
;var Xf=window.ytcsi&&window.ytcsi.now?window.ytcsi.now:window.performance&&window.performance.timing&&window.performance.now&&window.performance.timing.navigationStart?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};function Yf(a){this.w=a;this.f=null;this.j=0;this.m=null;this.l=0;this.h=[];for(a=0;4>a;a++)this.h.push(0);this.i=0;this.D=W(window,"mousemove",A(this.F,this));a=A(this.A,this);Ca(a)&&(a=se(a));this.K=window.setInterval(a,25)}
D(Yf,M);Yf.prototype.F=function(a){void 0===a.f&&Sf(a);var b=a.f;void 0===a.g&&Sf(a);this.f=new rc(b,a.g)};
Yf.prototype.A=function(){if(this.f){var a=Xf();if(0!=this.j){var b=this.m,c=this.f,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.j);this.h[this.i]=.5<Math.abs((d-this.l)/this.l)?1:0;for(c=b=0;4>c;c++)b+=this.h[c]||0;3<=b&&this.w();this.l=d}this.j=a;this.m=this.f;this.i=(this.i+1)%4}};
Yf.prototype.o=function(){window.clearInterval(this.K);Wf(this.D)};function Zf(){}
function $f(a,b){return ag(a,1,b)}
;function bg(){}
t(bg,Zf);function ag(a,b,c){isNaN(c)&&(c=void 0);var d=z("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):S(a,c||0)}
bg.prototype.start=function(){var a=z("yt.scheduler.instance.start");a&&a()};
bg.prototype.pause=function(){var a=z("yt.scheduler.instance.pause");a&&a()};
ya(bg);bg.getInstance();var cg={};
function dg(a){var b=void 0===a?{}:a;a=void 0===b.Ea?!0:b.Ea;b=void 0===b.Pa?!1:b.Pa;if(null==z("_lact",window)){var c=parseInt(Q("LACT"),10);c=isFinite(c)?C()-Math.max(c,0):-1;y("_lact",c,window);y("_fact",c,window);-1==c&&eg();W(document,"keydown",eg);W(document,"keyup",eg);W(document,"mousedown",eg);W(document,"mouseup",eg);a&&(b?W(window,"touchmove",function(){fg("touchmove",200)},{passive:!0}):(W(window,"resize",function(){fg("resize",200)}),W(window,"scroll",function(){fg("scroll",200)})));
new Yf(function(){fg("mouse",100)});
W(document,"touchstart",eg,{passive:!0});W(document,"touchend",eg,{passive:!0})}}
function fg(a,b){cg[a]||(cg[a]=!0,$f(function(){eg();cg[a]=!1},b))}
function eg(){null==z("_lact",window)&&dg();var a=C();y("_lact",a,window);-1==z("_fact",window)&&y("_fact",a,window);(a=z("ytglobal.ytUtilActivityCallback_"))&&a()}
function gg(){var a=z("_lact",window);return null==a?-1:Math.max(C()-a,0)}
;var hg=z("ytLoggingGelSequenceIdObj_")||{};y("ytLoggingGelSequenceIdObj_",hg,void 0);
function ig(a,b,c,d){d=void 0===d?{}:d;var e={};e.eventTimeMs=Math.round(d.timestamp||U());e[a]=b;e.context={lastActivityMs:String(d.timestamp?-1:gg())};R("log_sequence_info_on_gel_web")&&d.P&&(a=e.context,b=d.P,hg[b]=b in hg?hg[b]+1:0,a.sequence={index:hg[b],groupKey:b},d.rb&&delete hg[d.P]);(d=d.da)?(a={},d.videoId?a.videoId=d.videoId:d.playlistId&&(a.playlistId=d.playlistId),Ef[d.token]=a,d=Kf("log_event",d.token)):d=Kf("log_event");d.push(e);c&&(zf.log_event=new c);c=Ie("web_logging_max_batch")||
100;e=U();d.length>=c?Hf():10<=e-Cf&&(Nf(),Cf=e)}
;function Jf(){for(var a={},b=q(Object.entries(Ae(Q("DEVICE","")))),c=b.next();!c.done;c=b.next()){var d=q(c.value);c=d.next().value;d=d.next().value;"cbrand"===c?a.deviceMake=d:"cmodel"===c?a.deviceModel=d:"cbr"===c?a.browserName=d:"cbrver"===c?a.browserVersion=d:"cos"===c?a.osName=d:"cosver"===c?a.osVersion=d:"cplatform"===c&&(a.platform=d)}return a}
;function jg(){return"INNERTUBE_API_KEY"in ne&&"INNERTUBE_API_VERSION"in ne}
function If(){return{innertubeApiKey:Q("INNERTUBE_API_KEY",void 0),innertubeApiVersion:Q("INNERTUBE_API_VERSION",void 0),Fa:Q("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),Ga:Q("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:Q("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0),Ia:Q("INNERTUBE_CONTEXT_HL",void 0),Ha:Q("INNERTUBE_CONTEXT_GL",void 0),Ja:Q("INNERTUBE_HOST_OVERRIDE",void 0)||"",Ka:!!Q("INNERTUBE_USE_THIRD_PARTY_AUTH",!1)}}
function kg(a,b,c){c=void 0===c?{}:c;var d={"X-Goog-Visitor-Id":c.visitorData||Q("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;(b=c.ob||Q("AUTHORIZATION"))||(a?b="Bearer "+z("gapi.auth.getToken")().nb:b=Sc([]));b&&(d.Authorization=b,d["X-Goog-AuthUser"]=Q("SESSION_INDEX",0),R("pageid_as_header_web")&&(d["X-Goog-PageId"]=Q("DELEGATED_SESSION_ID")));return d}
function lg(a){a=Object.assign({},a);delete a.Authorization;var b=Sc();if(b){var c=new jd;c.update(Q("INNERTUBE_API_KEY",void 0));c.update(b);b=c.digest();c=3;Ba(b);void 0===c&&(c=0);if(!lc){lc={};for(var d="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),e=["+/=","+/","-_=","-_.","-_"],f=0;5>f;f++){var g=d.concat(e[f].split(""));kc[f]=g;for(var h=0;h<g.length;h++){var k=g[h];void 0===lc[k]&&(lc[k]=h)}}}c=kc[c];d=[];for(e=0;e<b.length;e+=3){var l=b[e],m=(f=e+1<b.length)?
b[e+1]:0;k=(g=e+2<b.length)?b[e+2]:0;h=l>>2;l=(l&3)<<4|m>>4;m=(m&15)<<2|k>>6;k&=63;g||(k=64,f||(m=64));d.push(c[h],c[l],c[m]||"",c[k]||"")}a.hash=d.join("")}return a}
;function mg(a,b,c,d){pc.set(""+a,b,{ma:c,path:"/",domain:void 0===d?"youtube.com":d,secure:!1})}
;function ng(){var a=new fe;(a=a.isAvailable()?new le(a,"yt.innertube"):null)||(a=new ge("yt.innertube"),a=a.isAvailable()?a:null);this.f=a?new be(a):null;this.g=document.domain||window.location.hostname}
ng.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.f)try{this.f.set(a,b,C()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(yd(b))}catch(f){return}else e=escape(b);mg(a,e,c,this.g)};
ng.prototype.get=function(a,b){var c=void 0,d=!this.f;if(!d)try{c=this.f.get(a)}catch(e){d=!0}if(d&&(c=pc.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
ng.prototype.remove=function(a){this.f&&this.f.remove(a);var b=this.g;pc.remove(""+a,"/",void 0===b?"youtube.com":b)};var og=new ng;function pg(a,b,c,d){if(d)return null;d=og.get("nextId",!0)||1;var e=og.get("requests",!0)||{};e[d]={method:a,request:b,authState:lg(c),requestTime:Math.round(U())};og.set("nextId",d+1,86400,!0);og.set("requests",e,86400,!0);return d}
function qg(a){var b=og.get("requests",!0)||{};delete b[a];og.set("requests",b,86400,!0)}
function rg(a){var b=og.get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(U())-d.requestTime)){var e=d.authState,f=lg(kg(!1));bb(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(U())),Lf(a,d.method,e,{}));delete b[c]}}og.set("requests",b,86400,!0)}}
;function sg(a){var b=this;this.f=null;a?this.f=a:jg()&&(this.f=If());ag(function(){rg(b)},0,5E3)}
sg.prototype.isReady=function(){!this.f&&jg()&&(this.f=If());return!!this.f};
function Lf(a,b,c,d){!Q("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&ue(Error("Missing VISITOR_DATA when sending innertube request."));var e={headers:{"Content-Type":"application/json"},method:"POST",C:c,ra:"JSON",O:function(){d.O()},
qa:d.O,onSuccess:function(v,r){if(d.onSuccess)d.onSuccess(r)},
oa:function(v){if(d.onSuccess)d.onSuccess(v)},
onError:function(v,r){if(d.onError)d.onError(r)},
vb:function(v){if(d.onError)d.onError(v)},
timeout:d.timeout,withCredentials:!0},f="",g=a.f.Ja;g&&(f=g);g=a.f.Ka||!1;var h=kg(g,f,d);Object.assign(e.headers,h);e.headers.Authorization&&!f&&(e.headers["x-origin"]=window.location.origin);var k=Be(""+f+("/youtubei/"+a.f.innertubeApiVersion+"/"+b),{alt:"json",key:a.f.innertubeApiKey}),l;if(d.retry&&R("retry_web_logging_batches")&&"www.youtube-nocookie.com"!=f&&(l=pg(b,c,h,g))){var m=e.onSuccess,p=e.oa;e.onSuccess=function(v,r){qg(l);m(v,r)};
c.oa=function(v,r){qg(l);p(v,r)}}try{R("use_fetch_for_op_xhr")?Se(k,e):(e.method="POST",e.C||(e.C={}),Ve(k,e))}catch(v){if("InvalidAccessError"==v)l&&(qg(l),l=0),ue(Error("An extension is blocking network request."));
else throw v;}l&&ag(function(){rg(a)},0,5E3)}
;function tg(a,b,c){c=void 0===c?{}:c;var d=sg;Q("ytLoggingEventsDefaultDisabled",!1)&&sg==sg&&(d=null);ig(a,b,d,c)}
function ug(){R("log_web_meta")&&Of().forEach(function(a){tg("delayedEventMetricCaptured",a)})}
;function vg(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];d=Error.call(this,a);this.message=d.message;"stack"in d&&(this.stack=d.stack);this.args=[].concat(c instanceof Array?c:ka(q(c)))}
t(vg,Error);var wg=new Set,xg=0;function yg(a){zg(a,"WARNING")}
function zg(a,b,c,d,e){e=void 0===e?{}:e;e.name=c||Q("INNERTUBE_CONTEXT_CLIENT_NAME",1);e.version=d||Q("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);c=e||{};b=void 0===b?"ERROR":b;b=void 0===b?"ERROR":b;d=window&&window.yterr||!1;if(a&&d&&!(5<=xg)&&(R("console_log_js_exceptions")&&(d=[],d.push("Name: "+a.name),d.push("Message: "+a.message),a.hasOwnProperty("params")&&d.push("Error Params: "+JSON.stringify(a.params)),d.push("File name: "+a.fileName),d.push("Stacktrace: "+a.stack),window.console.log(d.join("\n"),
a)),0!==a.f)){d=a.g;e=a.columnNumber;if(a.args&&a.args.length)for(var f=0,g=0;g<a.args.length;g++){var h=a.args[g],k="params."+g;f+=k.length;if(h)if(Array.isArray(h))for(var l=c,m=0;m<h.length&&!(h[m]&&(f+=Ag(m,h[m],k,l),500<f));m++);else if("object"===typeof h)for(l in l=void 0,m=c,h){if(h[l]&&(f+=Ag(l,h[l],k,m),500<f))break}else c[k]=String(JSON.stringify(h)).substring(0,500),f+=c[k].length;else c[k]=String(JSON.stringify(h)).substring(0,500),f+=c[k].length;if(500<=f)break}else if(a.hasOwnProperty("params"))if(h=
a.params,"object"===typeof a.params)for(g in k=0,h){if(h[g]&&(f="params."+g,l=String(JSON.stringify(h[g])).substr(0,500),c[f]=l,k+=f.length+l.length,500<k))break}else c.params=String(JSON.stringify(h)).substr(0,500);a=mc(a);(d=d||a.stack)||(d="Not available");h={stackTrace:d};a.fileName&&(h.filename=a.fileName);g=a.lineNumber.toString();isNaN(g)||!e||isNaN(e)||(h.lineNumber=Number(g),h.columnNumber=Number(e),g=g+":"+e);window.yterr&&Ca(window.yterr)&&(a.params=c,window.yterr(a));if(!(wg.has(a.message)||
0<=d.indexOf("/YouTubeCenter.js")||0<=d.indexOf("/mytube.js"))){if(R("kevlar_gel_error_routing")){k=b;e={level:"ERROR_LEVEL_UNKNOWN",message:a.message};"ERROR"===k?e.level="ERROR_LEVEL_ERROR":"WARNING"===k&&(e.level="ERROR_LEVEL_WARNNING");h={isObfuscated:!0,browserStackInfo:h};k={pageUrl:window.location.href,kvPairs:[]};f=q(Object.keys(c));for(l=f.next();!l.done;l=f.next())l=l.value,k.kvPairs.push({key:"client."+l,value:String(c[l])});tg("clientError",{errorMetadata:k,stackTrace:h,logMessage:e});
ug();Hf()}b={ab:{a:"logerror",t:"jserror",type:a.name,msg:a.message.substr(0,250),line:g,level:b,"client.name":c.name},C:{url:Q("PAGE_NAME",window.location.href),file:a.fileName},method:"POST"};c.version&&(b["client.version"]=c.version);if(b.C){d&&(b.C.stack=d);d=q(Object.keys(c));for(e=d.next();!e.done;e=d.next())e=e.value,b.C["client."+e]=c[e];if(c=Q("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(d=q(Object.keys(c)),e=d.next();!e.done;e=d.next())e=e.value,b.C[e]=c[e]}Ve(Q("ECATCHER_REPORT_HOST",
"")+"/error_204",b);wg.add(a.message);xg++}}}
function Ag(a,b,c,d){c+="."+a;a=String(JSON.stringify(b)).substr(0,500);d[c]=a;return c.length+a.length}
;function Bg(a,b,c,d,e,f){zg(a,void 0===b?"ERROR":b,c,d,f)}
;var Cg=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};y("yt.msgs_",Cg,void 0);function Dg(a){me(Cg,arguments)}
;function Eg(a){a&&(a.dataset?a.dataset[Fg("loaded")]="true":a.setAttribute("data-loaded","true"))}
function Gg(a,b){return a?a.dataset?a.dataset[Fg(b)]:a.getAttribute("data-"+b):null}
var Hg={};function Fg(a){return Hg[a]||(Hg[a]=String(a).replace(/\-([a-z])/g,function(b,c){return c.toUpperCase()}))}
;var Ig=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,Jg=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function Kg(a,b,c){c=void 0===c?null:c;if(window.spf&&spf.script){c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(Ig,""),c=c.replace(Jg,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else Lg(a,b,c)}
function Lg(a,b,c){c=void 0===c?null:c;var d=Mg(a),e=document.getElementById(d),f=e&&Gg(e,"loaded"),g=e&&!f;f?b&&b():(b&&(f=lf(d,b),b=""+Ea(b),Ng[b]=f),g||(e=Og(a,d,function(){Gg(e,"loaded")||(Eg(e),of(d),S(Ka(pf,d),0))},c)))}
function Og(a,b,c,d){d=void 0===d?null:d;var e=xc(document,"SCRIPT");e.id=b;e.onload=function(){c&&setTimeout(c,0)};
e.onreadystatechange=function(){switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);Nb(e,Bc(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function Pg(a){a=Mg(a);var b=document.getElementById(a);b&&(pf(a),b.parentNode.removeChild(b))}
function Qg(a,b){if(a&&b){var c=""+Ea(b);(c=Ng[c])&&nf(c)}}
function Mg(a){var b=document.createElement("a");Mb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+Pb(a)}
var Ng={};var Rg=[],Sg=!1;function Tg(){if("1"!=Xa(oe(),"args","privembed")){var a=function(){Sg=!0;"google_ad_status"in window?P("DCLKSTAT",1):P("DCLKSTAT",2)};
Kg("//static.doubleclick.net/instream/ad_status.js",a);Rg.push($f(function(){Sg||"google_ad_status"in window||(Qg("//static.doubleclick.net/instream/ad_status.js",a),Sg=!0,P("DCLKSTAT",3))},5E3))}}
function Ug(){return parseInt(Q("DCLKSTAT",0),10)}
;function Vg(){this.g=!1;this.f=null}
Vg.prototype.initialize=function(a,b,c,d,e,f){var g=this;f=void 0===f?!1:f;b?(this.g=!0,Kg(b,function(){g.g=!1;window.botguard?Wg(g,c,d,f):(Pg(b),yg(new vg("Unable to load Botguard","from "+b)))},e)):a&&(eval(a),window.botguard?Wg(this,c,d,f):yg(Error("Unable to load Botguard from JS")))};
function Wg(a,b,c,d){if(d)try{a.f=new window.botguard.bg(b,c?function(){return c(b)}:xa)}catch(e){yg(e)}else{try{a.f=new window.botguard.bg(b)}catch(e){yg(e)}c&&c(b)}}
Vg.prototype.dispose=function(){this.f=null};var Xg=new Vg,Yg=!1,Zg=0,$g="";function ah(a){R("botguard_periodic_refresh")?Zg=U():R("botguard_always_refresh")&&($g=a)}
function bh(a){if(a){if(Xg.g)return!1;if(R("botguard_periodic_refresh"))return 72E5<U()-Zg;if(R("botguard_always_refresh"))return $g!=a}else return!1;return!Yg}
function ch(){return!!Xg.f}
function dh(a){a=void 0===a?{}:a;a=void 0===a?{}:a;return Xg.f?Xg.f.invoke(void 0,void 0,a):null}
;var eh=C().toString();
function fh(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=C();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(eh)for(a=1,b=0;b<eh.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^eh.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));
return a.join("")}
;var gh=z("ytLoggingDocDocumentNonce_")||fh();y("ytLoggingDocDocumentNonce_",gh,void 0);var hh=1;function ih(a){this.f=a}
function jh(a){var b={};void 0!==a.f.trackingParams?b.trackingParams=a.f.trackingParams:(b.veType=a.f.veType,void 0!==a.f.veCounter&&(b.veCounter=a.f.veCounter),void 0!==a.f.elementIndex&&(b.elementIndex=a.f.elementIndex));void 0!==a.f.dataElement&&(b.dataElement=jh(a.f.dataElement));void 0!==a.f.youtubeData&&(b.youtubeData=a.f.youtubeData);return b}
ih.prototype.toString=function(){return JSON.stringify(jh(this))};function kh(a){a=void 0===a?0:a;return 0==a?"client-screen-nonce":"client-screen-nonce."+a}
function lh(a){a=void 0===a?0:a;return 0==a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a}
function mh(a){return Q(lh(void 0===a?0:a),void 0)}
y("yt_logging_screen.getRootVeType",mh,void 0);function nh(){var a=mh(0),b;a?b=new ih({veType:a,youtubeData:void 0}):b=null;return b}
function oh(){var a=Q("csn-to-ctt-auth-info");a||(a={},P("csn-to-ctt-auth-info",a));return a}
function ph(a){a=void 0===a?0:a;var b=Q(kh(a));if(!b&&!Q("USE_CSN_FALLBACK",!0))return null;b||0!=a||(R("kevlar_client_side_screens")||R("c3_client_side_screens")?b="UNDEFINED_CSN":b=Q("EVENT_ID"));return b?b:null}
y("yt_logging_screen.getCurrentCsn",ph,void 0);function qh(a,b,c){var d=oh();(c=ph(c))&&delete d[c];b&&(d[a]=b)}
function rh(a){return oh()[a]}
y("yt_logging_screen.getCttAuthInfo",rh,void 0);function sh(a,b,c,d){c=void 0===c?0:c;if(a!==Q(kh(c))||b!==Q(lh(c)))if(qh(a,d,c),P(kh(c),a),P(lh(c),b),0==c||R("web_screen_associated_all_layers"))b=function(){setTimeout(function(){a&&ig("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:gh,clientScreenNonce:a},sg)},0)},"requestAnimationFrame"in window?window.requestAnimationFrame(b):b()}
y("yt_logging_screen.setCurrentScreen",sh,void 0);function th(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=Q("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=void 0===e?!0:e;var f=Q("VALID_SESSION_TEMPDATA_DOMAINS",[]),g=I(J(3,window.location.href));g&&f.push(g);g=I(J(3,d));if(0<=Na(f,g)||!g&&0==d.lastIndexOf("/",0))if(R("autoescape_tempdata_url")&&(f=document.createElement("a"),Mb(f,d),d=f.href),d){g=d.match(Qb);d=g[5];f=g[6];g=g[7];var h="";d&&(h+=d);f&&(h+="?"+f);g&&(h+="#"+g);d=h;f=d.indexOf("#");if(d=0>f?d:d.substr(0,f))if(e&&!b.csn&&(b.itct||
b.ved)&&(b=Object.assign({csn:ph()},b)),k){var k=parseInt(k,10);isFinite(k)&&0<k&&(e=b,b="ST-"+Pb(d).toString(36),e=e?Sb(e):"",mg(b,e,k||5))}else k=b,e="ST-"+Pb(d).toString(36),k=k?Sb(k):"",mg(e,k,5)}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var l=void 0===l?{}:l;var m=void 0===m?"":m;var p=void 0===p?window:p;c=p.location;a=Tb(a,l)+m;a=a instanceof G?a:Cb(a);c.href=Ab(a)}return!0}
;function uh(a,b){this.version=a;this.args=b}
;function vh(a,b){this.topic=a;this.f=b}
vh.prototype.toString=function(){return this.topic};var wh=z("ytPubsub2Pubsub2Instance")||new O;O.prototype.subscribe=O.prototype.subscribe;O.prototype.unsubscribeByKey=O.prototype.N;O.prototype.publish=O.prototype.M;O.prototype.clear=O.prototype.clear;y("ytPubsub2Pubsub2Instance",wh,void 0);var xh=z("ytPubsub2Pubsub2SubscribedKeys")||{};y("ytPubsub2Pubsub2SubscribedKeys",xh,void 0);var yh=z("ytPubsub2Pubsub2TopicToKeys")||{};y("ytPubsub2Pubsub2TopicToKeys",yh,void 0);var zh=z("ytPubsub2Pubsub2IsAsync")||{};y("ytPubsub2Pubsub2IsAsync",zh,void 0);
y("ytPubsub2Pubsub2SkipSubKey",null,void 0);function Ah(a,b){var c=Bh();c&&c.publish.call(c,a.toString(),a,b)}
function Ch(a){var b=Dh,c=Bh();if(!c)return 0;var d=c.subscribe(b.toString(),function(e,f){var g=z("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=function(){if(xh[d])try{if(f&&b instanceof vh&&b!=e)try{var h=b.f,k=f;if(!k.args||!k.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!h.H){var l=new h;h.H=l.version}var m=h.H}catch(p){}if(!m||k.version!=m)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{f=Reflect.construct(h,
Ta(k.args))}catch(p){throw p.message="yt.pubsub2.Data.deserialize(): "+p.message,p;}}catch(p){throw p.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+p.message,p;}a.call(window,f)}catch(p){te(p)}},zh[b.toString()]?z("yt.scheduler.instance")?$f(g):S(g,0):g())});
xh[d]=!0;yh[b.toString()]||(yh[b.toString()]=[]);yh[b.toString()].push(d);return d}
function Eh(){var a=Fh,b=Ch(function(c){a.apply(void 0,arguments);Gh(b)});
return b}
function Gh(a){var b=Bh();b&&("number"===typeof a&&(a=[a]),F(a,function(c){b.unsubscribeByKey(c);delete xh[c]}))}
function Bh(){return z("ytPubsub2Pubsub2Instance")}
;function Hh(a){uh.call(this,1,arguments);this.csn=a}
t(Hh,uh);var Dh=new vh("screen-created",Hh),Ih=[],Jh=0;function Kh(a,b,c){var d=R("use_default_events_client")?void 0:sg;b={csn:a,parentVe:jh(b),childVes:Pa(c,function(f){return jh(f)})};
c=q(c);for(var e=c.next();!e.done;e=c.next())e=jh(e.value),($a(e)||!e.trackingParams&&!e.veType)&&Bg(Error("Child VE logged with no data"),"WARNING");c={da:rh(a),P:a};"UNDEFINED_CSN"==a?Lh("visualElementAttached",b,c):d?ig("visualElementAttached",b,d,c):tg("visualElementAttached",b,c)}
function Lh(a,b,c){Ih.push({payloadName:a,payload:b,options:c});Jh||(Jh=Eh())}
function Fh(a){if(Ih){for(var b=q(Ih),c=b.next();!c.done;c=b.next())c=c.value,c.payload&&(c.payload.csn=a.csn,ig(c.payloadName,c.payload,null,c.options));Ih.length=0}Jh=0}
;function Mh(a){a=a||{};var b={},c={};this.url=a.url||"";this.args=a.args||cb(b);this.assets=a.assets||{};this.attrs=a.attrs||cb(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
Mh.prototype.clone=function(){var a=new Mh,b;for(b in this)if(this.hasOwnProperty(b)){var c=this[b];"object"==za(c)?a[b]=cb(c):a[b]=c}return a};function Nh(){M.call(this);this.f=[]}
t(Nh,M);Nh.prototype.o=function(){for(;this.f.length;){var a=this.f.pop();a.target.removeEventListener(a.name,a.pb)}M.prototype.o.call(this)};var Oh=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function Ph(a){a=a||"";if(window.spf){var b=a.match(Oh);spf.style.load(a,b?b[1]:"",void 0)}else Qh(a)}
function Qh(a){var b=Rh(a),c=document.getElementById(b),d=c&&Gg(c,"loaded");d||c&&!d||(c=Sh(a,b,function(){Gg(c,"loaded")||(Eg(c),of(b),S(Ka(pf,b),0))}))}
function Sh(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Bc(a);d.rel="stylesheet";d.href=ob(a).toString();(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function Rh(a){var b=xc(document,"A");Mb(b,new G(yb,a));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+Pb(a)}
;function Th(a,b,c,d){M.call(this);var e=this;this.m=this.X=a;this.U=b;this.w=!1;this.api={};this.V=this.D=null;this.F=new O;Ic(this,Ka(Jc,this.F));this.j={};this.R=this.W=this.h=this.ca=this.f=null;this.K=!1;this.l=this.A=null;this.Y={};this.ua=["onReady"];this.ba=null;this.ka=NaN;this.S={};this.i=d;Uh(this);this.Z("WATCH_LATER_VIDEO_ADDED",this.Ma.bind(this));this.Z("WATCH_LATER_VIDEO_REMOVED",this.Na.bind(this));this.Z("onAdAnnounce",this.wa.bind(this));this.va=new Nh(this);Ic(this,Ka(Jc,this.va));
this.T=0;c?this.T=S(function(){e.loadNewVideoConfig(c)},0):d&&(Vh(this),Wh(this))}
t(Th,M);n=Th.prototype;n.getId=function(){return this.U};
n.loadNewVideoConfig=function(a){if(!this.g){this.T&&(T(this.T),this.T=0);a instanceof Mh||(a=new Mh(a));this.ca=a;this.f=a.clone();Vh(this);this.W||(this.W=Xh(this,this.f.args.jsapicallback||"onYouTubePlayerReady"));this.f.args.jsapicallback=null;if(a=this.f.attrs.width)this.m.style.width=Lc(Number(a)||a);if(a=this.f.attrs.height)this.m.style.height=Lc(Number(a)||a);Wh(this);this.w&&Yh(this)}};
function Vh(a){var b;a.i?b=a.i.rootElementId:b=a.f.attrs.id;a.h=b||a.h;"video-player"==a.h&&(a.h=a.U,a.f.attrs.id=a.U);a.m.id==a.h&&(a.h+="-player",a.f.attrs.id=a.h)}
n.Ba=function(){return this.ca};
function Yh(a){a.f&&!a.f.loaded&&(a.f.loaded=!0,"0"!=a.f.args.autoplay?a.api.loadVideoByPlayerVars(a.f.args):a.api.cueVideoByPlayerVars(a.f.args))}
function Zh(a){var b=!0,c=$h(a);c&&a.f&&(a=ai(a),b=Gg(c,"version")===a);return b&&!!z("yt.player.Application.create")}
function Wh(a){if(!a.g&&!a.K){var b=Zh(a);if(b&&"html5"==($h(a)?"html5":null))a.R="html5",a.w||bi(a);else if(ci(a),a.R="html5",b&&a.l)a.X.appendChild(a.l),bi(a);else{a.f&&(a.f.loaded=!0);var c=!1;a.A=function(){c=!0;if(a.i)var d=a.i.serializedExperimentFlags;else a.f&&a.f.args&&(d=a.f.args.fflags);d="true"==ye(d||"").player_bootstrap_method?z("yt.player.Application.createAlternate")||z("yt.player.Application.create"):z("yt.player.Application.create");var e=a.f?a.f.clone():void 0;d(a.X,e,a.i);bi(a)};
a.K=!0;b?a.A():(Kg(ai(a),a.A),(b=a.i?a.i.cssUrl:a.f.assets.css)&&Ph(b),di(a)&&!c&&y("yt.player.Application.create",null,void 0))}}}
function $h(a){var b=tc(a.h);!b&&a.m&&a.m.querySelector&&(b=a.m.querySelector("#"+a.h));return b}
function bi(a){if(!a.g){var b=$h(a),c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);c?(a.K=!1,b.isNotServable&&a.f&&b.isNotServable(a.f.args.video_id)||ei(a)):a.ka=S(function(){bi(a)},50)}}
function ei(a){Uh(a);a.w=!0;var b=$h(a);b.addEventListener&&(a.D=fi(a,b,"addEventListener"));b.removeEventListener&&(a.V=fi(a,b,"removeEventListener"));var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=0;d<c.length;d++){var e=c[d];a.api[e]||(a.api[e]=fi(a,b,e))}for(var f in a.j)a.D(f,a.j[f]);Yh(a);a.W&&a.W(a.api);a.F.M("onReady",a.api)}
function fi(a,b,c){var d=b[c];return function(){try{return a.ba=null,d.apply(b,arguments)}catch(e){"sendAbandonmentPing"!=c&&(e.params=c,a.ba=e,ue(e))}}}
function Uh(a){a.w=!1;if(a.V)for(var b in a.j)a.V(b,a.j[b]);for(var c in a.S)T(parseInt(c,10));a.S={};a.D=null;a.V=null;for(var d in a.api)a.api[d]=null;a.api.addEventListener=a.Z.bind(a);a.api.removeEventListener=a.Ra.bind(a);a.api.destroy=a.dispose.bind(a);a.api.getLastError=a.Ca.bind(a);a.api.getPlayerType=a.Da.bind(a);a.api.getCurrentVideoConfig=a.Ba.bind(a);a.api.loadNewVideoConfig=a.loadNewVideoConfig.bind(a);a.api.isReady=a.La.bind(a)}
n.La=function(){return this.w};
n.Z=function(a,b){var c=this,d=Xh(this,b);if(d){if(!(0<=Na(this.ua,a)||this.j[a])){var e=gi(this,a);this.D&&this.D(a,e)}this.F.subscribe(a,d);"onReady"==a&&this.w&&S(function(){d(c.api)},0)}};
n.Ra=function(a,b){if(!this.g){var c=Xh(this,b);c&&Wd(this.F,a,c)}};
function Xh(a,b){var c=b;if("string"==typeof b){if(a.Y[b])return a.Y[b];c=function(){var d=z(b);d&&d.apply(x,arguments)};
a.Y[b]=c}return c?c:null}
function gi(a,b){var c="ytPlayer"+b+a.U;a.j[b]=c;x[c]=function(d){var e=S(function(){if(!a.g){a.F.M(b,d);var f=a.S,g=String(e);g in f&&delete f[g]}},0);
ab(a.S,String(e))};
return c}
n.wa=function(a){of("a11y-announce",a)};
n.Ma=function(a){of("WATCH_LATER_VIDEO_ADDED",a)};
n.Na=function(a){of("WATCH_LATER_VIDEO_REMOVED",a)};
n.Da=function(){return this.R||($h(this)?"html5":null)};
n.Ca=function(){return this.ba};
function ci(a){a.cancel();Uh(a);a.R=null;a.f&&(a.f.loaded=!1);var b=$h(a);b&&(Zh(a)||!di(a)?a.l=b:(b&&b.destroy&&b.destroy(),a.l=null));for(a=a.X;b=a.firstChild;)a.removeChild(b)}
n.cancel=function(){this.A&&Qg(ai(this),this.A);T(this.ka);this.K=!1};
n.o=function(){ci(this);if(this.l&&this.f&&this.l.destroy)try{this.l.destroy()}catch(b){te(b)}this.Y=null;for(var a in this.j)x[this.j[a]]=null;this.ca=this.f=this.api=null;delete this.X;delete this.m;M.prototype.o.call(this)};
function di(a){return a.f&&a.f.args&&a.f.args.fflags?-1!=a.f.args.fflags.indexOf("player_destroy_old_version=true"):!1}
function ai(a){return a.i?a.i.jsUrl:a.f.assets.js}
;var hi={},ii="player_uid_"+(1E9*Math.random()>>>0);function ji(a){delete hi[a.getId()]}
;function ki(a,b){uh.call(this,1,arguments)}
t(ki,uh);function li(a,b){uh.call(this,1,arguments)}
t(li,uh);var mi=new vh("aft-recorded",ki),ni=new vh("timing-sent",li);var oi=window;function pi(){this.timing={};this.clearResourceTimings=function(){};
this.webkitClearResourceTimings=function(){};
this.mozClearResourceTimings=function(){};
this.msClearResourceTimings=function(){};
this.oClearResourceTimings=function(){}}
var X=oi.performance||oi.mozPerformance||oi.msPerformance||oi.webkitPerformance||new pi;var qi=!1;function ri(a){var b=si(a);if(b.aft)return b.aft;a=Q((a||"")+"TIMING_AFT_KEYS",["ol"]);for(var c=a.length,d=0;d<c;d++){var e=b[a[d]];if(e)return e}return NaN}
function ti(a){var b;(b=z("ytcsi."+(a||"")+"data_"))||(b={tick:{},info:{}},La("ytcsi."+(a||"")+"data_",b));return b}
function ui(a){a=ti(a);a.info||(a.info={});return a.info}
function si(a){a=ti(a);a.tick||(a.tick={});return a.tick}
function vi(a){var b=ti(a).nonce;b||(b=fh(),ti(a).nonce=b);return b}
function wi(a){var b=si(a||""),c=ri(a);c&&!qi&&(Ah(mi,new ki(Math.round(c-b._start),a)),qi=!0)}
;function xi(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];if(!yi(a)||c.some(function(e){return!yi(e)}))throw Error("Only objects may be merged.");
c=q(c);for(d=c.next();!d.done;d=c.next())zi(a,d.value);return a}
function zi(a,b){for(var c in b)if(yi(b[c])){if(c in a&&!yi(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});zi(a[c],b[c])}else if(Ai(b[c])){if(c in a&&!Ai(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);Bi(a[c],b[c])}else a[c]=b[c];return a}
function Bi(a,b){for(var c=q(b),d=c.next();!d.done;d=c.next())d=d.value,yi(d)?a.push(zi({},d)):Ai(d)?a.push(Bi([],d)):a.push(d);return a}
function yi(a){return"object"===typeof a&&!Array.isArray(a)}
function Ai(a){return"object"===typeof a&&Array.isArray(a)}
;function Ci(){var a=z("ytcsi.debug");a||(a=[],y("ytcsi.debug",a,void 0),y("ytcsi.reference",{},void 0));return a}
function Di(a){a=a||"";var b=z("ytcsi.reference");b||(Ci(),b=z("ytcsi.reference"));if(b[a])return b[a];var c=Ci(),d={timerName:a,info:{},tick:{}};c.push(d);return b[a]=d}
;var Ei=z("ytLoggingLatencyUsageStats_")||{};y("ytLoggingLatencyUsageStats_",Ei,void 0);function Fi(){this.f=0}
function Gi(){Fi.instance||(Fi.instance=new Fi);return Fi.instance}
Fi.prototype.tick=function(a,b,c){Hi(this,"tick_"+a+"_"+b)||tg("latencyActionTicked",{tickName:a,clientActionNonce:b},{timestamp:c})};
Fi.prototype.info=function(a,b){var c=Object.keys(a).join("");Hi(this,"info_"+c+"_"+b)||(a.clientActionNonce=b,tg("latencyActionInfo",a))};
function Hi(a,b){Ei[b]=Ei[b]||{count:0};var c=Ei[b];c.count++;c.time=U();a.f||(a.f=ag(function(){var d=U(),e;for(e in Ei)Ei[e]&&6E4<d-Ei[e].time&&delete Ei[e];a&&(a.f=0)},0,5E3));
return 5<c.count?(6===c.count&&1>1E5*Math.random()&&(c=new vg("CSI data exceeded logging limit with key",b),0===b.indexOf("info")?yg(c):zg(c)),!0):!1}
;var Y={},Ii=(Y.ad_allowed="adTypesAllowed",Y.yt_abt="adBreakType",Y.ad_cpn="adClientPlaybackNonce",Y.ad_docid="adVideoId",Y.yt_ad_an="adNetworks",Y.ad_at="adType",Y.browse_id="browseId",Y.p="httpProtocol",Y.t="transportProtocol",Y.cpn="clientPlaybackNonce",Y.ccs="creatorInfo.creatorCanaryState",Y.cseg="creatorInfo.creatorSegment",Y.csn="clientScreenNonce",Y.docid="videoId",Y.GetHome_rid="requestId",Y.GetSearch_rid="requestId",Y.GetPlayer_rid="requestId",Y.GetWatchNext_rid="requestId",Y.GetBrowse_rid=
"requestId",Y.GetLibrary_rid="requestId",Y.is_continuation="isContinuation",Y.is_nav="isNavigation",Y.b_p="kabukiInfo.browseParams",Y.is_prefetch="kabukiInfo.isPrefetch",Y.is_secondary_nav="kabukiInfo.isSecondaryNav",Y.prev_browse_id="kabukiInfo.prevBrowseId",Y.query_source="kabukiInfo.querySource",Y.voz_type="kabukiInfo.vozType",Y.yt_lt="loadType",Y.mver="creatorInfo.measurementVersion",Y.yt_ad="isMonetized",Y.nr="webInfo.navigationReason",Y.nrsu="navigationRequestedSameUrl",Y.ncnp="webInfo.nonPreloadedNodeCount",
Y.pnt="performanceNavigationTiming",Y.prt="playbackRequiresTap",Y.plt="playerInfo.playbackType",Y.pis="playerInfo.playerInitializedState",Y.paused="playerInfo.isPausedOnLoad",Y.yt_pt="playerType",Y.fmt="playerInfo.itag",Y.yt_pl="watchInfo.isPlaylist",Y.yt_pre="playerInfo.preloadType",Y.yt_ad_pr="prerollAllowed",Y.pa="previousAction",Y.yt_red="isRedSubscriber",Y.rce="mwebInfo.responseContentEncoding",Y.scrh="screenHeight",Y.scrw="screenWidth",Y.st="serverTimeMs",Y.aq="tvInfo.appQuality",Y.br_trs="tvInfo.bedrockTriggerState",
Y.kebqat="kabukiInfo.earlyBrowseRequestInfo.abandonmentType",Y.kebqa="kabukiInfo.earlyBrowseRequestInfo.adopted",Y.label="tvInfo.label",Y.is_mdx="tvInfo.isMdx",Y.preloaded="tvInfo.isPreloaded",Y.upg_player_vis="playerInfo.visibilityState",Y.query="unpluggedInfo.query",Y.upg_chip_ids_string="unpluggedInfo.upgChipIdsString",Y.yt_vst="videoStreamType",Y.vph="viewportHeight",Y.vpw="viewportWidth",Y.yt_vis="isVisible",Y.rcl="mwebInfo.responseContentLength",Y.GetSettings_rid="requestId",Y.GetTrending_rid=
"requestId",Y.GetMusicSearchSuggestions_rid="requestId",Y.REQUEST_ID="requestId",Y),Ji="isContinuation isNavigation kabukiInfo.earlyBrowseRequestInfo.adopted kabukiInfo.isPrefetch kabukiInfo.isSecondaryNav isMonetized navigationRequestedSameUrl performanceNavigationTiming playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber tvInfo.isMdx tvInfo.isPreloaded isVisible watchInfo.isPlaylist playbackRequiresTap".split(" "),Ki={},Li=(Ki.ccs="CANARY_STATE_",Ki.mver="MEASUREMENT_VERSION_",Ki.pis="PLAYER_INITIALIZED_STATE_",
Ki.yt_pt="LATENCY_PLAYER_",Ki.pa="LATENCY_ACTION_",Ki.yt_vst="VIDEO_STREAM_TYPE_",Ki),Mi="all_vc ap c cver cbrand cmodel cplatform ctheme ei l_an l_mm plid srt yt_fss yt_li vpst vpni2 vpil2 icrc icrt pa GetAccountOverview_rid GetHistory_rid cmt d_vpct d_vpnfi d_vpni nsru pc pfa pfeh pftr pnc prerender psc rc start tcrt tcrc ssr vpr vps yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis ytu_pvis yt_ref yt_sts tds".split(" ");function Ni(a){return!!Q("FORCE_CSI_ON_GEL",!1)||R("csi_on_gel")||!!ti(a).useGel}
function Oi(a){a=ti(a);if(!("gel"in a))a.gel={gelTicks:{},gelInfos:{}};else if(a.gel){var b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}return a.gel}
;function Pi(a,b,c){if(null!==b)if(ui(c)[a]=b,Ni(c)){var d=b;b=Oi(c);if(b.gelInfos)b.gelInfos["info_"+a]=!0;else{var e={};b.gelInfos=(e["info_"+a]=!0,e)}if(a in Ii){if(a.match("_rid")){var f=a.split("_rid")[0];a="REQUEST_ID"}b=Ii[a];0<=Na(Ji,b)&&(d=!!d);a in Li&&"string"===typeof d&&(d=Li[a]+d.toUpperCase());a=d;d=b.split(".");for(var g=e={},h=0;h<d.length-1;h++){var k=d[h];g[k]={};g=g[k]}g[d[d.length-1]]="requestId"===b?[{id:a,endpoint:f}]:a;f=xi({},e)}else 0<=Na(Mi,a)||yg(new vg("Unknown label logged with GEL CSI",
a)),f=void 0;f&&Ni(c)&&(b=Di(c||""),xi(b.info,f),b=Oi(c),"gelInfos"in b||(b.gelInfos={}),xi(b.gelInfos,f),c=vi(c),Gi().info(f,c))}else Di(c||"").info[a]=b}
if(R("overwrite_polyfill_on_logging_lib_loaded")){var Qi=window;Qi.ytcsi&&(Qi.ytcsi.info=Pi)};function Ri(a,b,c){var d=si(c),e;if(e=R("use_first_tick"))e=si(c),e=a in e;if(e)return d[a];b||"_"==a[0]||(e=a,X.mark&&(0==e.lastIndexOf("mark_",0)||(e="mark_"+e),c&&(e+=" ("+c+")"),X.mark(e)));e=b||U();d[a]=e;e=Oi(c);e.gelTicks&&(e.gelTicks["tick_"+a]=!0);c||b||U();if(Ni(c)){Di(c||"").tick[a]=b||U();e=vi(c);if("_start"===a){var f=Gi();Hi(f,"baseline_"+e)||tg("latencyActionBaselined",{clientActionNonce:e},{timestamp:b})}else Gi().tick(a,e,b);wi(c);e=!0}else e=!1;if(!e){if(!z("yt.timing."+(c||"")+
"pingSent_")&&(f=Q((c||"")+"TIMING_ACTION",void 0),e=si(c),z("ytglobal.timing"+(c||"")+"ready_")&&f&&e._start&&ri(c)))if(wi(c),c)Si(c);else{f=!0;var g=Q("TIMING_WAIT",[]);if(g.length)for(var h=0,k=g.length;h<k;++h)if(!(g[h]in e)){f=!1;break}f&&Si(c)}Di(c||"").tick[a]=b||U()}return d[a]}
function Si(a){if(!Ni(a)){var b=si(a),c=ui(a),d=b._start,e=Q("CSI_SERVICE_NAME","youtube"),f={v:2,s:e,action:Q((a||"")+"TIMING_ACTION",void 0)},g=c.srt;void 0!==b.srt&&delete c.srt;if(c.h5jse){var h=window.location.protocol+z("ytplayer.config.assets.js");(h=X.getEntriesByName?X.getEntriesByName(h)[0]:void 0)?c.h5jse=Math.round(c.h5jse-h.responseEnd):delete c.h5jse}b.aft=ri(a);var k=si(a);h=k.pbr;var l=k.vc;k=k.pbs;h&&l&&k&&h<l&&l<k&&ui(a).yt_pvis&&"youtube"==e&&(Pi("yt_lt","hot_bg",a),e=b.vc,h=b.pbs,
delete b.aft,c.aft=Math.round(h-e));for(var m in c)"_"!=m.charAt(0)&&(f[m]=c[m]);b.ps=U();m={};e=[];for(var p in b)"_"!=p.charAt(0)&&(h=Math.round(b[p]-d),m[p]=h,e.push(p+"."+h));f.rt=e.join(",");(b=z("ytdebug.logTiming"))&&b(f,m);c=!!c.ap;R("debug_csi_data")&&(b=z("yt.timing.csiData"),b||(b=[],La("yt.timing.csiData",b)),b.push({page:location.href,time:new Date,args:f}));b="";for(var v in f)f.hasOwnProperty(v)&&(b+="&"+v+"="+f[v]);f="/csi_204?"+b.substring(1);if(window.navigator&&window.navigator.sendBeacon&&
c){var r=void 0===r?"":r;ff(f,r)||cf(f,void 0,void 0,void 0,r)}else cf(f);y("yt.timing."+(a||"")+"pingSent_",!0,void 0);Ah(ni,new li(m.aft+(g||0),a))}}
A(X.clearResourceTimings||X.webkitClearResourceTimings||X.mozClearResourceTimings||X.msClearResourceTimings||X.oClearResourceTimings||xa,X);var Ti=window;R("csi_on_gel")&&Ti.ytcsi&&(Ti.ytcsi.tick=Ri);function Ui(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function Vi(a,b,c){"string"===typeof a&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});a:{if((b=a.mediaContentUrl)&&(b=/\/([ve]|embed)\/([^#?]+)/.exec(b))&&b[2]){b=b[2];break a}b=null}a.videoId=b;return Wi(a)}
function Wi(a,b,c){if("string"===typeof a)return{videoId:a,startSeconds:b,suggestedQuality:c};b=["endSeconds","startSeconds","mediaContentUrl","suggestedQuality","videoId"];c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}
function Xi(a,b,c,d){if(Da(a)&&!Aa(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};"string"===typeof a&&16===a.length?b.list="PL"+a:b.playlist=a;return b}
;function Yi(a){a=void 0===a?!1:a;M.call(this);this.f=new O(a);Ic(this,Ka(Jc,this.f))}
D(Yi,M);Yi.prototype.subscribe=function(a,b,c){return this.g?0:this.f.subscribe(a,b,c)};
Yi.prototype.j=function(a,b){this.g||this.f.M.apply(this.f,arguments)};function Zi(a,b,c){Yi.call(this);this.h=a;this.i=b;this.l=c}
t(Zi,Yi);function $i(a,b,c){if(!a.g){var d=a.h;d.g||a.i!=d.f||(a={id:a.l,command:b},c&&(a.data=c),d.f.postMessage(yd(a),d.i))}}
Zi.prototype.o=function(){this.i=this.h=null;Yi.prototype.o.call(this)};function aj(a){M.call(this);this.f=a;this.f.subscribe("command",this.sa,this);this.h={};this.j=!1}
t(aj,M);n=aj.prototype;n.start=function(){this.j||this.g||(this.j=!0,$i(this.f,"RECEIVING"))};
n.sa=function(a,b,c){if(this.j&&!this.g){var d=b||{};switch(a){case "addEventListener":"string"===typeof d.event&&(a=d.event,a in this.h||(c=A(this.Ta,this,a),this.h[a]=c,this.addEventListener(a,c)));break;case "removeEventListener":"string"===typeof d.event&&bj(this,d.event);break;default:this.i.isReady()&&this.i.isExternalMethodAvailable(a,c||null)&&(b=cj(a,b||{}),c=this.i.handleExternalCall(a,b,c||null),(c=dj(a,c))&&this.j&&!this.g&&$i(this.f,a,c))}}};
n.Ta=function(a,b){this.j&&!this.g&&$i(this.f,a,this.fa(a,b))};
n.fa=function(a,b){if(null!=b)return{value:b}};
function bj(a,b){b in a.h&&(a.removeEventListener(b,a.h[b]),delete a.h[b])}
n.o=function(){var a=this.f;a.g||Wd(a.f,"command",this.sa,this);this.f=null;for(var b in this.h)bj(this,b);M.prototype.o.call(this)};function ej(a,b){aj.call(this,b);this.i=a;this.start()}
t(ej,aj);ej.prototype.addEventListener=function(a,b){this.i.addEventListener(a,b)};
ej.prototype.removeEventListener=function(a,b){this.i.removeEventListener(a,b)};
function cj(a,b){switch(a){case "loadVideoById":return b=Wi(b),[b];case "cueVideoById":return b=Wi(b),[b];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return b=Xi(b),[b];case "cuePlaylist":return b=Xi(b),[b];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];
case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function dj(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
ej.prototype.fa=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return aj.prototype.fa.call(this,a,b)};
ej.prototype.o=function(){aj.prototype.o.call(this);delete this.i};function fj(a,b,c){M.call(this);var d=this;c=c||Q("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname;this.h=b||null;this.w="*";this.i=c;this.sessionId=null;this.channel="widget";this.A=!!a;this.m=function(e){a:if(!("*"!=d.i&&e.origin!=d.i||d.h&&e.source!=d.h||"string"!==typeof e.data)){try{var f=JSON.parse(e.data)}catch(g){break a}if(!(null==f||d.A&&(d.sessionId&&d.sessionId!=f.id||d.channel&&d.channel!=f.channel))&&f)switch(f.event){case "listening":"null"!=
e.origin&&(d.i=d.w=e.origin);d.h=e.source;d.sessionId=f.id;d.f&&(d.f(),d.f=null);break;case "command":d.j&&(!d.l||0<=Na(d.l,f.func))&&d.j(f.func,f.args,e.origin)}}};
this.l=this.f=this.j=null;window.addEventListener("message",this.m)}
t(fj,M);fj.prototype.sendMessage=function(a,b){var c=b||this.h;if(c){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var d=JSON.stringify(a);c.postMessage(d,this.w)}catch(e){ue(e)}}};
fj.prototype.o=function(){window.removeEventListener("message",this.m);M.prototype.o.call(this)};function gj(){var a=this.g=new fj(!!Q("WIDGET_ID_ENFORCE")),b=A(this.Qa,this);a.j=b;a.l=null;this.g.channel="widget";if(a=Q("WIDGET_ID"))this.g.sessionId=a;this.i=[];this.l=!1;this.j={}}
n=gj.prototype;n.Qa=function(a,b,c){"addEventListener"==a&&b?(a=b[0],this.j[a]||"onReady"==a||(this.addEventListener(a,hj(this,a)),this.j[a]=!0)):this.na(a,b,c)};
n.na=function(){};
function hj(a,b){return A(function(c){this.sendMessage(b,c)},a)}
n.addEventListener=function(){};
n.Aa=function(){this.l=!0;this.sendMessage("initialDelivery",this.ga());this.sendMessage("onReady");F(this.i,this.ta,this);this.i=[]};
n.ga=function(){return null};
function ij(a,b){a.sendMessage("infoDelivery",b)}
n.ta=function(a){this.l?this.g.sendMessage(a):this.i.push(a)};
n.sendMessage=function(a,b){this.ta({event:a,info:void 0==b?null:b})};
n.dispose=function(){this.g=null};function jj(a){gj.call(this);this.f=a;this.h=[];this.addEventListener("onReady",A(this.Oa,this));this.addEventListener("onVideoProgress",A(this.Xa,this));this.addEventListener("onVolumeChange",A(this.Ya,this));this.addEventListener("onApiChange",A(this.Sa,this));this.addEventListener("onPlaybackQualityChange",A(this.Ua,this));this.addEventListener("onPlaybackRateChange",A(this.Va,this));this.addEventListener("onStateChange",A(this.Wa,this));this.addEventListener("onWebglSettingsChanged",A(this.Za,
this))}
t(jj,gj);n=jj.prototype;n.na=function(a,b,c){if(this.f.isExternalMethodAvailable(a,c)){b=b||[];if(0<b.length&&Ui(a)){var d=b;if(Da(d[0])&&!Aa(d[0]))d=d[0];else{var e={};switch(a){case "loadVideoById":case "cueVideoById":e=Wi.apply(window,d);break;case "loadVideoByUrl":case "cueVideoByUrl":e=Vi.apply(window,d);break;case "loadPlaylist":case "cuePlaylist":e=Xi.apply(window,d)}d=e}b.length=1;b[0]=d}this.f.handleExternalCall(a,b,c);Ui(a)&&ij(this,this.ga())}};
n.Oa=function(){var a=A(this.Aa,this);this.g.f=a};
n.addEventListener=function(a,b){this.h.push({eventType:a,listener:b});this.f.addEventListener(a,b)};
n.ga=function(){if(!this.f)return null;var a=this.f.getApiInterface();Sa(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c];if(0===e.search("get")||0===e.search("is")){var f=0;0===e.search("get")?f=3:0===e.search("is")&&(f=2);f=e.charAt(f).toLowerCase()+e.substr(f+1);try{var g=this.f[e]();b[f]=g}catch(h){}}}b.videoData=this.f.getVideoData();b.currentTimeLastUpdated_=C()/1E3;return b};
n.Wa=function(a){a={playerState:a,currentTime:this.f.getCurrentTime(),duration:this.f.getDuration(),videoData:this.f.getVideoData(),videoStartBytes:0,videoBytesTotal:this.f.getVideoBytesTotal(),videoLoadedFraction:this.f.getVideoLoadedFraction(),playbackQuality:this.f.getPlaybackQuality(),availableQualityLevels:this.f.getAvailableQualityLevels(),currentTimeLastUpdated_:C()/1E3,playbackRate:this.f.getPlaybackRate(),mediaReferenceTime:this.f.getMediaReferenceTime()};this.f.getVideoUrl&&(a.videoUrl=
this.f.getVideoUrl());this.f.getVideoContentRect&&(a.videoContentRect=this.f.getVideoContentRect());this.f.getProgressState&&(a.progressState=this.f.getProgressState());this.f.getPlaylist&&(a.playlist=this.f.getPlaylist());this.f.getPlaylistIndex&&(a.playlistIndex=this.f.getPlaylistIndex());this.f.getStoryboardFormat&&(a.storyboardFormat=this.f.getStoryboardFormat());ij(this,a)};
n.Ua=function(a){ij(this,{playbackQuality:a})};
n.Va=function(a){ij(this,{playbackRate:a})};
n.Sa=function(){for(var a=this.f.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.f.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],l=this.f.getOption(e,k);b[e][k]=l}}this.sendMessage("apiInfoDelivery",b)};
n.Ya=function(){ij(this,{muted:this.f.isMuted(),volume:this.f.getVolume()})};
n.Xa=function(a){a={currentTime:a,videoBytesLoaded:this.f.getVideoBytesLoaded(),videoLoadedFraction:this.f.getVideoLoadedFraction(),currentTimeLastUpdated_:C()/1E3,playbackRate:this.f.getPlaybackRate(),mediaReferenceTime:this.f.getMediaReferenceTime()};this.f.getProgressState&&(a.progressState=this.f.getProgressState());ij(this,a)};
n.Za=function(){var a={sphericalProperties:this.f.getSphericalProperties()};ij(this,a)};
n.dispose=function(){gj.prototype.dispose.call(this);for(var a=0;a<this.h.length;a++){var b=this.h[a];this.f.removeEventListener(b.eventType,b.listener)}this.h=[]};function kj(a,b,c){M.call(this);this.f=a;this.i=c;this.j=W(window,"message",A(this.l,this));this.h=new Zi(this,a,b);Ic(this,Ka(Jc,this.h))}
t(kj,M);kj.prototype.l=function(a){var b;if(b=!this.g)if(b=a.origin==this.i)a:{b=this.f;do{b:{var c=a.source;do{if(c==b){c=!0;break b}if(c==c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,"string"===typeof b)){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.h,c.g||c.j("command",b.command,b.data,a.origin))}};
kj.prototype.o=function(){Wf(this.j);this.f=null;M.prototype.o.call(this)};function lj(){var a=cb(mj),b;return Ld(new N(function(c,d){a.onSuccess=function(e){Le(e)?c(e):d(new nj("Request failed, status="+(e&&"status"in e?e.status:-1),"net.badstatus",e))};
a.onError=function(e){d(new nj("Unknown request error","net.unknown",e))};
a.O=function(e){d(new nj("Request timed out","net.timeout",e))};
b=Ve("//googleads.g.doubleclick.net/pagead/id",a)}),function(c){c instanceof Md&&b.abort();
return Jd(c)})}
function nj(a,b){E.call(this,a+", errorCode="+b);this.errorCode=b;this.name="PromiseAjaxError"}
t(nj,E);function oj(){this.g=0;this.f=null}
oj.prototype.then=function(a,b,c){return 1===this.g&&a?(a=a.call(c,this.f),Ed(a)?a:pj(a)):2===this.g&&b?(a=b.call(c,this.f),Ed(a)?a:qj(a)):this};
oj.prototype.getValue=function(){return this.f};
oj.prototype.$goog_Thenable=!0;function qj(a){var b=new oj;a=void 0===a?null:a;b.g=2;b.f=void 0===a?null:a;return b}
function pj(a){var b=new oj;a=void 0===a?null:a;b.g=1;b.f=void 0===a?null:a;return b}
;function rj(a){E.call(this,a.message||a.description||a.name);this.isMissing=a instanceof sj;this.isTimeout=a instanceof nj&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof Md}
t(rj,E);rj.prototype.name="BiscottiError";function sj(){E.call(this,"Biscotti ID is missing from server")}
t(sj,E);sj.prototype.name="BiscottiMissingError";var mj={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},tj=null;function we(){if("1"===Xa(oe(),"args","privembed"))return Jd(Error("Biscotti ID is not available in private embed mode"));tj||(tj=Ld(lj().then(uj),function(a){return vj(2,a)}));
return tj}
function uj(a){a=a.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new sj;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new sj;a=a.id;xe(a);tj=pj(a);wj(18E5,2);return a}
function vj(a,b){var c=new rj(b);xe("");tj=qj(c);0<a&&wj(12E4,a-1);throw c;}
function wj(a,b){S(function(){Ld(lj().then(uj,function(c){return vj(b,c)}),xa)},a)}
function xj(){try{var a=z("yt.ads.biscotti.getId_");return a?a():we()}catch(b){return Jd(b)}}
;function yj(a){if("1"!==Xa(oe(),"args","privembed")){a&&ve();try{xj().then(function(){},function(){}),S(yj,18E5)}catch(b){te(b)}}}
;var Z=z("ytglobal.prefsUserPrefsPrefs_")||{};y("ytglobal.prefsUserPrefsPrefs_",Z,void 0);function zj(){this.f=Q("ALT_PREF_COOKIE_NAME","PREF");var a=pc.get(""+this.f,void 0);if(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(Z[d]=c.toString())}}}
n=zj.prototype;n.get=function(a,b){Aj(a);Bj(a);var c=void 0!==Z[a]?Z[a].toString():null;return null!=c?c:b?b:""};
n.set=function(a,b){Aj(a);Bj(a);if(null==b)throw Error("ExpectedNotNull");Z[a]=b.toString()};
n.remove=function(a){Aj(a);Bj(a);delete Z[a]};
n.save=function(){mg(this.f,this.dump(),63072E3)};
n.clear=function(){for(var a in Z)delete Z[a]};
n.dump=function(){var a=[],b;for(b in Z)a.push(b+"="+encodeURIComponent(String(Z[b])));return a.join("&")};
function Bj(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function Aj(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function Cj(a){a=void 0!==Z[a]?Z[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
ya(zj);var Dj=null,Ej=null,Fj=null,Gj={};function Hj(a){var b=a.id;a=a.ve_type;var c=hh++;a=new ih({veType:a,veCounter:c,elementIndex:void 0,dataElement:void 0,youtubeData:void 0});Gj[b]=a;b=ph();c=nh();b&&c&&Kh(b,c,[a])}
function Ij(a){var b=a.csn;a=a.root_ve_type;if(b&&a&&(sh(b,a),a=nh()))for(var c in Gj){var d=Gj[c];d&&Kh(b,a,[d])}}
function Jj(a){Gj[a.id]=new ih({trackingParams:a.tracking_params})}
function Kj(a){var b=ph(),c=Gj[a.id];if(b&&c){a=R("use_default_events_client")?void 0:sg;c={csn:b,ve:jh(c),gestureType:"INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK"};var d={da:rh(b),P:b};"UNDEFINED_CSN"==b?Lh("visualElementGestured",c,d):a?ig("visualElementGestured",c,a,d):tg("visualElementGestured",c,d)}}
function Lj(a){a=a.ids;var b=ph();if(b)for(var c=0;c<a.length;c++){var d=Gj[a[c]];if(d){var e=b,f=R("use_default_events_client")?void 0:sg;d={csn:e,ve:jh(d),eventType:1};var g={da:rh(e),P:e};"UNDEFINED_CSN"==e?Lh("visualElementShown",d,g):f?ig("visualElementShown",d,f,g):tg("visualElementShown",d,g)}}}
;y("yt.setConfig",P,void 0);y("yt.config.set",P,void 0);y("yt.setMsg",Dg,void 0);y("yt.msgs.set",Dg,void 0);y("yt.logging.errors.log",Bg,void 0);
y("writeEmbed",function(){var a=Q("PLAYER_CONFIG",void 0);yj(!0);"gvn"==a.args.ps&&(document.body.style.backgroundColor="transparent");var b=document.referrer,c=Q("POST_MESSAGE_ORIGIN");window!=window.top&&b&&b!=document.URL&&(a.args.loaderUrl=b);Q("LIGHTWEIGHT_AUTOPLAY")&&(a.args.autoplay="1");b="player";var d=void 0===d?!0:d;b="string"===typeof b?tc(b):b;var e=ii+"_"+Ea(b),f=hi[e];f&&d?a&&a.args&&a.args.fflags&&a.args.fflags.includes("web_player_remove_playerproxy=true")?f.api.loadVideoByPlayerVars(a.args||
null):f.loadNewVideoConfig(a):(f=new Th(b,e,a,void 0),hi[e]=f,of("player-added",f.api),Ic(f,Ka(ji,f)));a=f.api;Dj=a;a.addEventListener("onScreenChanged",Ij);a.addEventListener("onLogClientVeCreated",Hj);a.addEventListener("onLogServerVeCreated",Jj);a.addEventListener("onLogVeClicked",Kj);a.addEventListener("onLogVesShown",Lj);d=Q("POST_MESSAGE_ID","player");Q("ENABLE_JS_API")?Fj=new jj(a):Q("ENABLE_POST_API")&&"string"===typeof d&&"string"===typeof c&&(Ej=new kj(window.parent,d,c),Fj=new ej(a,Ej.h));
c=Q("BG_P",void 0);bh(c)&&(Q("BG_I")||Q("BG_IU"))&&(Yg=!0,Xg.initialize(Q("BG_I",null),Q("BG_IU",null),c,ah,void 0,!!Q("BG_CE",!1)));Tg()},void 0);
y("yt.www.watch.ads.restrictioncookie.spr",function(a){cf(a+"mac_204?action_fcts=1");return!0},void 0);
var Mj=se(function(){Ri("ol");var a=zj.getInstance(),b=!!((Cj("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&nd(document.body,"exp-invert-logo"))if(c&&!nd(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!nd(d,"inverted-hdpi")){var e=ld(d);md(d,e+(0<e.length?" inverted-hdpi":"inverted-hdpi"))}}else!c&&nd(document.body,"inverted-hdpi")&&od();b!=c&&(b="f"+(Math.floor(119/31)+1),d=Cj(b)||0,d=c?d|67108864:
d&-67108865,0==d?delete Z[b]:(c=d.toString(16),Z[b]=c.toString()),a.save())}),Nj=se(function(){var a=Dj;
a&&a.sendAbandonmentPing&&a.sendAbandonmentPing();Q("PL_ATT")&&Xg.dispose();a=0;for(var b=Rg.length;a<b;a++){var c=Rg[a];if(!isNaN(c)){var d=z("yt.scheduler.instance.cancelJob");d?d(c):T(c)}}Rg.length=0;Pg("//static.doubleclick.net/instream/ad_status.js");Sg=!1;P("DCLKSTAT",0);Kc(Fj,Ej);if(a=Dj)a.removeEventListener("onScreenChanged",Ij),a.removeEventListener("onLogClientVeCreated",Hj),a.removeEventListener("onLogServerVeCreated",Jj),a.removeEventListener("onLogVeClicked",Kj),a.removeEventListener("onLogVesShown",
Lj),a.destroy();Gj={}});
window.addEventListener?(window.addEventListener("load",Mj),window.addEventListener("unload",Nj)):window.attachEvent&&(window.attachEvent("onload",Mj),window.attachEvent("onunload",Nj));La("yt.abuse.player.botguardInitialized",z("yt.abuse.player.botguardInitialized")||ch);La("yt.abuse.player.invokeBotguard",z("yt.abuse.player.invokeBotguard")||dh);La("yt.abuse.dclkstatus.checkDclkStatus",z("yt.abuse.dclkstatus.checkDclkStatus")||Ug);
La("yt.player.exports.navigate",z("yt.player.exports.navigate")||th);La("yt.util.activity.init",z("yt.util.activity.init")||dg);La("yt.util.activity.getTimeSinceActive",z("yt.util.activity.getTimeSinceActive")||gg);La("yt.util.activity.setTimestamp",z("yt.util.activity.setTimestamp")||eg);}).call(this);
