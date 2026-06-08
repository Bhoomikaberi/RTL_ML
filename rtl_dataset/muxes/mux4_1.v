module mux4_1(
input [3:0] d,
input [1:0] sel,
output y
);

assign y =
(sel==0)?d[0]:
(sel==1)?d[1]:
(sel==2)?d[2]:
d[3];

endmodule