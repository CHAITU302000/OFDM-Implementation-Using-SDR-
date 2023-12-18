	% Read in the two files
	file1 = fopen('OFDM_trans1.txt', 'rb');	
    file2 = fopen('BERreceive.txt', 'rb');
	% Read in the contents of the files as binary data
	data1 = fread(file1, '*ubit1')';
	data2 = fread(file2, '*ubit1')';
% 	data1
%     data2
	% Determine the longer and shorter sequences
	if length(data1) >= length(data2)
	    longer_seq = data1;
	    shorter_seq = data2;
	else
	    longer_seq = data2;
	    shorter_seq = data1;
    end
    b=numel(longer_seq)%1*2022000
    c=mod(b,a);
    b=b-c;
    a=numel(shorter_seq)%1*128
    shorter_seq;
    BER=0;
    num_errors=0;
    i=0;
   while i<b
       for j=1+i:a+i
          diff=longer_seq(1,j)-shorter_seq(1,j-i);
        if diff~=0
            num_errors=num_errors+1; 
        end
       end
       i=i+a;
   end
   BER = num_errors / length(longer_seq);

 	fprintf('Bit Error Rate (BER) = %f\n', BER);
 	
%  Close the files
 	fclose(file1);
 	fclose(file2);
