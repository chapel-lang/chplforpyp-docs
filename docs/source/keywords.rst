.. warning::
    This page was contributed in 2015 and is not being actively maintained.  Please refer to chapel-lang.org/docs instead.

Keywords
--------

You might stumble over keywords in Chapel that you did not see coming. The following code might look harmless for a Python programmer:

.. literalinclude:: /examples/beginIsKeyword.chpl
    :language: chapel

However, in Chapel ``begin`` is a keyword for one of the task-parallelism features of the language. The above will therefore produce an error along the lines of ``syntax error: near 'begin'``. Chapel uses the following keywords::

    _           align       atomic      begin       break
    by          class       cobegin     coforall    config
    const       continue    delete      dmapped     do      
    domain      else        enum        export      extern
    for         forall      if          in          index
    inline      inout       iter        label       let 
    local       module      new         nil         on  
    otherwise   out         param       proc        record
    reduce      ref         return      scan        select
    serial      single      sparse      subdomain   sync
    then        type        union       use         var
    when        where       while       yield       zip

