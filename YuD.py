import pandas as pd
import numpy as np
import GTF

try:
    'taking the user input for csv and gtf file'
    user_transcript_file_input = input("Enter transcript file name (file should be in csv format):").lower()
    user_transcript_file_input_split = user_transcript_file_input.split('.')
    if user_transcript_file_input_split[-1] != "csv":
        print("The input file is not recognized, please enter a CSV file")
        quit()
    else:
        df1 = pd.read_csv(user_transcript_file_input)
        print(df1)

    user_gtf_file_input = input("Enter gtf file name (file should be in gtf format):").lower()
    user_gtf_file_input_split = user_gtf_file_input.split('.')
    if user_gtf_file_input_split[-1] != "gtf":
        print("The input file is not recognized, please enter a gtf file")
        quit()
    else:
        df2 = GTF.dataframe(user_gtf_file_input)
        print(df2)

    'taking input and converting integers into KBs'
    user_input_kb = int(input("Enter the number of KBs you want to look UPSTREAM and DOWNSTREAM:"))
    user_input_kb_mul = user_input_kb * 1000

    'indexing transcripts file'
    index1 = df1.index
    last_index1 = index1[-1] + 1

    'inserting values of upstream, start, end, downstream to arrays'
    array_start_values = np.array([], dtype='int64')
    array_upstream_values = np.array([], dtype='int64')
    array_end_values = np.array([], dtype='int64')
    array_downstream_values = np.array([], dtype='int64')

    for i in range(0, last_index1):
        if i == last_index1:
            break
        else:
            start_value = df1.iloc[i, 1]
            end_value = df1.iloc[i, 2]

            if str(start_value).lower() == "nan" or str(end_value).lower() == "nan":
                print("Any start and end site cannot be left empty")
                break
            else:
                upstream_values = start_value - user_input_kb_mul
                downstream_values = end_value + user_input_kb_mul
                array_start_values = np.append(array_start_values, [start_value], axis=0)
                array_upstream_values = np.append(array_upstream_values, [upstream_values], axis=0)
                array_end_values = np.append(array_end_values, [end_value], axis=0)
                array_downstream_values = np.append(array_downstream_values, [downstream_values], axis=0)

    'indexing gtf file'
    index2 = df2.index
    last_index2 = index2[-1] + 1

    df2.start = df2.start.astype('int64')
    df2.end = df2.end.astype('int64')

    'writing results to upstream and downstream files'
    f = open("upstream.csv", "w")
    for i in range(0, last_index1):
        condition1 = df2[(df2['start'] > array_upstream_values[i]) & (df2['start'] < array_start_values[i])]
        condition1.insert(0, '', '')
        sample_transcripts = df1.iloc[i, 0]
        f.write(str(sample_transcripts))
        f.write(condition1.to_csv(index=False))
    f.close()
    f = open("downstream.csv", "w")
    for i in range(0, last_index1):
        condition2 = df2[(df2['end'] > array_upstream_values[i]) & (df2['end'] < array_start_values[i])]
        condition2.insert(0, '', '')
        sample_transcripts = df1.iloc[i, 0]
        f.write(str(sample_transcripts))
        f.write(condition2.to_csv(index=False))
    f.close()
    print("Upstream and Downstream Files have been created")
    input("Press ENTER to EXIT")

except Exception as e:
    print(e)
    input("Press ENTER to EXIT")
