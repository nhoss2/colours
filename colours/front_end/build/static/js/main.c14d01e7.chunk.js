(this.webpackJsonpstatic=this.webpackJsonpstatic||[]).push([[0],{11:function(t,e,c){},13:function(t,e,c){},15:function(t,e,c){"use strict";c.r(e);var n=c(1),r=c.n(n),s=c(4),a=c.n(s),o=(c(11),c(3)),u=c.n(o),i=c(5),j=c(6),l=(c(13),c(0));function p(t){var e=t.colourData;return Object(l.jsx)("div",{className:"colour-box",style:{background:e.css},children:e.css})}var b=function(){var t=Object(n.useState)([]),e=Object(j.a)(t,2),c=e[0],r=e[1],s=function(){var t=Object(i.a)(u.a.mark((function t(){var e,c;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,fetch("/api/get_colours");case 2:return e=t.sent,t.next=5,e.json();case 5:c=t.sent,r(c.colours);case 7:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}();return Object(n.useEffect)((function(){s()}),[]),Object(l.jsxs)("div",{className:"app",children:[Object(l.jsx)("h1",{children:"Colours app"}),Object(l.jsx)("div",{id:"colours-list",children:c.map((function(t,e){return Object(l.jsx)(p,{colourData:t},e)}))})]})};a.a.render(Object(l.jsx)(r.a.StrictMode,{children:Object(l.jsx)(b,{})}),document.getElementById("root"))}},[[15,1,2]]]);
//# sourceMappingURL=main.c14d01e7.chunk.js.map