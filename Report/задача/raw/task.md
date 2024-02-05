# Тестовые задания

Задание LLM Prompts and Inferences Analysis (Analyst)
На основании тестовых данных (см. раздел Тестовые данные) решить поставленную задачу с использованием традиционного DS/ML stack, а также с использованием Large Language Model (LLM) и внешних инструментов (Python code, APIs), проанализировать выводы (результаты) и сделать заключения и рекомендации.
Постановка задачи
Решить задачу анализа данных, описанную запросом (prompt) пользователя, двумя способами, сравнить результаты и сделать выводы:

1. Решение DS/ML: с использованием традиционного DS/ML stack, своей квалификации и опыта:
   1. провести разведочный анализ данных
   2. провести корреляционный анализ (если требуется)
   3. обучить модель, способную прогнозировать вероятность возникновения события или трендов (если требуется)
   4. ответить на поставленный в prompt вопрос
2. Решение LLM: с использованием LLM и внешних инструментов (Python code, созданный LLM и вызывающий внешние APIs):
   1. опционально: провести декомпозицию задачи (LLM)
   2. решить исходную или выделенные отдельные задачи последовательно, итеративно или параллельно (LLM)
   3. сгенерировать код на Python, использующий DS/ML frameworks/libs для анализа и визуализации данных и результатов (LLM)
   4. выполнить сгенерированный код (automatic или manual operation)
   5. объединить полученные результаты (automatic или manual operation)
   6. предоставить шаги решения и результаты/ выводы (inferences) системы в форме текстовой и графической информации (automatic или manual operation)
   7. допустимо предварительно обработать исходные данные для решения LLM
   8. допустимо незначительно модифицировать и конкретизировать исходные user prompts для решения LLM, чтобы направить LLM на получение требуемого решения
3. Сравнить полученные решения, сделать выводы и рекомендации.

Примеры prompts - см. раздел Тестовые данные. Для выполнения задания может использоваться любой prompt.

Хорошее стабильное решение LLM должно позволять решать некоторые другие или даже все задачи данного класса и потенциально может быть проверено с использованием другого prompt и повторения предложенных для решения LLM шагов.
Результаты
Общие требования

* Документ с отчетом предоставляется в любом репозитории
* Source code предоставляется в любом репозитории
* Deployment/Delivery, если требуется, осуществляется в любой форме, допускающей online проверки (manual QA)
* На выполнение задания отводится одна неделя
Решение LLM - Требования к оформлению результатов
Решение LLM предоставляется в виде документа в любом формате, содержащем:
* Исходная задача (prompt)
* Результирующий вывод (Inference)
* Последовательность шагов, приведших к решению: полный prompt (включая внутренние инструкции) и Inference для каждого LLM шага; выполненный код (если имеется) и результаты; комментарии и пояснения, если требуется
* Заключение и рекомендации
Решение LLM - Требования к source code
* Основная часть кода должна генерироваться LLM
* Используемый в процессе решения задачи дополнительный код (если таковой потребуется) должен быть написан на Python
* Дополнительно написанный код должен носить вспомогательный общий характер для данного класса задач и не должен решать поставленные задачи непосредственно

________________
Тестовые данные
Для выполнения задания можно использовать предоставленные статические данные, аналогичные публично доступные данные или собственные синтетические (искусственно сгенерированные) данные.
Статические данные
Файлы данных interview.X.csv и interview.y.csv доступны к загрузке по этой ссылке.
Описание данных
У файлов interview.X.csv и interview.y.csv есть общее поле, по которому между ними может быть установлена связь - идентификатор показа (uid).

Следует учитывать, что это реальные данные, которые могут содержать ошибки, дублирующуюся или некорректную информацию, и которые могут потребовать предварительной обработки для выполнения задания.

Допустимо для решения LLM провести предварительную обработку и объединение исходных данных.
interview.X.csv
Лог показов (просмотров, impressions):

* reg_time - timestamp;
* uid - идентификатор показа;
* fc_imp_chk - число предшествующих показов:

Значение
 Описание
 -1
 N/A
 0
 1 impression
 1
 2-5 impressions
 2
 6-10 impressions
 3
 11-20 impressions
 4
 21+ impressions
 
* fc_time_chk - время с момента последнего показа:

Значение
 Описание
 -1
 N/A
 0
 Less than a minute
 1
 1-10 minutes
 2
 11-30 minutes
 3
 31-60 minutes
 4
 1-3 hours
 5
 4-24 hours
 6
 One or more days
 7
 Never before
 
* utmtr - время просмотра в часовом поясе пользователя:

Значение
 Описание
 -1
 N/A
 0
 00:00 - 03:00
 1
 03:00 - 06:00
 2
 06:00 - 09:00
 3
 09:00 - 12:00
 4
 12:00 - 15:00
 5
 15:00 - 18:00
 6
 18:00 - 21:00
 7
 21:00 - 00:00
 
      * mm_dma - DMA (Designated Market Area);
      * osName - OS;
      * model - модель устройства;
      * hardware - тип устройства;
      * site_id - сайт, где был просмотр
interview.y.csv
Лог событий (events):
      *uid - идентификатор показа, в результате которого произошло событие;
      * tag - тип события:
      *буква <v> в начале некоторых событий означает, что событие произошло без клика = view-through. В противном случае имеем click-through событие;
      * событие fclick - первый клик (используется для расчета CTR).
Метрики CTR и EvPM
      *Click Through Rate (CTR)
CTR (click rate) = 100* click_count / impression_count %.
В нашем случае click_count - кол-во событий fclick.
См. также CTR (ссылка на википедию)

      * Event Permille (EvPM)
EvPM (event rate) = 1000 * event_count / impression_count ‰
для запрошенного типа события. Признак view/click-through учитывать не требуется (т.е. при вычислении EvPM для (v)registration в числителе имеем сумму числа registration и vregistration).
User Prompts
Провести анализ данных, позволяющий ответить на запрос, содержащийся в user prompt.

Ниже перечислены user prompts, относящиеся к одному классу задач, в детальной формулировке:
      *Identify Important Factors: Find out what factors are most likely to make someone click on online ads. Tell me which factors are the strongest predictors and rank them.
      * Predict Click Probability: Can you create a model that tells us how likely it is for someone to click on an online ad? Use the data we have and provide an estimate of the probability.
      *Assess the effectiveness of advertising on different devices based on clicks. Present the results in the form of an ordered list in descending order of performance along with the corresponding Click-Through Rates (CTR).
      * Create targeting based on the top 10 DMAs (Designated Market Areas) by CTR.
      * Propose targeting based on the top 5 best hours of the day by CTR. Present the results in the form of an ordered list in descending order of performance along with the corresponding CTR.

Дополнительные примеры user prompts в более лаконичной, дружелюбной для человека форме, характерной для реальных сценариев использования:
      * Find the top factors that drive ad clicks
      * Which types of devices get the most ad clicks, ranked from highest to lowest
      *Build a model to predict ad click probabilities
      * Rank features by their influence on ad clicks
      *Identify the top 10 geographic areas where our ads perform best in terms of click rates
      * Assess how well the click prediction model works
      *What are the best times of day for ad clicks? List the top 5 hours by their click success rate
      * Improve the model's accuracy in predicting ad clicks
      *Which day of the week sees the highest click rates on our ads?
      * Discover patterns in user events like signups and registrations
      * Display the top 15 websites where our ads receive the most clicks

Допустимо для решения LLM незначительно модифицировать и конкретизировать исходные user prompts для этого варианта, чтобы направить LLM на требуемое решение.
________________

Приложение. Решение LLM - Пояснения и рекомендации
Рекомендуемые действия
Результаты решения LLM рекомендуется получить путем использования следующих действий:
      *применение готового к использованию LLM/ Foundation Model промышленного уровня, обученного на требуемых API; предпочтительно: GPT-4, Bard
      * конструирования уточненных prompts, contexts, training samples:
      *текст должен быть структурированным/ размеченным и допускать автоматические подстановки и parsing в дальнейшем (см. примеры в разделе Примеры внутренних LLM Prompts)
      * должна быть предусмотрена возможность автоматической вставки в текст исходного prompt пользователя или его частей
      *текст не должен содержать явных рекомендаций по решению конкретного prompt, но может содержать рекомендации общего плана для родственного класса задач (не отражено в примерах)
      * текст может содержать обучающие примеры из родственного класса задач (не отражено в примерах)
      *распределения задачи между несколькими сущностями (называемыми далее Agents):
      * Agent может представлять из себя LLM Chat, Intelligent Agent другого типа, либо Agent, использующий алгоритмическую часть
      *Agents могут взаимодействовать в различных произвольных последовательностях
      * генерации Python кода с помощью Agents
      *использования предварительно разработанного Python кода, общего для данного класса задач
      * предпочтительно: полной программной (автоматической) реализации решения LLM
      *приемлемо: ручного моделирования решения LLM и взаимодействия между Agents:
      * не требуется программно реализовывать все взаимодействия между агентами
      *не требуется программно реализовывать интеграцию с LLM API, отдельные результаты могут быть получены в интерактивной сессии пользовательского уровня
      * данные могут передаваться вручную: copy & paste текстовой информации, передача links/paths на online хранилища с объемными данными, ручное объединение кода, сгенерированного разными Agents, по простым правилам. ручное объединение результатов
      *использования любых фреймворков и библиотек для анализа и визуализации данных (из массива знаний LLM); приветствуется выбор используемого инструментария с помощью LLM
      * выполнения сгенерированного Python Code в любой среде программирования/ моделирования (automatic или manual operation)
      *объединения полученных результатов (automatic или manual operation)
      * анализа и уточнения результатов (automatic или manual operation)
      *дополнительными плюсами решения будут:
      * попытка дополнительно решить задачу с помощью одного mono-agent и сложного prompt и context
      *использование RAG для более гибкого формирования контекста
      * решение дополнительно той же задачи с использованием других аналогичных AI/LLM инструментов (AutoGPT, MetaGPT, LangChain, AgentVerse, ChatDev)
      *реализация операций, помеченных “(automatic или manual operation)”, программно - частично или полностью
      * сравнение полученных дополнительных различных решений с основными (DS/ML и LLM), предоставление выводов и рекомендаций
Задание для ML/DS специалиста
Ниже приведено обобщенное описание задач, которые мог бы решить ML/DS специалист, чтобы иметь инструмент для ответа на уточняющие вопросы по предоставленным данным и user prompts, относящихся к данному классу задач.

Используя предоставленные данные решить следующие задачи:
      *Определить, какие признаки показа являются хорошими предикторами события (например, события fclick), упорядочить их в порядке убывания вместе с численной оценкой их качества
      * Написать код выбора, подбора параметров, обучения и валидации модели классификации на Python, которая прогнозирует вероятность клика на основании информации о показах
Примеры внутренних LLM Prompts
Ниже приведены примеры преамбул внутренних prompts к LLM, предваряющих предметный prompt и позволяющих получить более корректный и детерминированный вывод (inference) системы.

      * Описание роли архитектора в процессе разработки программного обеспечения:
You are an Architect.
Design a concise, usable, complete python system.
Try to specify good open source tools as much as possible.

      * Описание роли программиста-разработчика, ответственного за написание и, возможно, проверку кода:
You are a Software Engineer.
Write elegant, readable, extensible, efficient code.
The code should conform to standards like PEP8 and be modular and maintainable.

      * Более сложное описания агента-помощника, предназначенного для решения задач с помощью LLM:
As an AI assistant:
Use coding and language skills for task resolution.
Provide Python or shell scripts for data gathering. Solve the task using gathered info.
Offer complete scripts for executable tasks, clearly indicating script type.
Explain task plans, differentiating between code execution and language processing steps.
Ensure code is ready-to-run without user modifications. Include # filename: <filename> for file-saving instructions.
Use one code block per response with 'print' for outputs. Avoid requiring user edits or result copy-pasting.
Correct errors in scripts and reassess if tasks remain unsolved after successful execution.
Confirm accuracy of solutions and provide evidence when possible.
End interactions with "TERMINATE" after task completion.

      * Описание агента-руководителя, занимающегося декомпозицией задач и их делегированием:
You are а Head of the department.
Available agents: [database structure analyzer, statistics generation, data visualization].
Decompose the task and choose the most suitable agents from the available agents. Print ONLY a list where each element is: <number>###<Task description>###<the most suitable agent from the available agents>
