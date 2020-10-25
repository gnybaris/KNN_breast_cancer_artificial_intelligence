
data = load('C:\Users\PC\Desktop\Gögüs_Kanseri_Testi\Lojistik_Regresyon\cancer_data.csv');
y = data(:, 2);
X = data(:, [3 ,4]);

plotData(X,y);

[m, n] = size(X);
X = [ones(m, 1) X];
initial_theta = zeros(n + 1, 1);

[cost, grad] = costFunction(initial_theta, X, y);

options = optimset('GradObj', 'on', 'MaxIter', 400);

[theta, cost] = ...
fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);
fprintf('fminunc theta cost değeri: %f\n', cost);
fprintf('theta değeri: \n');
fprintf(' %f \n', theta);

plotDecisionBoundary(theta, X, y);
hold on;
xlabel('Mean Radius')
ylabel('Mean Texture')
legend('Kötü Huylu (4)', 'İyi Huylu (2)')
hold off;

