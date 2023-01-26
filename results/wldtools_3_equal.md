(venv) jarda@ux430unr:~/Desktop/roz/project$ python3 wldtools_3_equal.py 
INFO:root:00:49:55
RANDOM_STATE=42
SAMPLES=10000
SIZE=128
T=8
M=4
WEIGHTS=False
S=10
EQUALIZE=True
GREYSCALE=False
INFO:root:Extracting WLD from images
  0%|                                                                                                                                              | 0/10000 [00:00<?, ?it/s]DEBUG:matplotlib:matplotlib data path: /home/jarda/.local/lib/python3.10/site-packages/matplotlib/mpl-data
DEBUG:matplotlib:CONFIGDIR=/home/jarda/r/configs/.config/matplotlib
DEBUG:matplotlib:interactive is False
DEBUG:matplotlib:platform is linux
DEBUG:matplotlib:CACHEDIR=/home/jarda/.cache/matplotlib
DEBUG:matplotlib.font_manager:Using fontManager instance from /home/jarda/.cache/matplotlib/fontlist-v330.json
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [08:36<00:00, 19.36it/s]
INFO:root:---------- TEST SIZE 0.3, TRAIN SIZE 0.7 ---------
INFO:root:00:58:31, round 0, class ('KNN', '1')
INFO:root:01:02:36, round 0, class ('KNN', '3')
INFO:root:01:06:42, round 0, class ('SVM', 'poly(3)')
INFO:root:01:06:53, round 0, class ('SVM', 'rbf')
INFO:root:01:07:08, round 1, class ('KNN', '1')
INFO:root:01:11:09, round 1, class ('KNN', '3')
INFO:root:01:15:08, round 1, class ('SVM', 'poly(3)')
INFO:root:01:15:19, round 1, class ('SVM', 'rbf')
INFO:root:01:15:34, round 2, class ('KNN', '1')
INFO:root:01:19:30, round 2, class ('KNN', '3')
INFO:root:01:23:29, round 2, class ('SVM', 'poly(3)')
INFO:root:01:23:40, round 2, class ('SVM', 'rbf')
INFO:root:01:23:55, round 3, class ('KNN', '1')
INFO:root:01:27:52, round 3, class ('KNN', '3')
INFO:root:01:31:52, round 3, class ('SVM', 'poly(3)')
INFO:root:01:32:02, round 3, class ('SVM', 'rbf')
INFO:root:01:32:18, round 4, class ('KNN', '1')
INFO:root:01:36:14, round 4, class ('KNN', '3')
INFO:root:01:40:12, round 4, class ('SVM', 'poly(3)')
INFO:root:01:40:22, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.3, 'metric': 'BA', ('KNN', '1'): '0.52(+-0.0e+00)', ('KNN', '3'): '0.5(+-0.0e+00)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'TN', ('KNN', '1'): '2.9e+03(+-0.0e+00)', ('KNN', '3'): '2.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '2.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '2.9e+03(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'FP', ('KNN', '1'): '5.2e+01(+-0.0e+00)', ('KNN', '3'): '6.0(+-0.0e+00)', ('SVM', 'poly(3)'): '1.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'FN', ('KNN', '1'): '4.8e+01(+-0.0e+00)', ('KNN', '3'): '5.1e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '5.1e+01(+-0.0e+00)', ('SVM', 'rbf'): '5.1e+01(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'TP', ('KNN', '1'): '3.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
INFO:root:---------- TEST SIZE 0.5, TRAIN SIZE 0.5 ---------
INFO:root:01:40:38, round 0, class ('KNN', '1')
INFO:root:01:45:19, round 0, class ('KNN', '3')
INFO:root:01:50:02, round 0, class ('SVM', 'poly(3)')
INFO:root:01:50:08, round 0, class ('SVM', 'rbf')
INFO:root:01:50:21, round 1, class ('KNN', '1')
INFO:root:01:55:04, round 1, class ('KNN', '3')
INFO:root:01:59:49, round 1, class ('SVM', 'poly(3)')
INFO:root:01:59:56, round 1, class ('SVM', 'rbf')
INFO:root:02:00:08, round 2, class ('KNN', '1')
INFO:root:02:04:50, round 2, class ('KNN', '3')
INFO:root:02:09:34, round 2, class ('SVM', 'poly(3)')
INFO:root:02:09:41, round 2, class ('SVM', 'rbf')
INFO:root:02:09:53, round 3, class ('KNN', '1')
INFO:root:02:14:38, round 3, class ('KNN', '3')
INFO:root:02:19:23, round 3, class ('SVM', 'poly(3)')
INFO:root:02:19:30, round 3, class ('SVM', 'rbf')
INFO:root:02:19:43, round 4, class ('KNN', '1')
INFO:root:02:24:27, round 4, class ('KNN', '3')
INFO:root:02:29:12, round 4, class ('SVM', 'poly(3)')
INFO:root:02:29:19, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.5, 'metric': 'BA', ('KNN', '1'): '0.5(+-0.0e+00)', ('KNN', '3'): '0.5(+-0.0e+00)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'TN', ('KNN', '1'): '4.8e+03(+-0.0e+00)', ('KNN', '3'): '4.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '4.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '4.9e+03(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'FP', ('KNN', '1'): '9.2e+01(+-0.0e+00)', ('KNN', '3'): '1.6e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '3.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'FN', ('KNN', '1'): '8.8e+01(+-0.0e+00)', ('KNN', '3'): '9e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '9e+01(+-0.0e+00)', ('SVM', 'rbf'): '9e+01(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'TP', ('KNN', '1'): '2.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
INFO:root:---------- TEST SIZE 0.7, TRAIN SIZE 0.30000000000000004 ---------
INFO:root:02:29:32, round 0, class ('KNN', '1')
INFO:root:02:33:29, round 0, class ('KNN', '3')
INFO:root:02:37:30, round 0, class ('SVM', 'poly(3)')
INFO:root:02:37:34, round 0, class ('SVM', 'rbf')
INFO:root:02:37:41, round 1, class ('KNN', '1')
INFO:root:02:41:41, round 1, class ('KNN', '3')
INFO:root:02:45:41, round 1, class ('SVM', 'poly(3)')
INFO:root:02:45:45, round 1, class ('SVM', 'rbf')
INFO:root:02:45:52, round 2, class ('KNN', '1')
INFO:root:02:49:52, round 2, class ('KNN', '3')
INFO:root:02:53:53, round 2, class ('SVM', 'poly(3)')
INFO:root:02:53:57, round 2, class ('SVM', 'rbf')
INFO:root:02:54:04, round 3, class ('KNN', '1')
INFO:root:02:58:04, round 3, class ('KNN', '3')
INFO:root:03:00:53, round 3, class ('SVM', 'poly(3)')
INFO:root:03:00:55, round 3, class ('SVM', 'rbf')
INFO:root:03:00:59, round 4, class ('KNN', '1')
INFO:root:03:03:09, round 4, class ('KNN', '3')
INFO:root:03:04:54, round 4, class ('SVM', 'poly(3)')
INFO:root:03:04:56, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.7, 'metric': 'BA', ('KNN', '1'): '0.51(+-0.0e+00)', ('KNN', '3'): '0.51(+-0.0e+00)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'TN', ('KNN', '1'): '6.8e+03(+-0.0e+00)', ('KNN', '3'): '6.8e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '6.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '6.9e+03(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'FP', ('KNN', '1'): '1.1e+02(+-0.0e+00)', ('KNN', '3'): '2.5e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '1.2e+01(+-0.0e+00)', ('SVM', 'rbf'): '1.1e+01(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'FN', ('KNN', '1'): '1.2e+02(+-0.0e+00)', ('KNN', '3'): '1.3e+02(+-0.0e+00)', ('SVM', 'poly(3)'): '1.3e+02(+-0.0e+00)', ('SVM', 'rbf'): '1.3e+02(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'TP', ('KNN', '1'): '5.0(+-0.0e+00)', ('KNN', '3'): '2.0(+-0.0e+00)', ('SVM', 'poly(3)'): '1.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
/home/jarda/Desktop/roz/project/wldtools_3_equal.py:244: FutureWarning: In future versions `DataFrame.to_latex` is expected to utilise the base implementation of `Styler.to_latex` for formatting and rendering. The arguments signature may therefore change. It is recommended instead to use `DataFrame.style.to_latex` which also contains additional functionality.
  print(table.to_latex())
\begin{tabular}{llllll}
\toprule
    &    & \multicolumn{2}{l}{KNN} & \multicolumn{2}{l}{SVM} \\
    &    &                   1 &                   3 &             poly(3) &                 rbf \\
test\_size & metric &                     &                     &                     &                     \\
\midrule
0.3 & BA &     0.52(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) \\
    & FP &  5.2e+01(+-0.0e+00) &      6.0(+-0.0e+00) &      1.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  4.8e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) \\
    & TP &      3.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
0.5 & BA &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  4.8e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) \\
    & FP &  9.2e+01(+-0.0e+00) &  1.6e+01(+-0.0e+00) &      3.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  8.8e+01(+-0.0e+00) &    9e+01(+-0.0e+00) &    9e+01(+-0.0e+00) &    9e+01(+-0.0e+00) \\
    & TP &      2.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
0.7 & BA &     0.51(+-0.0e+00) &     0.51(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  6.8e+03(+-0.0e+00) &  6.8e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) \\
    & FP &  1.1e+02(+-0.0e+00) &  2.5e+01(+-0.0e+00) &  1.2e+01(+-0.0e+00) &  1.1e+01(+-0.0e+00) \\
    & FN &  1.2e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) \\
    & TP &      5.0(+-0.0e+00) &      2.0(+-0.0e+00) &      1.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
\bottomrule
\end{tabular}

