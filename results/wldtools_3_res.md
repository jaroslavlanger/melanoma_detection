(venv) jarda@ux430unr:~/Desktop/roz/project$ python3 wldtools_3.py 
INFO:root:00:48:07
RANDOM_STATE=42
SAMPLES=10000
SIZE=128
T=8
M=4
WEIGHTS=False
S=10
EQUALIZE=False
GREYSCALE=False
INFO:root:Extracting WLD from images
  0%|                                                                                                                                              | 0/10000 [00:00<?, ?it/s]DEBUG:matplotlib:matplotlib data path: /home/jarda/.local/lib/python3.10/site-packages/matplotlib/mpl-data
DEBUG:matplotlib:CONFIGDIR=/home/jarda/r/configs/.config/matplotlib
DEBUG:matplotlib:interactive is False
DEBUG:matplotlib:platform is linux
DEBUG:matplotlib:CACHEDIR=/home/jarda/.cache/matplotlib
DEBUG:matplotlib.font_manager:Using fontManager instance from /home/jarda/.cache/matplotlib/fontlist-v330.json
  0%|▏                                                                                                                                    | 13/10000 [00:00<08:14, 20.18it/s]/home/jarda/Desktop/roz/project/wldtools_3.py:87: RuntimeWarning: divide by zero encountered in divide
  return np.arctan(np.divide(v00, v01))
  1%|█▏                                                                                                                                   | 90/10000 [00:03<05:08, 32.16it/s]/home/jarda/Desktop/roz/project/wldtools_3.py:87: RuntimeWarning: invalid value encountered in divide
  return np.arctan(np.divide(v00, v01))
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [06:39<00:00, 25.03it/s]
INFO:root:---------- TEST SIZE 0.3, TRAIN SIZE 0.7 ---------
INFO:root:00:54:47, round 0, class ('KNN', '1')
INFO:root:00:58:43, round 0, class ('KNN', '3')
INFO:root:01:02:29, round 0, class ('SVM', 'poly(3)')
INFO:root:01:02:39, round 0, class ('SVM', 'rbf')
INFO:root:01:02:51, round 1, class ('KNN', '1')
INFO:root:01:06:42, round 1, class ('KNN', '3')
INFO:root:01:10:29, round 1, class ('SVM', 'poly(3)')
INFO:root:01:10:38, round 1, class ('SVM', 'rbf')
INFO:root:01:10:49, round 2, class ('KNN', '1')
INFO:root:01:14:40, round 2, class ('KNN', '3')
INFO:root:01:18:29, round 2, class ('SVM', 'poly(3)')
INFO:root:01:18:38, round 2, class ('SVM', 'rbf')
INFO:root:01:18:49, round 3, class ('KNN', '1')
INFO:root:01:22:41, round 3, class ('KNN', '3')
INFO:root:01:26:32, round 3, class ('SVM', 'poly(3)')
INFO:root:01:26:41, round 3, class ('SVM', 'rbf')
INFO:root:01:26:53, round 4, class ('KNN', '1')
INFO:root:01:30:43, round 4, class ('KNN', '3')
INFO:root:01:34:33, round 4, class ('SVM', 'poly(3)')
INFO:root:01:34:42, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.3, 'metric': 'BA', ('KNN', '1'): '0.56(+-0.0e+00)', ('KNN', '3'): '0.5(+-3.9e-33)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'TN', ('KNN', '1'): '2.9e+03(+-0.0e+00)', ('KNN', '3'): '2.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '2.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '2.9e+03(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'FP', ('KNN', '1'): '4.4e+01(+-0.0e+00)', ('KNN', '3'): '2.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'FN', ('KNN', '1'): '4.4e+01(+-0.0e+00)', ('KNN', '3'): '5.1e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '5.1e+01(+-0.0e+00)', ('SVM', 'rbf'): '5.1e+01(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'TP', ('KNN', '1'): '7.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
INFO:root:---------- TEST SIZE 0.5, TRAIN SIZE 0.5 ---------
INFO:root:01:34:53, round 0, class ('KNN', '1')
INFO:root:01:39:22, round 0, class ('KNN', '3')
INFO:root:01:43:53, round 0, class ('SVM', 'poly(3)')
INFO:root:01:43:58, round 0, class ('SVM', 'rbf')
INFO:root:01:44:07, round 1, class ('KNN', '1')
INFO:root:01:48:33, round 1, class ('KNN', '3')
INFO:root:01:53:03, round 1, class ('SVM', 'poly(3)')
INFO:root:01:53:09, round 1, class ('SVM', 'rbf')
INFO:root:01:53:17, round 2, class ('KNN', '1')
INFO:root:01:57:44, round 2, class ('KNN', '3')
INFO:root:02:02:13, round 2, class ('SVM', 'poly(3)')
INFO:root:02:02:18, round 2, class ('SVM', 'rbf')
INFO:root:02:02:27, round 3, class ('KNN', '1')
INFO:root:02:06:55, round 3, class ('KNN', '3')
INFO:root:02:11:25, round 3, class ('SVM', 'poly(3)')
INFO:root:02:11:30, round 3, class ('SVM', 'rbf')
INFO:root:02:11:39, round 4, class ('KNN', '1')
INFO:root:02:16:05, round 4, class ('KNN', '3')
INFO:root:02:20:33, round 4, class ('SVM', 'poly(3)')
INFO:root:02:20:39, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.5, 'metric': 'BA', ('KNN', '1'): '0.54(+-0.0e+00)', ('KNN', '3'): '0.5(+-0.0e+00)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'TN', ('KNN', '1'): '4.8e+03(+-0.0e+00)', ('KNN', '3'): '4.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '4.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '4.9e+03(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'FP', ('KNN', '1'): '8e+01(+-0.0e+00)', ('KNN', '3'): '1.2e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'FN', ('KNN', '1'): '8.1e+01(+-0.0e+00)', ('KNN', '3'): '9e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '9e+01(+-0.0e+00)', ('SVM', 'rbf'): '9e+01(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'TP', ('KNN', '1'): '9.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
INFO:root:---------- TEST SIZE 0.7, TRAIN SIZE 0.30000000000000004 ---------
INFO:root:02:20:47, round 0, class ('KNN', '1')
INFO:root:02:24:28, round 0, class ('KNN', '3')
INFO:root:02:28:15, round 0, class ('SVM', 'poly(3)')
INFO:root:02:28:17, round 0, class ('SVM', 'rbf')
INFO:root:02:28:21, round 1, class ('KNN', '1')
INFO:root:02:32:07, round 1, class ('KNN', '3')
INFO:root:02:35:53, round 1, class ('SVM', 'poly(3)')
INFO:root:02:35:55, round 1, class ('SVM', 'rbf')
INFO:root:02:35:59, round 2, class ('KNN', '1')
INFO:root:02:39:41, round 2, class ('KNN', '3')
INFO:root:02:43:24, round 2, class ('SVM', 'poly(3)')
INFO:root:02:43:26, round 2, class ('SVM', 'rbf')
INFO:root:02:43:31, round 3, class ('KNN', '1')
INFO:root:02:47:16, round 3, class ('KNN', '3')
INFO:root:02:51:02, round 3, class ('SVM', 'poly(3)')
INFO:root:02:51:04, round 3, class ('SVM', 'rbf')
INFO:root:02:51:08, round 4, class ('KNN', '1')
INFO:root:02:54:51, round 4, class ('KNN', '3')
INFO:root:02:58:32, round 4, class ('SVM', 'poly(3)')
INFO:root:02:58:34, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.7, 'metric': 'BA', ('KNN', '1'): '0.52(+-0.0e+00)', ('KNN', '3'): '0.51(+-0.0e+00)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'TN', ('KNN', '1'): '6.8e+03(+-0.0e+00)', ('KNN', '3'): '6.8e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '6.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '6.9e+03(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'FP', ('KNN', '1'): '1.2e+02(+-0.0e+00)', ('KNN', '3'): '2e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'FN', ('KNN', '1'): '1.2e+02(+-0.0e+00)', ('KNN', '3'): '1.3e+02(+-0.0e+00)', ('SVM', 'poly(3)'): '1.3e+02(+-0.0e+00)', ('SVM', 'rbf'): '1.3e+02(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'TP', ('KNN', '1'): '7.0(+-0.0e+00)', ('KNN', '3'): '2.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
/home/jarda/Desktop/roz/project/wldtools_3.py:244: FutureWarning: In future versions `DataFrame.to_latex` is expected to utilise the base implementation of `Styler.to_latex` for formatting and rendering. The arguments signature may therefore change. It is recommended instead to use `DataFrame.style.to_latex` which also contains additional functionality.
  print(table.to_latex())
\begin{tabular}{llllll}
\toprule
    &    & \multicolumn{2}{l}{KNN} & \multicolumn{2}{l}{SVM} \\
    &    &                   1 &                   3 &             poly(3) &                 rbf \\
test\_size & metric &                     &                     &                     &                     \\
\midrule
0.3 & BA &     0.56(+-0.0e+00) &      0.5(+-3.9e-33) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) \\
    & FP &  4.4e+01(+-0.0e+00) &      2.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  4.4e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) \\
    & TP &      7.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
0.5 & BA &     0.54(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  4.8e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) \\
    & FP &    8e+01(+-0.0e+00) &  1.2e+01(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  8.1e+01(+-0.0e+00) &    9e+01(+-0.0e+00) &    9e+01(+-0.0e+00) &    9e+01(+-0.0e+00) \\
    & TP &      9.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
0.7 & BA &     0.52(+-0.0e+00) &     0.51(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  6.8e+03(+-0.0e+00) &  6.8e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) \\
    & FP &  1.2e+02(+-0.0e+00) &    2e+01(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  1.2e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) \\
    & TP &      7.0(+-0.0e+00) &      2.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
\bottomrule
\end{tabular}

