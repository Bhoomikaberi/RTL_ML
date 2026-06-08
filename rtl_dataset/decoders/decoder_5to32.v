module decoder_5to32(
input [4:0] in,
output [31:0] out
);

assign out = 32'b1 << in;

endmodule