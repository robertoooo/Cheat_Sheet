# Mocker

### Mocking an object
```py
mocker.patch.object(object, 'attribute_name', attribute_value)
```

### Mocking a method
```py
mocker.patch("dir1.dir2.script.class.method")
mocker.patch("dir1.dir2.script.class.method", return_value="anything", new_callable=mocker.PropertyMock, create=True))

```

### Creating a mock object
With configure mock:
```py
attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
mock = mocker.Mock(some_attribute='eggs', **attrs)
mock.some_attribute
-> 'eggs'
mock.method()
-> 3
```
