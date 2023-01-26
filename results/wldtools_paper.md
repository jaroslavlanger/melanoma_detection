(venv) jarda@ux430unr:~/Desktop/roz/project$ python3 wldtools_paper.py 
INFO:root:00:45:22
RANDOM_STATE=42
SAMPLES=10000
SIZE=128
T=8
M=6
WEIGHTS=(0.2688, 0.0852, 0.0955, 0.1, 0.1018, 0.3487)
S=20
EQUALIZE=True
GREYSCALE=True
INFO:root:Extracting WLD from images
  0%|                                                                                                                                              | 0/10000 [00:00<?, ?it/s]DEBUG:matplotlib:matplotlib data path: /home/jarda/.local/lib/python3.10/site-packages/matplotlib/mpl-data
DEBUG:matplotlib:CONFIGDIR=/home/jarda/r/configs/.config/matplotlib
DEBUG:matplotlib:interactive is False
DEBUG:matplotlib:platform is linux
DEBUG:matplotlib:CACHEDIR=/home/jarda/.cache/matplotlib
DEBUG:matplotlib.font_manager:Using fontManager instance from /home/jarda/.cache/matplotlib/fontlist-v330.json
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [02:39<00:00, 62.60it/s]
INFO:root:---------- TEST SIZE 0.3, TRAIN SIZE 0.7 ---------
INFO:root:00:48:02, round 0, class ('KNN', '1')
INFO:root:00:50:56, round 0, class ('KNN', '3')
INFO:root:00:54:54, round 0, class ('SVM', 'poly(3)')
INFO:root:00:55:07, round 0, class ('SVM', 'rbf')
INFO:root:00:55:24, round 1, class ('KNN', '1')
INFO:root:00:59:27, round 1, class ('KNN', '3')
INFO:root:01:03:32, round 1, class ('SVM', 'poly(3)')
INFO:root:01:03:44, round 1, class ('SVM', 'rbf')
INFO:root:01:04:00, round 2, class ('KNN', '1')
INFO:root:01:08:02, round 2, class ('KNN', '3')
INFO:root:01:12:01, round 2, class ('SVM', 'poly(3)')
INFO:root:01:12:13, round 2, class ('SVM', 'rbf')
INFO:root:01:12:29, round 3, class ('KNN', '1')
INFO:root:01:16:31, round 3, class ('KNN', '3')
INFO:root:01:20:35, round 3, class ('SVM', 'poly(3)')
INFO:root:01:20:47, round 3, class ('SVM', 'rbf')
INFO:root:01:21:03, round 4, class ('KNN', '1')
INFO:root:01:25:10, round 4, class ('KNN', '3')
INFO:root:01:29:13, round 4, class ('SVM', 'poly(3)')
INFO:root:01:29:26, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.3, 'metric': 'BA', ('KNN', '1'): '0.51(+-0.0e+00)', ('KNN', '3'): '0.5(+-0.0e+00)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'TN', ('KNN', '1'): '2.9e+03(+-0.0e+00)', ('KNN', '3'): '2.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '2.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '2.9e+03(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'FP', ('KNN', '1'): '4.5e+01(+-0.0e+00)', ('KNN', '3'): '4.0(+-0.0e+00)', ('SVM', 'poly(3)'): '1.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'FN', ('KNN', '1'): '4.9e+01(+-0.0e+00)', ('KNN', '3'): '5.1e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '5.1e+01(+-0.0e+00)', ('SVM', 'rbf'): '5.1e+01(+-0.0e+00)'}, {'test_size': 0.3, 'metric': 'TP', ('KNN', '1'): '2.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
INFO:root:---------- TEST SIZE 0.5, TRAIN SIZE 0.5 ---------
INFO:root:01:29:42, round 0, class ('KNN', '1')
INFO:root:01:34:29, round 0, class ('KNN', '3')
INFO:root:01:39:18, round 0, class ('SVM', 'poly(3)')
INFO:root:01:39:26, round 0, class ('SVM', 'rbf')
INFO:root:01:39:40, round 1, class ('KNN', '1')
INFO:root:01:44:26, round 1, class ('KNN', '3')
INFO:root:01:49:09, round 1, class ('SVM', 'poly(3)')
INFO:root:01:49:17, round 1, class ('SVM', 'rbf')
INFO:root:01:49:29, round 2, class ('KNN', '1')
INFO:root:01:54:13, round 2, class ('KNN', '3')
INFO:root:01:58:56, round 2, class ('SVM', 'poly(3)')
INFO:root:01:59:04, round 2, class ('SVM', 'rbf')
INFO:root:01:59:17, round 3, class ('KNN', '1')
INFO:root:02:04:02, round 3, class ('KNN', '3')
INFO:root:02:08:46, round 3, class ('SVM', 'poly(3)')
INFO:root:02:08:54, round 3, class ('SVM', 'rbf')
INFO:root:02:09:07, round 4, class ('KNN', '1')
INFO:root:02:13:53, round 4, class ('KNN', '3')
INFO:root:02:18:37, round 4, class ('SVM', 'poly(3)')
INFO:root:02:18:46, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.5, 'metric': 'BA', ('KNN', '1'): '0.51(+-0.0e+00)', ('KNN', '3'): '0.5(+-3.9e-33)', ('SVM', 'poly(3)'): '0.5(+-3.9e-33)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'TN', ('KNN', '1'): '4.8e+03(+-0.0e+00)', ('KNN', '3'): '4.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '4.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '4.9e+03(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'FP', ('KNN', '1'): '8.6e+01(+-0.0e+00)', ('KNN', '3'): '7.0(+-0.0e+00)', ('SVM', 'poly(3)'): '7.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'FN', ('KNN', '1'): '8.6e+01(+-0.0e+00)', ('KNN', '3'): '9e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '9e+01(+-0.0e+00)', ('SVM', 'rbf'): '9e+01(+-0.0e+00)'}, {'test_size': 0.5, 'metric': 'TP', ('KNN', '1'): '4.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
INFO:root:---------- TEST SIZE 0.7, TRAIN SIZE 0.30000000000000004 ---------
INFO:root:02:18:58, round 0, class ('KNN', '1')
INFO:root:02:22:57, round 0, class ('KNN', '3')
INFO:root:02:26:57, round 0, class ('SVM', 'poly(3)')
INFO:root:02:27:01, round 0, class ('SVM', 'rbf')
INFO:root:02:27:09, round 1, class ('KNN', '1')
INFO:root:02:31:11, round 1, class ('KNN', '3')
INFO:root:02:35:10, round 1, class ('SVM', 'poly(3)')
INFO:root:02:35:14, round 1, class ('SVM', 'rbf')
INFO:root:02:35:21, round 2, class ('KNN', '1')
INFO:root:02:39:18, round 2, class ('KNN', '3')
INFO:root:02:43:16, round 2, class ('SVM', 'poly(3)')
INFO:root:02:43:20, round 2, class ('SVM', 'rbf')
INFO:root:02:43:28, round 3, class ('KNN', '1')
INFO:root:02:47:26, round 3, class ('KNN', '3')
INFO:root:02:51:24, round 3, class ('SVM', 'poly(3)')
INFO:root:02:51:28, round 3, class ('SVM', 'rbf')
INFO:root:02:51:36, round 4, class ('KNN', '1')
INFO:root:02:55:34, round 4, class ('KNN', '3')
INFO:root:02:59:20, round 4, class ('SVM', 'poly(3)')
INFO:root:02:59:24, round 4, class ('SVM', 'rbf')
INFO:root:[{'test_size': 0.7, 'metric': 'BA', ('KNN', '1'): '0.51(+-0.0e+00)', ('KNN', '3'): '0.5(+-3.9e-33)', ('SVM', 'poly(3)'): '0.5(+-0.0e+00)', ('SVM', 'rbf'): '0.5(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'TN', ('KNN', '1'): '6.8e+03(+-0.0e+00)', ('KNN', '3'): '6.9e+03(+-0.0e+00)', ('SVM', 'poly(3)'): '6.9e+03(+-0.0e+00)', ('SVM', 'rbf'): '6.9e+03(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'FP', ('KNN', '1'): '1.1e+02(+-0.0e+00)', ('KNN', '3'): '1.6e+01(+-0.0e+00)', ('SVM', 'poly(3)'): '1.7e+01(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'FN', ('KNN', '1'): '1.3e+02(+-0.0e+00)', ('KNN', '3'): '1.3e+02(+-0.0e+00)', ('SVM', 'poly(3)'): '1.3e+02(+-0.0e+00)', ('SVM', 'rbf'): '1.3e+02(+-0.0e+00)'}, {'test_size': 0.7, 'metric': 'TP', ('KNN', '1'): '4.0(+-0.0e+00)', ('KNN', '3'): '0.0(+-0.0e+00)', ('SVM', 'poly(3)'): '0.0(+-0.0e+00)', ('SVM', 'rbf'): '0.0(+-0.0e+00)'}]
/home/jarda/Desktop/roz/project/wldtools_paper.py:244: FutureWarning: In future versions `DataFrame.to_latex` is expected to utilise the base implementation of `Styler.to_latex` for formatting and rendering. The arguments signature may therefore change. It is recommended instead to use `DataFrame.style.to_latex` which also contains additional functionality.
  print(table.to_latex())
\begin{tabular}{llllll}
\toprule
    &    & \multicolumn{2}{l}{KNN} & \multicolumn{2}{l}{SVM} \\
    &    &                   1 &                   3 &             poly(3) &                 rbf \\
test\_size & metric &                     &                     &                     &                     \\
\midrule
0.3 & BA &     0.51(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) &  2.9e+03(+-0.0e+00) \\
    & FP &  4.5e+01(+-0.0e+00) &      4.0(+-0.0e+00) &      1.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  4.9e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) &  5.1e+01(+-0.0e+00) \\
    & TP &      2.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
0.5 & BA &     0.51(+-0.0e+00) &      0.5(+-3.9e-33) &      0.5(+-3.9e-33) &      0.5(+-0.0e+00) \\
    & TN &  4.8e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) &  4.9e+03(+-0.0e+00) \\
    & FP &  8.6e+01(+-0.0e+00) &      7.0(+-0.0e+00) &      7.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  8.6e+01(+-0.0e+00) &    9e+01(+-0.0e+00) &    9e+01(+-0.0e+00) &    9e+01(+-0.0e+00) \\
    & TP &      4.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
0.7 & BA &     0.51(+-0.0e+00) &      0.5(+-3.9e-33) &      0.5(+-0.0e+00) &      0.5(+-0.0e+00) \\
    & TN &  6.8e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) &  6.9e+03(+-0.0e+00) \\
    & FP &  1.1e+02(+-0.0e+00) &  1.6e+01(+-0.0e+00) &  1.7e+01(+-0.0e+00) &      0.0(+-0.0e+00) \\
    & FN &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) &  1.3e+02(+-0.0e+00) \\
    & TP &      4.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) &      0.0(+-0.0e+00) \\
\bottomrule
\end{tabular}

