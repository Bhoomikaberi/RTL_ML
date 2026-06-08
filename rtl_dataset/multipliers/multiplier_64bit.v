module multiplier_64bit(
input [63:0] a,
input [63:0] b,
output [127:0] p
);

assign p = a * b;

endmodule