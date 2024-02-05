# 🕵🏿‍♂️ Autogen's Solution

## Story ✅ ✅

С использованием LLM и внешних инструментов (Python code, созданный LLM и вызывающий внешние APIs):

   1. опционально: провести декомпозицию задачи (LLM)
   2. решить исходную или выделенные отдельные задачи последовательно, итеративно или параллельно (LLM)
   3. сгенерировать код на Python, использующий DS/ML frameworks/libs для анализа и визуализации данных и результатов (LLM)
   4. выполнить сгенерированный код (automatic или manual operation)
   5. объединить полученные результаты (automatic или manual operation)
   6. предоставить шаги решения и результаты/ выводы (inferences) системы в форме текстовой и графической информации (automatic или manual operation)
   7. допустимо предварительно обработать исходные данные для решения LLM
   8. допустимо незначительно модифицировать и конкретизировать исходные user prompts для решения LLM, чтобы направить LLM на получение требуемого решения

## 📚 Решение LLM

### Шаги решения LLM

* Загрузить файлы и проанализировать и предподготовить данные для решения задач
* Определить, какие признаки показа являются хорошими предикторами события (например, события fclick), упорядочить их в порядке убывания вместе с численной оценкой их качества
* Написать код выбора, подбора параметров, обучения и валидации модели классификации на Python, которая прогнозирует вероятность клика на основании информации о показах

#### Используя предоставленные данные решить следующие задачи

* Определить, какие признаки показа являются хорошими предикторами события (например, события fclick), упорядочить их в порядке убывания вместе с численной оценкой их качества
* Написать код выбора, подбора параметров, обучения и валидации модели классификации на Python, которая прогнозирует вероятность клика на основании информации о показах

### ⚙️ Agents Team 🤖🤖🤖🤖

* Описание [агента-руководителя](agents/Manager.md), занимающегося декомпозицией задач и их делегированием:
* Более сложное описания [агента-помощника](agents/Assistant.md), предназначенного для решения задач с помощью LLM:
* Описание роли [программиста-разработчика](agents/Developer.md), ответственного за написание и, возможно, проверку кода:
* Описание роли [архитектора в процессе разработки программного обеспечения](agents/Architect.md):

#### Agents tools

[tools_root](tools/inventory.md)

#### Ниже перечислены user prompts, относящиеся к одному классу задач, в детальной формулировке

* Identify Important Factors: Find out what factors are most likely to make someone click on online ads. Tell me which factors are the strongest predictors and rank them.
* Predict Click Probability: Can you create a model that tells us how likely it is for someone to click on an online ad? Use the data we have and provide an estimate of the probability.
* Assess the effectiveness of advertising on different devices based on clicks. Present the results in the form of an ordered list in descending order of performance along with the corresponding Click-Through Rates (CTR).
* Create targeting based on the top 10 DMAs (Designated Market Areas) by CTR.
* Propose targeting based on the top 5 best hours of the day by CTR. Present the results in the form of an ordered list in descending order of performance along with the corresponding CTR.

#### Дополнительные примеры user prompts в более лаконичной, дружелюбной для человека форме, характерной для реальных сценариев использования

* Find the top factors that drive ad clicks
* Which types of devices get the most ad clicks, ranked from highest to lowest
* Build a model to predict ad click probabilities
* Rank features by their influence on ad clicks
* Identify the top 10 geographic areas where our ads perform best in terms of click rates
* Assess how well the click prediction model works
* What are the best times of day for ad clicks? List the top 5 hours by their click success rate
* Improve the model's accuracy in predicting ad clicks
* Which day of the week sees the highest click rates on our ads?
* Discover patterns in user events like signups and registrations
* Display the top 15 websites where our ads receive the most clicks
