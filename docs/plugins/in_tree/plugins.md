# In-tree plugins.

Processed releases: rally 0.11.0 - 0.12.1

## Task Component

### Chart

Base class for charts.

This is a base for all plugins that prepare data for specific charts
in HTML report. Each chart must at least declare chart widget and
prepare data that is suitable for rendering by JavaScript.

#### Lines [Chart]

Display results as generic chart with lines.

This plugin processes additive data and displays it in HTML report
as linear chart with X axis bound to iteration number.
Complete output data is displayed as linear chart as well, without
any processing.

Examples of using this plugin in Scenario, for saving output data:

```python
self.add_output(
    additive={"title": "Additive data as stacked area",
              "description": "Iterations trend for foo and bar",
              "chart_plugin": "Lines",
              "data": [["foo", 12], ["bar", 34]]},
    complete={"title": "Complete data as stacked area",
              "description": "Data is shown as stacked area, as-is",
              "chart_plugin": "Lines",
              "data": [["foo", [[0, 5], [1, 42], [2, 15], [3, 7]]],
                       ["bar", [[0, 2], [1, 1.3], [2, 5], [3, 9]]]],
              "label": "Y-axis label text",
              "axis_label": "X-axis label text"})
```

__Platform__: default

__Module__: [rally.task.processing.charts](https://github.com/openstack/rally/blob/master/rally/task/processing/charts.py)

<hr />

#### OSProfiler [Chart]

osprofiler content.

This plugin complete data of osprofiler

__Platform__: default

__Module__: [rally.plugins.openstack.embedcharts.osprofilerchart](https://github.com/openstack/rally/blob/master/rally/plugins/openstack/embedcharts/osprofilerchart.py)

<hr />

#### Pie [Chart]

Display results as pie, calculate average values for additive data.

This plugin processes additive data and calculate average values.
Both additive and complete data are displayed in HTML report as pie chart.

Examples of using this plugin in Scenario, for saving output data:

```python
self.add_output(
    additive={"title": "Additive output",
              "description": ("Pie with average data "
                              "from all iterations values"),
              "chart_plugin": "Pie",
              "data": [["foo", 12], ["bar", 34], ["spam", 56]]},
    complete={"title": "Complete output",
              "description": "Displayed as a pie, as-is",
              "chart_plugin": "Pie",
              "data": [["foo", 12], ["bar", 34], ["spam", 56]]})
```

__Platform__: default

__Module__: [rally.task.processing.charts](https://github.com/openstack/rally/blob/master/rally/task/processing/charts.py)

<hr />

#### StackedArea [Chart]

Display results as stacked area.

This plugin processes additive data and displays it in HTML report
as stacked area with X axis bound to iteration number.
Complete output data is displayed as stacked area as well, without
any processing.

Keys "description", "label" and "axis_label" are optional.

Examples of using this plugin in Scenario, for saving output data:

```python
self.add_output(
    additive={"title": "Additive data as stacked area",
              "description": "Iterations trend for foo and bar",
              "chart_plugin": "StackedArea",
              "data": [["foo", 12], ["bar", 34]]},
    complete={"title": "Complete data as stacked area",
              "description": "Data is shown as stacked area, as-is",
              "chart_plugin": "StackedArea",
              "data": [["foo", [[0, 5], [1, 42], [2, 15], [3, 7]]],
                       ["bar", [[0, 2], [1, 1.3], [2, 5], [3, 9]]]],
              "label": "Y-axis label text",
              "axis_label": "X-axis label text"})
```

__Platform__: default

__Module__: [rally.task.processing.charts](https://github.com/openstack/rally/blob/master/rally/task/processing/charts.py)

<hr />

#### StatsTable [Chart]

Calculate statistics for additive data and display it as table.

This plugin processes additive data and compose statistics that is
displayed as table in HTML report.

Examples of using this plugin in Scenario, for saving output data:

```python
self.add_output(
    additive={"title": "Statistics",
              "description": ("Table with statistics generated "
                              "from all iterations values"),
              "chart_plugin": "StatsTable",
              "data": [["foo stat", 12], ["bar", 34], ["spam", 56]]})
```

__Platform__: default

__Module__: [rally.task.processing.charts](https://github.com/openstack/rally/blob/master/rally/task/processing/charts.py)

<hr />

#### Table [Chart]

Display complete output as table, can not be used for additive data.

Use this plugin for complete output data to display it in HTML report
as table. This plugin can not be used for additive data because it
does not contain any processing logic.

Examples of using this plugin in Scenario, for saving output data:

```python
self.add_output(
    complete={"title": "Arbitrary Table",
              "description": "Just show columns and rows as-is",
              "chart_plugin": "Table",
              "data": {"cols": ["foo", "bar", "spam"],
                       "rows": [["a row", 1, 2], ["b row", 3, 4],
                                ["c row", 5, 6]]}})
```

__Platform__: default

__Module__: [rally.task.processing.charts](https://github.com/openstack/rally/blob/master/rally/task/processing/charts.py)

<hr />

#### TextArea [Chart]

Arbitrary text.

This plugin processes complete data and displays of output in HTML report.

Examples of using this plugin in Scenario, for saving output data:

```python
self.add_output(
    complete={"title": "Script Inline",
              "chart_plugin": "TextArea",
              "data": ["first output", "second output",
                       "third output"]]})
```

__Platform__: default

__Module__: [rally.task.processing.charts](https://github.com/openstack/rally/blob/master/rally/task/processing/charts.py)

<hr />

### Context

#### dummy_context [Context]

Dummy context.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "properties": {
                "fail_cleanup": {
                    "type": "boolean"
                }, 
                "fail_setup": {
                    "type": "boolean"
                }
            }, 
            "additionalProperties": false
        }

__Module__: [rally.plugins.common.contexts.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/contexts/dummy.py)

<hr />

### Hook Action

Factory for hook classes.

#### sys_call [Hook Action]

Performs system call.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "string", 
            "description": "Command to execute."
        }

__Module__: [rally.plugins.common.hook.sys_call](https://github.com/openstack/rally/blob/master/rally/plugins/common/hook/sys_call.py)

<hr />

### Hook Trigger

Factory for hook trigger classes.

#### event [Hook Trigger]

Triggers hook on specified event and list of values.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "oneOf": [
                {
                    "description": "Triage hook based on specified seconds after start of workload.", 
                    "properties": {
                        "at": {
                            "type": "array", 
                            "items": {
                                "type": "integer", 
                                "minimum": 0
                            }, 
                            "minItems": 1, 
                            "uniqueItems": true
                        }, 
                        "unit": {
                            "enum": [
                                "time"
                            ]
                        }
                    }, 
                    "additionalProperties": false, 
                    "required": [
                        "unit", 
                        "at"
                    ]
                }, 
                {
                    "description": "Triage hook based on specific iterations.", 
                    "properties": {
                        "at": {
                            "type": "array", 
                            "items": {
                                "type": "integer", 
                                "minimum": 1
                            }, 
                            "minItems": 1, 
                            "uniqueItems": true
                        }, 
                        "unit": {
                            "enum": [
                                "iteration"
                            ]
                        }
                    }, 
                    "additionalProperties": false, 
                    "required": [
                        "unit", 
                        "at"
                    ]
                }
            ]
        }

__Module__: [rally.plugins.common.hook.triggers.event](https://github.com/openstack/rally/blob/master/rally/plugins/common/hook/triggers/event.py)

<hr />

#### periodic [Hook Trigger]

Periodically triggers hook with specified range and step.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "oneOf": [
                {
                    "description": "Periodically triage hook based on elapsed time after start of workload.", 
                    "properties": {
                        "end": {
                            "type": "integer", 
                            "minimum": 1
                        }, 
                        "start": {
                            "type": "integer", 
                            "minimum": 0
                        }, 
                        "step": {
                            "type": "integer", 
                            "minimum": 1
                        }, 
                        "unit": {
                            "enum": [
                                "time"
                            ]
                        }
                    }, 
                    "additionalProperties": false, 
                    "required": [
                        "unit", 
                        "step"
                    ]
                }, 
                {
                    "description": "Periodically triage hook based on iterations.", 
                    "properties": {
                        "end": {
                            "type": "integer", 
                            "minimum": 1
                        }, 
                        "start": {
                            "type": "integer", 
                            "minimum": 1
                        }, 
                        "step": {
                            "type": "integer", 
                            "minimum": 1
                        }, 
                        "unit": {
                            "enum": [
                                "iteration"
                            ]
                        }
                    }, 
                    "additionalProperties": false, 
                    "required": [
                        "unit", 
                        "step"
                    ]
                }
            ]
        }

__Module__: [rally.plugins.common.hook.triggers.periodic](https://github.com/openstack/rally/blob/master/rally/plugins/common/hook/triggers/periodic.py)

<hr />

### SLA

Factory for criteria classes.

#### failure_rate [SLA]

Failure rate minimum and maximum in percents.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "properties": {
                "max": {
                    "type": "number", 
                    "minimum": 0.0, 
                    "maximum": 100.0
                }, 
                "min": {
                    "type": "number", 
                    "minimum": 0.0, 
                    "maximum": 100.0
                }
            }, 
            "minProperties": 1, 
            "additionalProperties": false
        }

__Module__: [rally.plugins.common.sla.failure_rate](https://github.com/openstack/rally/blob/master/rally/plugins/common/sla/failure_rate.py)

<hr />

#### max_avg_duration [SLA]

Maximum average duration of one iteration in seconds.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "type": "number", 
            "minimum": 0.0, 
            "exclusiveMinimum": true
        }

__Module__: [rally.plugins.common.sla.max_average_duration](https://github.com/openstack/rally/blob/master/rally/plugins/common/sla/max_average_duration.py)

<hr />

#### max_avg_duration_per_atomic [SLA]

Maximum average duration of one iterations atomic actions in seconds.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "patternProperties": {
                ".*": {
                    "type": "number", 
                    "description": "The name of atomic action."
                }
            }, 
            "minProperties": 1, 
            "additionalProperties": false
        }

__Module__: [rally.plugins.common.sla.max_average_duration_per_atomic](https://github.com/openstack/rally/blob/master/rally/plugins/common/sla/max_average_duration_per_atomic.py)

<hr />

#### max_seconds_per_iteration [SLA]

Maximum time for one iteration in seconds.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "type": "number", 
            "minimum": 0.0, 
            "exclusiveMinimum": true
        }

__Module__: [rally.plugins.common.sla.iteration_time](https://github.com/openstack/rally/blob/master/rally/plugins/common/sla/iteration_time.py)

<hr />

#### outliers [SLA]

Limit the number of outliers (iterations that take too much time).

The outliers are detected automatically using the computation of the mean
and standard deviation (std) of the data.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "properties": {
                "max": {
                    "type": "integer", 
                    "minimum": 0
                }, 
                "min_iterations": {
                    "type": "integer", 
                    "minimum": 3
                }, 
                "sigmas": {
                    "type": "number", 
                    "minimum": 0.0, 
                    "exclusiveMinimum": true
                }
            }, 
            "additionalProperties": false
        }

__Module__: [rally.plugins.common.sla.outliers](https://github.com/openstack/rally/blob/master/rally/plugins/common/sla/outliers.py)

<hr />

#### performance_degradation [SLA]

Calculates performance degradation based on iteration time.

This SLA plugin finds minimum and maximum duration of
iterations completed without errors during Rally task execution.
Assuming that minimum duration is 100%, it calculates
performance degradation against maximum duration.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "properties": {
                "max_degradation": {
                    "type": "number", 
                    "minimum": 0.0
                }
            }, 
            "additionalProperties": false, 
            "required": [
                "max_degradation"
            ]
        }

__Module__: [rally.plugins.common.sla.performance_degradation](https://github.com/openstack/rally/blob/master/rally/plugins/common/sla/performance_degradation.py)

<hr />

### Scenario

This is base class for any scenario.

All Scenario Plugins should be subclass of this class.

#### Dummy.dummy [Scenario]

Do nothing and sleep for the given number of seconds (0 by default).

Dummy.dummy can be used for testing performance of different
ScenarioRunners and of the ability of rally to store a large
amount of results.

__Platform__: default

**Parameters**:

<a name=ScenarioDummydummy-sleep></a>

* *sleep* [[ref]](#ScenarioDummydummy-sleep)  
  idle time of method (in seconds).

__Module__: [rally.plugins.common.scenarios.dummy.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/dummy/dummy.py)

<hr />

#### Dummy.dummy_exception [Scenario]

Throws an exception.

Dummy.dummy_exception used for testing if exceptions are processed
properly by task engine and analyze rally results storing & displaying
capabilities.

__Platform__: default

**Parameters**:

<a name=ScenarioDummydummy-exception-size-of-message></a>

* *size_of_message* [[ref]](#ScenarioDummydummy-exception-size-of-message)  
  int size of the exception message
  

<a name=ScenarioDummydummy-exception-sleep></a>

* *sleep* [[ref]](#ScenarioDummydummy-exception-sleep)  
  idle time of method (in seconds).
  

<a name=ScenarioDummydummy-exception-message></a>

* *message* [[ref]](#ScenarioDummydummy-exception-message)  
  message of the exception
  

__Module__: [rally.plugins.common.scenarios.dummy.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/dummy/dummy.py)

<hr />

#### Dummy.dummy_exception_probability [Scenario]

Throws an exception with given probability.

Dummy.dummy_exception_probability used for testing if exceptions are
processed properly by task engine and analyze rally results storing
& displaying capabilities.

__Platform__: default

**Parameters**:

<a name=ScenarioDummydummy-exception-probability-exception-probability></a>

* *exception_probability* [[ref]](#ScenarioDummydummy-exception-probability-exception-probability)  
  Sets how likely it is that an exception
  will be thrown. Float between 0 and 1
  0=never 1=always.
  

__Module__: [rally.plugins.common.scenarios.dummy.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/dummy/dummy.py)

<hr />

#### Dummy.dummy_output [Scenario]

Generate dummy output.

This scenario generates example of output data.

__Platform__: default

**Parameters**:

<a name=ScenarioDummydummy-output-random-range></a>

* *random_range* [[ref]](#ScenarioDummydummy-output-random-range)  
  max int limit for generated random values

__Module__: [rally.plugins.common.scenarios.dummy.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/dummy/dummy.py)

<hr />

#### Dummy.dummy_random_action [Scenario]

Sleep random time in dummy actions.

__Platform__: default

**Parameters**:

<a name=ScenarioDummydummy-random-action-actions-num></a>

* *actions_num* [[ref]](#ScenarioDummydummy-random-action-actions-num)  
  int number of actions to generate
  

<a name=ScenarioDummydummy-random-action-sleep-min></a>

* *sleep_min* [[ref]](#ScenarioDummydummy-random-action-sleep-min)  
  minimal time to sleep, numeric seconds
  

<a name=ScenarioDummydummy-random-action-sleep-max></a>

* *sleep_max* [[ref]](#ScenarioDummydummy-random-action-sleep-max)  
  maximum time to sleep, numeric seconds

__Module__: [rally.plugins.common.scenarios.dummy.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/dummy/dummy.py)

<hr />

#### Dummy.dummy_random_fail_in_atomic [Scenario]

Dummy.dummy_random_fail_in_atomic in dummy actions.

Can be used to test atomic actions
failures processing.

__Platform__: default

**Parameters**:

<a name=ScenarioDummydummy-random-fail-in-atomic-exception-probability></a>

* *exception_probability* [[ref]](#ScenarioDummydummy-random-fail-in-atomic-exception-probability)  
  Probability with which atomic actions
  fail in this dummy scenario (0 <= p <= 1)
  

__Module__: [rally.plugins.common.scenarios.dummy.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/dummy/dummy.py)

<hr />

#### Dummy.dummy_timed_atomic_actions [Scenario]

Run some sleepy atomic actions for SLA atomic action tests.

__Platform__: default

**Parameters**:

<a name=ScenarioDummydummy-timed-atomic-actions-number-of-actions></a>

* *number_of_actions* [[ref]](#ScenarioDummydummy-timed-atomic-actions-number-of-actions)  
  int number of atomic actions to create
  

<a name=ScenarioDummydummy-timed-atomic-actions-sleep-factor></a>

* *sleep_factor* [[ref]](#ScenarioDummydummy-timed-atomic-actions-sleep-factor)  
  int multiplier for number of seconds to sleep

__Module__: [rally.plugins.common.scenarios.dummy.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/dummy/dummy.py)

<hr />

#### Dummy.failure [Scenario]

Raise errors in some iterations.

__Platform__: default

**Parameters**:

<a name=ScenarioDummyfailure-sleep></a>

* *sleep* [[ref]](#ScenarioDummyfailure-sleep)  
  float iteration sleep time in seconds
  

<a name=ScenarioDummyfailure-from-iteration></a>

* *from_iteration* [[ref]](#ScenarioDummyfailure-from-iteration)  
  int iteration number which starts range
  of failed iterations
  

<a name=ScenarioDummyfailure-to-iteration></a>

* *to_iteration* [[ref]](#ScenarioDummyfailure-to-iteration)  
  int iteration number which ends range of
  failed iterations
  

<a name=ScenarioDummyfailure-each></a>

* *each* [[ref]](#ScenarioDummyfailure-each)  
  int cyclic number of iteration which actually raises
  an error in selected range. For example, each=3 will
  raise error in each 3rd iteration.
  

__Module__: [rally.plugins.common.scenarios.dummy.dummy](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/dummy/dummy.py)

<hr />

#### HttpRequests.check_random_request [Scenario]

Executes random HTTP requests from provided list.

This scenario takes random url from list of requests, and raises
exception if the response is not the expected response.

__Platform__: default

**Parameters**:

<a name=ScenarioHttpRequestscheck-random-request-requests></a>

* *requests* [[ref]](#ScenarioHttpRequestscheck-random-request-requests)  
  List of request dicts
  

<a name=ScenarioHttpRequestscheck-random-request-status-code></a>

* *status_code* [[ref]](#ScenarioHttpRequestscheck-random-request-status-code)  
  Expected Response Code it will
  be used only if we doesn't specified it in request proper
  

__Module__: [rally.plugins.common.scenarios.requests.http_requests](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/requests/http_requests.py)

<hr />

#### HttpRequests.check_request [Scenario]

Standard way for testing web services using HTTP requests.

This scenario is used to make request and check it with expected
Response.

__Platform__: default

**Parameters**:

<a name=ScenarioHttpRequestscheck-request-url></a>

* *url* [[ref]](#ScenarioHttpRequestscheck-request-url)  
  url for the Request object
  

<a name=ScenarioHttpRequestscheck-request-method></a>

* *method* [[ref]](#ScenarioHttpRequestscheck-request-method)  
  method for the Request object
  

<a name=ScenarioHttpRequestscheck-request-status-code></a>

* *status_code* [[ref]](#ScenarioHttpRequestscheck-request-status-code)  
  expected response code
  

<a name=ScenarioHttpRequestscheck-request-kwargs></a>

* *kwargs* [[ref]](#ScenarioHttpRequestscheck-request-kwargs)  
  optional additional request parameters

__Module__: [rally.plugins.common.scenarios.requests.http_requests](https://github.com/openstack/rally/blob/master/rally/plugins/common/scenarios/requests/http_requests.py)

<hr />

### Scenario Runner

Base class for all scenario runners.

Scenario runner is an entity that implements a certain strategy of
launching scenarios plugins, e.g. running them continuously or
periodically for a given number of times or seconds.
These strategies should be implemented in subclasses of ScenarioRunner
in the_run_scenario() method.

#### constant [Scenario Runner]

Creates constant load executing a scenario a specified number of times.

This runner will place a constant load on the cloud under test by
executing each scenario iteration without pausing between iterations
up to the number of times specified in the scenario config.

The concurrency parameter of the scenario config controls the
number of concurrent iterations which execute during a single
scenario in order to simulate the activities of multiple users
placing load on the cloud under test.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "properties": {
                "concurrency": {
                    "type": "integer", 
                    "description": "The number of parallel iteration executions.", 
                    "minimum": 1
                }, 
                "max_cpu_count": {
                    "type": "integer", 
                    "description": "The maximum number of processes to create load from.", 
                    "minimum": 1
                }, 
                "timeout": {
                    "type": "number", 
                    "description": "Operation's timeout."
                }, 
                "times": {
                    "type": "integer", 
                    "description": "Total number of iteration executions.", 
                    "minimum": 1
                }
            }, 
            "additionalProperties": false
        }

__Module__: [rally.plugins.common.runners.constant](https://github.com/openstack/rally/blob/master/rally/plugins/common/runners/constant.py)

<hr />

#### constant_for_duration [Scenario Runner]

Creates constant load executing a scenario for an interval of time.

This runner will place a constant load on the cloud under test by
executing each scenario iteration without pausing between iterations
until a specified interval of time has elapsed.

The concurrency parameter of the scenario config controls the
number of concurrent iterations which execute during a single
sceanario in order to simulate the activities of multiple users
placing load on the cloud under test.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "properties": {
                "concurrency": {
                    "type": "integer", 
                    "description": "The number of parallel iteration executions.", 
                    "minimum": 1
                }, 
                "duration": {
                    "type": "number", 
                    "description": "The number of seconds during which to generate a load.", 
                    "minimum": 0.0
                }, 
                "timeout": {
                    "type": "number", 
                    "description": "Operation's timeout.", 
                    "minimum": 1
                }
            }, 
            "additionalProperties": false, 
            "required": [
                "duration"
            ]
        }

__Module__: [rally.plugins.common.runners.constant](https://github.com/openstack/rally/blob/master/rally/plugins/common/runners/constant.py)

<hr />

#### rps [Scenario Runner]

Scenario runner that does the job with specified frequency.

Every single scenario iteration is executed with specified frequency
(runs per second) in a pool of processes. The scenario will be
launched for a fixed number of times in total (specified in the config).

An example of a rps scenario is booting 1 VM per second. This
execution type is thus very helpful in understanding the maximal load that
a certain cloud can handle.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "properties": {
                "max_concurrency": {
                    "type": "integer", 
                    "minimum": 1
                }, 
                "max_cpu_count": {
                    "type": "integer", 
                    "minimum": 1
                }, 
                "rps": {
                    "anyOf": [
                        {
                            "type": "number", 
                            "description": "Generate constant requests per second during the whole workload.", 
                            "minimum": 0, 
                            "exclusiveMinimum": true
                        }, 
                        {
                            "type": "object", 
                            "description": "Increase requests per second for specified value each time after a certain number of seconds.", 
                            "properties": {
                                "duration": {
                                    "type": "number", 
                                    "minimum": 1
                                }, 
                                "end": {
                                    "type": "number", 
                                    "minimum": 1
                                }, 
                                "start": {
                                    "type": "number", 
                                    "minimum": 1
                                }, 
                                "step": {
                                    "type": "number", 
                                    "minimum": 1
                                }
                            }, 
                            "additionalProperties": false, 
                            "required": [
                                "start", 
                                "end", 
                                "step"
                            ]
                        }
                    ]
                }, 
                "timeout": {
                    "type": "number"
                }, 
                "times": {
                    "type": "integer", 
                    "minimum": 1
                }
            }, 
            "additionalProperties": false, 
            "required": [
                "times", 
                "rps"
            ]
        }

__Module__: [rally.plugins.common.runners.rps](https://github.com/openstack/rally/blob/master/rally/plugins/common/runners/rps.py)

<hr />

#### serial [Scenario Runner]

Scenario runner that executes scenarios serially.

Unlike scenario runners that execute in parallel, the serial scenario
runner executes scenarios one-by-one in the same python interpreter process
as Rally. This allows you to execute scenario without introducing
any concurrent operations as well as interactively debug the scenario
from the same command that you use to start Rally.

__Platform__: default

??? note "The input of this plugin should be valid to the following JSONSchema"
        :::json
        {
            "$schema": "http://json-schema.org/draft-04/schema", 
            "type": "object", 
            "properties": {
                "times": {
                    "type": "integer", 
                    "minimum": 1
                }
            }, 
            "additionalProperties": true
        }

__Module__: [rally.plugins.common.runners.serial](https://github.com/openstack/rally/blob/master/rally/plugins/common/runners/serial.py)

<hr />

### Task Exporter

Base class for all exporters for Tasks.

#### elastic [Task Exporter]

Exports task results to the ElasticSearch 2.x or 5.x clusters.

The exported data includes:

- Task basic information such as title, description, status,
  deployment uuid, etc.
  See rally_task_v1_data index.
- Workload information such as scenario name and configuration, runner
  type and configuration, time of the start load, success rate, sla
  details in case of errors, etc.
  See rally_workload_v1_data index.
- Separate documents for all atomic actions.
  See rally_atomic_action_data_v1 index.

The destination can be a remote server. In this case specify it like:

> <https://elastic:changeme@example.com>

Or we can dump documents to the file. The destination should look like:

> /home/foo/bar.txt

In case of an empty destination, the <http://localhost:9200> destination
will be used.

__Platform__: default

__Module__: [rally.plugins.common.exporters.elastic.exporter](https://github.com/openstack/rally/blob/master/rally/plugins/common/exporters/elastic/exporter.py)

<hr />

#### html [Task Exporter]

Generates task report in HTML format.

__Platform__: default

__Module__: [rally.plugins.common.exporters.html](https://github.com/openstack/rally/blob/master/rally/plugins/common/exporters/html.py)

<hr />

#### html-static [Task Exporter]

Generates task report in HTML format with embedded JS/CSS.

__Platform__: default

__Module__: [rally.plugins.common.exporters.html](https://github.com/openstack/rally/blob/master/rally/plugins/common/exporters/html.py)

<hr />

#### json [Task Exporter]

Generates task report in JSON format.

__Platform__: default

__Module__: [rally.plugins.common.exporters.json_exporter](https://github.com/openstack/rally/blob/master/rally/plugins/common/exporters/json_exporter.py)

<hr />

#### junit-xml [Task Exporter]

Generates task report in JUnit-XML format.

An example of the report (All dates, numbers, names appearing in this
example are fictitious. Any resemblance to real things is purely
coincidental):

```xml
<testsuites>
  <!--Report is generated by Rally 0.10.0 at 2017-06-04T05:14:00-->
  <testsuite id="task-uu-ii-dd"
             errors="0"
             failures="1"
             skipped="0"
             tests="2"
             time="75.0"
             timestamp="2017-06-04T05:14:00">
    <testcase classname="CinderVolumes"
              name="list_volumes"
              id="workload-1-uuid"
              time="29.9695231915"
              timestamp="2017-06-04T05:14:44" />
    <testcase classname="NovaServers"
              name="list_keypairs"
              id="workload-2-uuid"
              time="5"
              timestamp="2017-06-04T05:15:15">
      <failure>ooops</failure>
    </testcase>
  </testsuite>
</testsuites>
```

__Platform__: default

__Module__: [rally.plugins.common.exporters.junit](https://github.com/openstack/rally/blob/master/rally/plugins/common/exporters/junit.py)

<hr />

### Validator

A base class for all validators.

#### args-spec [Validator]

Scenario arguments validator.

__Platform__: default

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />

#### check_api_versions [Validator]

Additional validation for api_versions context.

__Platform__: default

__Module__: [rally.plugins.openstack.context.api_versions](https://github.com/openstack/rally/blob/master/rally/plugins/openstack/context/api_versions.py)

<hr />

#### check_cleanup_resources [Validator]

Validates that openstack resource managers exist.

__Platform__: default

**Parameters**:

<a name=Validatorcheck-cleanup-resources-admin-required></a>

* *admin_required* [[ref]](#Validatorcheck-cleanup-resources-admin-required)  
  describes access level to resource

__Module__: [rally.plugins.openstack.context.cleanup.base](https://github.com/openstack/rally/blob/master/rally/plugins/openstack/context/cleanup/base.py)

<hr />

#### check_constant [Validator]

Additional schema validation for constant runner.

__Platform__: default

__Module__: [rally.plugins.common.runners.constant](https://github.com/openstack/rally/blob/master/rally/plugins/common/runners/constant.py)

<hr />

#### check_rps [Validator]

Additional schema validation for rps runner.

__Platform__: default

__Module__: [rally.plugins.common.runners.rps](https://github.com/openstack/rally/blob/master/rally/plugins/common/runners/rps.py)

<hr />

#### enum [Validator]

Checks that parameter is in a list.

Ensure a parameter has the right value. This value need to be defined
in a list.

__Platform__: default

**Parameters**:

<a name=Validatorenum-param-name></a>

* *param_name* [[ref]](#Validatorenum-param-name)  
  Name of parameter to validate
  

<a name=Validatorenum-values></a>

* *values* [[ref]](#Validatorenum-values)  
  List of values accepted
  

<a name=Validatorenum-missed></a>

* *missed* [[ref]](#Validatorenum-missed)  
  Allow to accept optional parameter
  

<a name=Validatorenum-case-insensitive></a>

* *case_insensitive* [[ref]](#Validatorenum-case-insensitive)  
  Ignore case in enum values

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />

#### es_exporter_destination [Validator]

Validates the destination for ElasticSearch exporter.

In case when the destination is ElasticSearch cluster, the version of it
should be 2.* or 5.*

__Platform__: default

__Module__: [rally.plugins.common.exporters.elastic.exporter](https://github.com/openstack/rally/blob/master/rally/plugins/common/exporters/elastic/exporter.py)

<hr />

#### file_exists [Validator]

Validator checks parameter is proper path to file with proper mode.

Ensure a file exists and can be accessed with the specified mode.
Note that path to file will be expanded before access checking.

__Platform__: default

**Parameters**:

<a name=Validatorfile-exists-param-name></a>

* *param_name* [[ref]](#Validatorfile-exists-param-name)  
  Name of parameter to validate
  

<a name=Validatorfile-exists-mode></a>

* *mode* [[ref]](#Validatorfile-exists-mode)  
  Access mode to test for. This should be one of:
  * os.F_OK (file exists)
  * os.R_OK (file is readable)
  * os.W_OK (file is writable)
  * os.X_OK (file is executable)
  
  If multiple modes are required they can be added, eg:
      mode=os.R_OK+os.W_OK
  

<a name=Validatorfile-exists-required></a>

* *required* [[ref]](#Validatorfile-exists-required)  
  Boolean indicating whether this argument is required.

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />

#### jsonschema [Validator]

JSON schema validator.

__Platform__: default

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />

#### number [Validator]

Checks that parameter is a number that pass specified condition.

Ensure a parameter is within the range [minval, maxval]. This is a
closed interval so the end points are included.

__Platform__: default

**Parameters**:

<a name=Validatornumber-param-name></a>

* *param_name* [[ref]](#Validatornumber-param-name)  
  Name of parameter to validate
  

<a name=Validatornumber-minval></a>

* *minval* [[ref]](#Validatornumber-minval)  
  Lower endpoint of valid interval
  

<a name=Validatornumber-maxval></a>

* *maxval* [[ref]](#Validatornumber-maxval)  
  Upper endpoint of valid interval
  

<a name=Validatornumber-nullable></a>

* *nullable* [[ref]](#Validatornumber-nullable)  
  Allow parameter not specified, or parameter=None
  

<a name=Validatornumber-integer-only></a>

* *integer_only* [[ref]](#Validatornumber-integer-only)  
  Only accept integers

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />

#### required_contexts [Validator]

Validator checks if required contexts are specified.

__Platform__: default

**Parameters**:

<a name=Validatorrequired-contexts-contexts></a>

* *contexts* [[ref]](#Validatorrequired-contexts-contexts)  
  list of strings and tuples with context names that
  should be specified. Tuple represent 'at least one
  of the'.
  

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />

#### required_param_or_context [Validator]

Validator checks if required image is specified.

__Platform__: default

**Parameters**:

<a name=Validatorrequired-param-or-context-param-name></a>

* *param_name* [[ref]](#Validatorrequired-param-or-context-param-name)  
  name of parameter
  

<a name=Validatorrequired-param-or-context-ctx-name></a>

* *ctx_name* [[ref]](#Validatorrequired-param-or-context-ctx-name)  
  name of context

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />

#### required_params [Validator]

Scenario required parameter validator.

This allows us to search required parameters in subdict of config.

__Platform__: default

**Parameters**:

<a name=Validatorrequired-params-subdict></a>

* *subdict* [[ref]](#Validatorrequired-params-subdict)  
  sub-dict of "config" to search. if
  not defined - will search in "config"
  

<a name=Validatorrequired-params-params></a>

* *params* [[ref]](#Validatorrequired-params-params)  
  list of required parameters

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />

#### required_platform [Validator]

Validates credentials for specified platform.

This allows us to create 4 kind of tests cases:
1) platform independent (validator is not specified)
2) requires platform with admin
3) requires platform with admin + users
4) requires platform with users

__Platform__: default

**Parameters**:

<a name=Validatorrequired-platform-platform></a>

* *platform* [[ref]](#Validatorrequired-platform-platform)  
  name of the platform
  

<a name=Validatorrequired-platform-admin></a>

* *admin* [[ref]](#Validatorrequired-platform-admin)  
  requires admin credential
  

<a name=Validatorrequired-platform-users></a>

* *users* [[ref]](#Validatorrequired-platform-users)  
  requires user credentials

__Module__: [rally.common.validation](https://github.com/openstack/rally/blob/master/rally/common/validation.py)

<hr />

#### restricted_parameters [Validator]

Validates that parameters is not set.

__Platform__: default

**Parameters**:

<a name=Validatorrestricted-parameters-param-names></a>

* *param_names* [[ref]](#Validatorrestricted-parameters-param-names)  
  parameter or parameters list to be validated.
  

<a name=Validatorrestricted-parameters-subdict></a>

* *subdict* [[ref]](#Validatorrestricted-parameters-subdict)  
  sub-dict of "config" to search for param_names. if
  not defined - will search in "config"
  

__Module__: [rally.plugins.common.validators](https://github.com/openstack/rally/blob/master/rally/plugins/common/validators.py)

<hr />