jarda@ux430unr:~/Desktop/roz/project$ python3 wldtools_paper_simple.py 
INFO:root:00:52:51
RANDOM_STATE=42
SAMPLES=10000
SIZE=128
T=8
M=6
WEIGHTS=False
S=20
EQUALIZE=False
GREYSCALE=True
INFO:root:Extracting WLD from images
  0%|                                                                                                                                              | 0/10000 [00:00<?, ?it/s]DEBUG:matplotlib:matplotlib data path: /home/jarda/.local/lib/python3.10/site-packages/matplotlib/mpl-data
DEBUG:matplotlib:CONFIGDIR=/home/jarda/r/configs/.config/matplotlib
DEBUG:matplotlib:interactive is False
DEBUG:matplotlib:platform is linux
DEBUG:matplotlib:CACHEDIR=/home/jarda/.cache/matplotlib
DEBUG:matplotlib.font_manager:Using fontManager instance from /home/jarda/.cache/matplotlib/fontlist-v330.json
  2%|██▌                                                                                                                                 | 198/10000 [00:07<06:22, 25.60it/s]/home/jarda/Desktop/roz/project/wldtools_paper_simple.py:87: RuntimeWarning: divide by zero encountered in divide
  return np.arctan(np.divide(v00, v01))
  6%|████████▏                                                                                                                           | 620/10000 [00:21<04:20, 35.98it/s]/home/jarda/Desktop/roz/project/wldtools_paper_simple.py:87: RuntimeWarning: invalid value encountered in divide
  return np.arctan(np.divide(v00, v01))
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [04:44<00:00, 35.16it/s]
INFO:root:---------- TEST SIZE 0.3, TRAIN SIZE 0.7 ---------
INFO:root:00:57:36, round 0, class ('KNN', '1')
INFO:root:01:01:30, round 0, class ('KNN', '3')
INFO:root:01:05:30, round 0, class ('SVM', 'poly(3)')
INFO:root:01:05:41, round 0, class ('SVM', 'rbf')
INFO:root:01:05:54, round 1, class ('KNN', '1')
INFO:root:01:09:48, round 1, class ('KNN', '3')
INFO:root:01:13:46, round 1, class ('SVM', 'poly(3)')
INFO:root:01:13:57, round 1, class ('SVM', 'rbf')
INFO:root:01:14:09, round 2, class ('KNN', '1')
INFO:root:01:18:03, round 2, class ('KNN', '3')
INFO:root:01:21:57, round 2, class ('SVM', 'poly(3)')
INFO:root:01:22:07, round 2, class ('SVM', 'rbf')
INFO:root:01:22:19, round 3, class ('KNN', '1')
INFO:root:01:26:08, round 3, class ('KNN', '3')
INFO:root:01:30:00, round 3, class ('SVM', 'poly(3)')
INFO:root:01:30:10, round 3, class ('SVM', 'rbf')
INFO:root:01:30:22, round 4, class ('KNN', '1')
INFO:root:01:34:13, round 4, class ('KNN', '3')
INFO:root:01:38:03, round 4, class ('SVM', 'poly(3)')
INFO:root:01:38:14, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.3, 'metric': 'BA', ('KNN', '1'): '0.54(+-0.0e+00)', ('KNN', '3'): '0.5(+-0.0e+00)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'TN', ('KNN', '1'): '2.9e+03(+-0.0e+00)', ('KNN', '3'): '2.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '2.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '2.9e+03(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'FP', ('KNN', '1'): '2.7e+01(+-0.0e+00)', ('KNN', '3'): '7.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'FN', ('KNN', '1'): '4.6e+01(+-0.0e+00)', ('KNN', '3'): '5.1e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '5.1e+01(+-0.0e+00)', ('SVM', 'rbf'): '5.1e+01(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'TP', ('KNN', '1'): '5.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
INFO:root:---------- TEST SIZE 0.5, TRAIN SIZE 0.5 ---------
INFO:root:01:38:26, round 0, class ('KNN', '1')
INFO:root:01:43:05, round 0, class ('KNN', '3')
INFO:root:01:47:42, round 0, class ('SVM', 'poly(3)')
INFO:root:01:47:48, round 0, class ('SVM', 'rbf')
INFO:root:01:47:57, round 1, class ('KNN', '1')
INFO:root:01:52:36, round 1, class ('KNN', '3')
INFO:root:01:57:13, round 1, class ('SVM', 'poly(3)')
INFO:root:01:57:18, round 1, class ('SVM', 'rbf')
INFO:root:01:57:27, round 2, class ('KNN', '1')
INFO:root:02:02:06, round 2, class ('KNN', '3')
INFO:root:02:06:43, round 2, class ('SVM', 'poly(3)')
INFO:root:02:06:48, round 2, class ('SVM', 'rbf')
INFO:root:02:06:57, round 3, class ('KNN', '1')
INFO:root:02:11:35, round 3, class ('KNN', '3')
INFO:root:02:16:10, round 3, class ('SVM', 'poly(3)')
INFO:root:02:16:16, round 3, class ('SVM', 'rbf')
INFO:root:02:16:25, round 4, class ('KNN', '1')
INFO:root:02:21:04, round 4, class ('KNN', '3')
INFO:root:02:25:39, round 4, class ('SVM', 'poly(3)')
INFO:root:02:25:44, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.5, 'metric': 'BA', ('KNN', '1'): '0.53(+-0.0e+00)', ('KNN', '3'): '0.5(+-3.9e-33)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'TN', ('KNN', '1'): '4.9e+03(+-0.0e+00)', ('KNN', '3'): '4.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '4.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '4.9e+03(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'FP', ('KNN', '1'): '5.6e+01(+-0.0e+00)', ('KNN', '3'): '1.4e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'FN', ('KNN', '1'): '8.3e+01(+-0.0e+00)', ('KNN', '3'): '9e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '9e+01(+-0.0e+00)', ('SVM', 'rbf'): '9e+01(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'TP', ('KNN', '1'): '7.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
INFO:root:---------- TEST SIZE 0.7, TRAIN SIZE 0.30000000000000004 ---------
INFO:root:02:25:53, round 0, class ('KNN', '1')
INFO:root:02:29:44, round 0, class ('KNN', '3')
INFO:root:02:33:33, round 0, class ('SVM', 'poly(3)')
INFO:root:02:33:36, round 0, class ('SVM', 'rbf')
INFO:root:02:33:41, round 1, class ('KNN', '1')
INFO:root:02:37:31, round 1, class ('KNN', '3')
INFO:root:02:41:24, round 1, class ('SVM', 'poly(3)')
INFO:root:02:41:26, round 1, class ('SVM', 'rbf')
INFO:root:02:41:30, round 2, class ('KNN', '1')
INFO:root:02:45:21, round 2, class ('KNN', '3')
INFO:root:02:49:11, round 2, class ('SVM', 'poly(3)')
INFO:root:02:49:13, round 2, class ('SVM', 'rbf')
INFO:root:02:49:18, round 3, class ('KNN', '1')
INFO:root:02:53:09, round 3, class ('KNN', '3')
INFO:root:02:56:59, round 3, class ('SVM', 'poly(3)')
INFO:root:02:57:02, round 3, class ('SVM', 'rbf')
INFO:root:02:57:06, round 4, class ('KNN', '1')
INFO:root:03:00:13, round 4, class ('KNN', '3')
INFO:root:03:02:30, round 4, class ('SVM', 'poly(3)')
INFO:root:03:02:31, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.7, 'metric': 'BA', ('KNN', '1'): '0.53(+-0.0e+00)', ('KNN', '3'): '0.5(+-0.0e+00)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'TN', ('KNN', '1'): '6.8e+03(+-0.0e+00)', ('KNN', '3'): '6.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '6.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '6.9e+03(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'FP', ('KNN', '1'): '8.5e+01(+-0.0e+00)', ('KNN', '3'): '1.5e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '9.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'FN', ('KNN', '1'): '1.2e+02(+-0.0e+00)', ('KNN', '3'): '1.3e+02(+-0.0e+00)', ('SVM', 'poly(3)'): '1.3e+02(+-0.0e+00)', ('SVM', 'rbf'): '1.3e+02(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'TP', ('KNN', '1'): '1e+01(+-0.0e+00)', ('KNN', '3'): '1.0(+-0.0e+00)', ('SVM', 'poly(3)'): '1.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
/home/jarda/Desktop/roz/project/wldtools_paper_simple.py:244: FutureWarning: In future versions `DataFrame.to_latex` is expected to utilise the base implementation of `Styler.to_latex` for formatting and rendering. The arguments signature may therefore change. It is recommended instead to use `DataFrame.style.to_latex` which also contains additional functionality.
  print(table.to_latex())
\begin{tabular}{llllll}
\toprule
    &    & \multicolumn{2}{l}{KNN} & \multicolumn{2}{l}{SVM} \\
    &    &                   1 &                   3 &             poly(3) &                 rbf \\
test\_size & metric &                     &                     &                     &                     \\
\midrule
0.3 & BA &     0.54(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) \\
    & FP &  2.7e+01(+-0.0e+00) &      7.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  4.6e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) \\
    & TP &      5.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
0.5 & BA &     0.53(+-0.0e+00) &      0.5(+-3.9e-33) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) \\
    & FP &  5.6e+01(+-0.0e+00) &  1.4e+01(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  8.3e+01(+-0.0e+00) &    9e+01(+-0.0e+00) &    9e+01(+-0.0e+00) &    9e+01(+-0.0e+00) \\
    & TP &      7.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
0.7 & BA &     0.53(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  6.8e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) \\
    & FP &  8.5e+01(+-0.0e+00) &  1.5e+01(+-0.0e+00) &      9.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  1.2e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) \\
    & TP &    1e+01(+-0.0e+00) &      1.0(+-0.0e+00) &      1.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
\bottomrule
\end{tabular}

